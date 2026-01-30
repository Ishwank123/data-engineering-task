from .config import BASE_URL, CATEGORIES, MAX_PAGES
from .fetcher import fetch_page
from .parser import parse_products
from .pipeline import save_to_csv

def crawl_category(category):
    all_products = []

    for page in range(1, MAX_PAGES + 1):
        url = f"{BASE_URL}/{category}?page={page}"
        html = fetch_page(url)

        if html:
            products = parse_products(html)
            all_products.extend(products)

    save_to_csv(all_products, category)

if __name__ == "__main__":
    for category in CATEGORIES:
        crawl_category(category)

