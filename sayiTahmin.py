import random

def sayi_tut():
    sayi = random.randint(0,100)
    return sayi

def tahmin_et():
    tahmin = int(input("Tahmininizi girin....:"))
    return tahmin

tahmin_edilecek = sayi_tut()

tahmin = tahmin_et()

if tahmin > tahmin_edilecek:
    print("Daha küçük sayı girin ...")
elif tahmin < tahmin_edilecek:
    print("Daha büyük sayı girin ...")
else:
    print("Doğru tahmin")
