# Farfetch parser

## Features
- Web Scraping: Use Scrapy to extract information about dresses.
- Data preparing: Save your data in XML format to pass it to CMS.

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
