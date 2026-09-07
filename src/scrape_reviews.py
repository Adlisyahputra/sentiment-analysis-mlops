from google_play_scraper import reviews, Sort
import pandas as pd

apps = {
    "gopay": "com.gojek.gopay",
    "dana": "id.dana",
    "ovo": "ovo.id",
}

all_reviews = []

for app_name, app_id in apps.items():
    print(f"Scraping {app_name}...")
    result, _ = reviews(
        app_id,
        lang="id",
        country="id",
        sort=Sort.NEWEST,
        count=100,
    )
    for r in result:
        r["app"] = app_name
    all_reviews.extend(result)

df = pd.DataFrame(all_reviews)
df.to_csv("data/raw/ewallet_reviews.csv", index=False)
print(f"Selesai. Total {len(df)} review disimpan.")