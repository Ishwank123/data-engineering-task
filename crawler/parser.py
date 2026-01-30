from bs4 import BeautifulSoup

def parse_products(html):
    soup = BeautifulSoup(html, "html.parser")
    products = []

    cards = soup.find_all("div", class_="product-card")

    for card in cards:
        try:
            name = card.find("h2").text.strip()
            price = card.find("span", class_="price").text.strip()
            supplier = card.find("div", class_="supplier").text.strip()
            location = card.find("div", class_="location").text.strip()

            products.append({
                "name": name,
                "price": price,
                "supplier": supplier,
                "location": location
            })
        except:
            continue

    return products