"""
This script will get the winning numbers from the Loto quebec website
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://loteries.lotoquebec.com/en/lotteries/celebration-2024")
    texts = page.locator(
        ".lqZonePretiragesParDates"
    ).all_inner_texts()  # text example ['2023-12-01\n893B159']
    with open("winning_numbers.csv", "w", encoding="utf-8") as f:
        f.write("date,winning_numbers\n")
        for text in texts:
            f.write(",".join(text.split("\n")))
            f.write("\n")
