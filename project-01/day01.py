import requests
from datetime import date

headers = {"User-Agent": "Mozilla/5.0"}

fashion_sites = [
    {"site_name": "H&M", "url": "https://www.hm.com"},
    {"site_name": "Zara", "url": "https://www.zara.com"},
    {"site_name": "Uniqlo", "url": "https://www.uniqlo.com"},
    {"site_name": "Forever 21", "url": "https://www.forever21.com"},
    {"site_name": "Gap", "url": "https://www.gap.com"},
    {"site_name": "Old Navy", "url": "https://www.oldnavy.com"},
    {"site_name": "American Eagle", "url": "https://www.ae.com"},
    {"site_name": "Abercrombie & Fitch", "url": "https://www.abercrombie.com"},
    {"site_name": "Hollister", "url": "https://www.hollisterco.com"},
    {"site_name": "Aritzia", "url": "https://www.aritzia.com"},
    {"site_name": "Shein", "url": "https://www.shein.com"},
    {"site_name": "ASOS", "url": "https://www.asos.com"},
    {"site_name": "Fashion Nova", "url": "https://www.fashionnova.com"},
    {"site_name": "Boohoo", "url": "https://www.boohoo.com"},
    {"site_name": "PrettyLittleThing", "url": "https://www.prettylittlething.com"}
]

print("=" * 44)
print("   Site Availability Checker")
print("   Date:", date.today())
print("=" * 44)

accessible_count = 0

for site in fashion_sites:

    try:
        response = requests.get(site["url"], headers=headers, timeout=5)

        site["status_code"] = response.status_code
        site["accessible"] = (response.status_code == 200)
        site["page_size"] = len(response.text)

    except requests.exceptions.Timeout:
        site["status_code"] = "Timeout"
        site["accessible"] = False
        site["page_size"] = 0

    except requests.exceptions.RequestException:
        site["status_code"] = "Error"
        site["accessible"] = False
        site["page_size"] = 0

    if site["accessible"]:
        accessible_count += 1

    print("\nSite:", site["site_name"])
    print("URL:", site["url"])
    print("Status:", site["status_code"])
    print("Accessible:", site["accessible"])
    print("Page Size:", site["page_size"], "characters")
    print("-" * 44)

print(
    f"\nSUMMARY: {accessible_count} out of {len(fashion_sites)} sites accessible today.")
