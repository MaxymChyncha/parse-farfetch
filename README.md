# Farfetch parser

## Features
- Scrape 120 Listings: The script efficiently scrapes data from the first 120 dress listings on Farfetch's women's dresses page.
- Data Extraction: Extract essential information such as product titles, prices, brands, and more.
- Google Merchant Feed Format: Transforms the scraped data into a format suitable for Google Merchant feeds, ensuring compatibility with CMS platforms.
- Easy Integration: Provides a seamless process to integrate the data into your CMS for e-commerce purposes.

## Installation

To clone this project from GitHub, follow these steps:

1. **Open your terminal or command prompt.**
2. **Navigate to the directory where you want to clone the project.**
3. **Run the following commands:**
```shell
git clone https://github.com/MaxymChyncha/scrape-farfetch
python -m venv venv
source venv/bin/activate  #for Windows use: venv\Scripts\activate
```

4. **Install requirements:**

```shell
pip install -r requirements.txt
```

5. **Run the Web Scraping Script:**
```shell
cd webscraping/
scrapy crawl farfetch -O farfetch_feed.xml
```

### Example of scraped data you can find with [link](https://drive.google.com/file/d/1Wzx91iJW9SDPQUj0bBOriEZuAKQO-VU6/view?usp=sharing).
