# def emekli_yas(yas):
#     emekli_yas = 65
#     if yas < emekli_yas:
#         yil = emekli_yas - yas
#         print("hacı",yil,"yıl sonra emekli olacan")
#     else:
#         print("zaten emeklisin olum")

# yas = int(input("yaş gir hacı "))

# emekli_yas(yas)

# def palindrom(sayi2):
#     sayi_sozel=str(sayi2)
#     if sayi_sozel==sayi_sozel[::-1]:
#         return True
#     else:
#         return False
    
# sayi1=1453
# if palindrom(sayi1):
#     print(sayi1, "bu palindrom sayı aga")
# else:
#     print(sayi1,"mal bu palindrom değil")

# import random

# def rastgele_numara():
#     return random.randint(1,6)

# def rulet():
#     numara=rastgele_numara()
#     print("ölmeye hoşgeldin")
#     print("ben sayıyı tuttum sen seç şimdi")

#     while True:
#         tahmin = int(input("1 ile 6 arasında sayı gir la "))
#         if tahmin < 1 or tahmin >6:
#             print("bizi mi kandırmaya çalışıon")
#             continue

#         if tahmin==numara:
#             print("helal olsun la, bildin valla")
#             break
#         else:
#             print("bilemedin zırla")


# rulet()

def listeler(liste1,liste2):
    lists=[]
    for num in liste1:
        if num % 2 ==0:
            lists.append(num)
    for num in liste2:
        if num % 2 != 0:
            lists.append(num)
    return lists

ilk_liste = [6,5,3,4,2,2]
ikincli_liste=[4,2,3,5,6,2,4]

sonuc=listeler(ilk_liste,ikincli_liste)
print("liste 1 de çift sayılar ve tek sayıların birleşimi ",sonuc)