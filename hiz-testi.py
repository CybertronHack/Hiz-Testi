import time
import datetime
import random

metinler = ["hello world", "siber dunya", "cyber world", "siber adam", "cyber man", "CybertonHack"]
random_metin = random.choice(metinler)
print("Girmeniz gereken metin : ")
print(random_metin)


print("Hazırsan 'Enter' Tuşuna Basınız")
input()

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("Hadi!")
time.sleep(0.2)
onceki = datetime.datetime.now()

metin=input("Metin Giriniz : ")
sonraki = datetime.datetime.now()

if metin == random_metin:
	speed = sonraki - onceki
	seconds = round(speed.total_seconds(),2)
	letter_per_second = round(len(metin) / seconds,1)
	
	print("Metini {} Saniyede Yazdınız.".format(seconds))
	print("Saniye Başına Girilen Harf {} Hızı".format(letter_per_second))
else:
	print("Hata!!")
