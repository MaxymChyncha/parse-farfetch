import scrapy

from scrapy.exceptions import CloseSpider
from scrapy.http import Response


class FarfetchSpider(scrapy.Spider):
    name = "farfetch"
    allowed_domains = ["www.farfetch.com"]
    start_urls = ["https://www.farfetch.com/ca/shopping/women/dresses-1/items.aspx"]

    def __init__(self, *args, **kwargs) -> None:
        super(FarfetchSpider, self).__init__(*args, **kwargs)
        self.parsed_items = 0
        self.max_items = 124

    def parse(self, response: Response, **kwargs) -> None:
        dress_detail_urls = response.css("li[data-testid='productCard']").css("a")
        for dress_detail_url in dress_detail_urls:
            yield response.follow(dress_detail_url, self._get_one_dress)

        next_page = (
            "https://www.farfetch.com/ca/shopping/women/dresses-1/items.aspx?page=2&view=96&sort=3"
        )
        yield scrapy.Request(next_page, callback=self.parse)

    @staticmethod
    def _get_color(response: Response) -> str:
        return (
            response.css("ul._fdc1e5")
            .css("li[data-component='Body']::text")[0]
            .get()
            .strip()
        )

    @staticmethod
    def _get_product_type(response: Response) -> str:
        product_types_li_elements = response.css("ol[data-component='Breadcrumbs'] li")

        return " ".join(
            [
                f"{li_product_type.css('a::text').get()};"
                for li_product_type in product_types_li_elements
            ]
        )

    def _get_one_dress(self, response: Response) -> dict:
        if self.parsed_items >= self.max_items:
            self.logger.info(f"Parsed 120 items. Stopping the spider.")
            raise CloseSpider(reason=f"Parsed 120 items.")

        self.parsed_items += 1

        yield {
            "id": (
                response.css("p:contains('FARFETCH ID:')").css("span::text").get().strip()
            ),
            "item_group_id": (
                response.css("p:contains('Brand style ID:')").css("span::text").get().strip()
            ),
            "mpn": (
                response.css("p:contains('Brand style ID:')").css("span::text").get().strip()
            ),
            "title": response.css("p[data-testid='product-short-description']::text").get(),
            "description": None,
            "image_link": response.css("div:nth-child(5) img")[0].attrib["src"],
            "additional_image_link": response.css("div:nth-child(5) img")[1].attrib["src"],
            "url": response.url,
            "gender": response.xpath(
                "normalize-space(//script[contains(text(), 'window.universal_variable')]/text())"
            ).re_first(r"'name':'(.*?)'"),
            "age_group": "adult",
            "brand": response.css("div:nth-child(5)").css("h1").css("a::text").get(),
            "color": self._get_color(response),
            "size": None,
            "availability": "in stock",
            "price": response.css("p[data-component='PriceLarge']::text").get(),
            "condition": None,
            "product_type": self._get_product_type(response),
            "google_product_category": 2271,
        }
