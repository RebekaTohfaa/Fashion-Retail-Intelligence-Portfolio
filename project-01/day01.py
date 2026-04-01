import requests
from datetime import date


headers = {"User-Agent": "Mozilla/5.0"}

fashion_sites = [
    {"site_name": "H&M", "url": "https://www2.hm.com/en_gb/ladies/new-arrivals/clothes.html"},
    {"site_name": "Books", "url": "https://books.toscrape.com"},
    {"site_name": "Quotes", "url": "https://quotes.toscrape.com"}]


print("=" * 44)
print("   FASHION SITE INTELLIGENCE REPORT")
print("   Date:", date.today())
print("=" * 44)

accessible_count = 0

for site in fashion_sites:
    response = requests.get(site["url"], headers=headers)

    site["status_code"] = response.status_code
    site["accessible"] = (response.status_code == 200)
    site["page_size"] = len(response.text)

    if site["accessible"]:
        accessible_count += 1

    print("\nSite:", site["site_name"])
    print("URL:", site["url"])
    print("Status:", site["status_code"])
    print("Accessible:", site["accessible"])
    print("Page Size:", site["page_size"], "characters")
    print("-" * 44)

print(f"\nSUMMARY: {accessible_count} out of 3 sites accessible today.")
