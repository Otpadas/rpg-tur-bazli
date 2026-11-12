player_cord = input("Oyuncunun koordinatlarını giriniz (Örnek: 10.20): ").split(".")
enemy_cord = input("Düşmanın koordinatlarını giriniz (Örnek: 20.70): ").split(".")

px, py = float(player_cord[0]), float(player_cord[1])
ex, ey = float(enemy_cord[0]), float(enemy_cord[1])

menzil = float(input("Silah menzilinizi giriniz: "))

xfark = px - ex
yfark = py - ey
mesafe = (xfark**2 + yfark**2) ** 0.5

player_can = 100.00
enemy_can = 10000.00

if mesafe > menzil:
    print(f"\nMenziliniz yetersiz! (Mesafe: {mesafe:.2f} | Menzil: {menzil:.2f})")
    print("Düşmana yaklaşılırken ağır ateş altında kaldınız!")
    uzaklik_h = mesafe - menzil
    uzaklik_hs = uzaklik_h * 5
    player_can -= uzaklik_hs
    print(f"Yaklaşırken {uzaklik_hs:.2f} hasar aldınız! Kalan Canınız: {player_can:.2f}\n")
    
    if player_can <= 0:
        print("Düşmana ulaşamadan yolda öldünüz!")
        exit()

dmg = float(input("Karakterinizin temel saldırı gücünü giriniz: "))
krtk = float(input("Yüzdelik olarak kritik oranınızı giriniz (%): "))

player_element = input("Saldırı elementiniz? (Ateş/Su/Buz/Normal): ").lower()
if player_element not in ["ateş", "su", "buz", "normal"]:
    print("Hatalı giriş.")
    exit()

enemy_element = input("Düşmanın elementi? (Ateş/Su/Buz/Normal): ").lower()
if enemy_element not in ["ateş", "su", "buz", "normal"]:
    print("Hatalı giriş.")
    exit()

player_reaksiyon = "Normal (x1.0)"
if player_element == "ateş":
    if enemy_element == "buz":
        dmg *= 2.0
        player_reaksiyon = "Eritme (x2.0)"
    elif enemy_element == "ateş":
        dmg *= 0.75
        player_reaksiyon = "Direnç (x0.75)"
    elif enemy_element == "su":
        dmg *= 0.5
        player_reaksiyon = "Zayıf (x0.5)"
elif player_element == "su":
    if enemy_element == "ateş":
        dmg *= 2.0
        player_reaksiyon = "Buharlaşma (x2.0)"
    elif enemy_element == "su":
        dmg *= 0.75
        player_reaksiyon = "Direnç (x0.75)"
    elif enemy_element == "buz":
        dmg *= 0.5
        player_reaksiyon = "ZAyıf (x0.5)"
elif player_element == "buz":
    if enemy_element == "su":
        dmg *= 2.0
        player_reaksiyon = "Dondurma (x2.0)"
    elif enemy_element == "ateş":
        dmg *= 0.5
        player_reaksiyon = "Zayıf (x0.5)"
    elif enemy_element == "buz":
        dmg *= 0.75
        player_reaksiyon = "Direnç (x0.75)"

enemy_dmg = 10.0
enemy_reaksiyon = "Normal (x1.0)"
if enemy_element == "ateş":
    if player_element == "buz":
        enemy_dmg *= 2.0
        enemy_reaksiyon = "Eritme (x2.0)"
    elif player_element == "ateş":
        enemy_dmg *= 0.75
        enemy_reaksiyon = "Direnç (x0.75)"
    elif player_element == "su":
        enemy_dmg *= 0.5
        enemy_reaksiyon = "Zayıf (x0.5)"
elif enemy_element == "su":
    if player_element == "ateş":
        enemy_dmg *= 2.0
        enemy_reaksiyon = "Buharlaşma (x2.0)"
    elif player_element == "su":
        enemy_dmg *= 0.75
        enemy_reaksiyon = "Direnç (x0.75)"
    elif player_element == "buz":
        enemy_dmg *= 0.5
        enemy_reaksiyon = "Zayıf (x0.5)"
elif player_element == "buz":
    if player_element == "su":
        enemy_dmg *= 2.0
        enemy_reaksiyon = "Dondurma (x2.0)"
    elif player_element == "ateş":
        enemy_dmg *= 0.5
        enemy_reaksiyon = "Zayıf (x0.5)"
    elif player_element == "buz":
        enemy_dmg *= 0.75
        enemy_reaksiyon = "Direnç (x0.75)"

krtk_dmg = dmg * (1 + (krtk / 100))
ilk_vurus_kritik_mi = False

ilk_vurus = input("İlk vuruşunuz kritik mi? (Evet/Hayır): ").lower()
if ilk_vurus == "evet":
    ilk_vurus_kritik_mi = True
    vurulan_ilk_hasar = krtk_dmg
elif ilk_vurus == "hayır":
    vurulan_ilk_hasar = dmg
else:
    print("Hatalı giriş.")
    exit()

enemy_can -= vurulan_ilk_hasar
durum = ""

if enemy_can <= 0:
    enemy_can = 0
    durum = "KAZANDINIZ (İlk vuruşta Boss tek yedi!)"
else:
    tur = 1
    while tur <= 3 and enemy_can > 0 and player_can > 0:
        enemy_can -= dmg
        if enemy_can <= 0:
            enemy_can = 0
            durum = "KAZANDINIZ (Düşman yok edildi!)"
            break
            
        player_can -= enemy_dmg
        if player_can <= 0:
            player_can = 0
            durum = "KAYBETTİNİZ)"
            break
        tur += 1
    if durum == "":
        durum = "DÜŞMAN KAÇTI!)"

print("\n" + "=" * 48)
print("             SAVAŞ VE HASAR RAPORU              ")
print("=" * 48)
print(f"Mesafe:\t\t\t\t{mesafe:.2f} birim")
print(f"Kritik Vuruş Durumu:\t\t{'KRİTİK!' if ilk_vurus_kritik_mi else 'Normal'}")
print(f"Senin Element Reaksiyonun:\t{player_reaksiyon}")
print(f"Düşmanın Reaksiyonu:\t\t{enemy_reaksiyon}")
print("-" * 48)
print(f"İlk Vuruş Net Hasarın:\t\t{vurulan_ilk_hasar:.2f}")
print(f"Tur Başı Vurduğun Hasar:\t{dmg:.2f}")
print(f"Tur Başı Yediğin Hasar:\t\t{enemy_dmg:.2f}")
print("-" * 48)
print(f"Kalan Oyuncu Canı:\t\t{player_can:.2f} HP")
print(f"Kalan Düşman Canı:\t\t{enemy_can:.2f} HP")
print(f"SONUÇ:\t\t\t\t{durum}")
print("=" * 48)
