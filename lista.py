zakupy = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "Rukola"]
}
for sklep, rzeczy in zakupy.items():
    x = f"Idę do {sklep}, kupuję tu następujące rzeczy {rzeczy}"
    print(x)