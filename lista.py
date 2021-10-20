zakupy = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "Rukola"]
}
for sklep, rzeczy in zakupy.items():
    sklep = sklep.capitalize()
    rzeczy[0] = rzeczy[0].capitalize()
    rzeczy[1] = rzeczy[1].capitalize()
    rzeczy[2] = rzeczy[2].capitalize()
    wartosc.append(rzeczy)
    x = f"Idę do {sklep}, kupuję tu następujące rzeczy {rzeczy}"
    print(x)
wartosc1 = len(wartosc[0]) + len(wartosc[1])
print(f"W sumie kupuję {wartosc1} produktów.")