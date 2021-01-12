class Insan():
    def __init__(self, ad, soyad, yas, ulke, sehir, yetenekler):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []


kisi = Insan(input("Adınızı Giriniz: "), input("Soyadınızı Giriniz: "), int(input("Yaşınızı Giriniz: ")), input("Ülkenizi Giriniz: "), input("Şehirinizi Giriniz: "), "")

def yetenek_ekle():
    kisi.yetenekler.append(input("Yetenek Giriniz: "))
    kisi.yetenekler.append(input("Yetenek Giriniz: "))
    kisi.yetenekler.append(input("Yetenek Giriniz: "))

def kisi_bilgileri(kisi):
    return print("Ad Soyad: " + kisi.ad, kisi.soyad + "\n" + "Yas: " + str(kisi.yas) + "\n" + "Ulke: " + kisi.ulke + "\n" + "Sehir: " + kisi.sehir + ("\nYetenekler: " + str(kisi.yetenekler)))

yetenek_ekle()
kisi_bilgileri(kisi)
