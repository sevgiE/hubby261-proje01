import time
from dataURL import DataURL
from getURL import GetURL

useDataURL = DataURL()
useGetURL = GetURL()

print(" Sevgi'nin mini örümceğine hoşgeldiniz! " )
print(" İçeride çay hizmetimiz bulunmaktadır.( İndirimde 5 lira) ")
print("|🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️|")
nick = input("Lütfen nickinizi giriniz: ")
print("Merhaba!" '\n' + nick + '\n' "Mini örümcek emrinize amadedir, ne istediğinizi lütfen geçerli numaralı sayılarla belirtiniz!!!" + "\n")
print("")
time.sleep(2)


while True:
    print("Menü: 0)Çıkış 1)URL Listele 2)URL Ekle 3)Örümcek Gönder 4)Sonuçları Listele ")
    sayiSecim = int(input("Yapmak istediğiniz işlemin numarasını giriniz: "))
    if menuSecim == 0:
        print("Sevgi'nin Mini Örümceği kapatılıyor... Tekrar görüşmek dileğiyle ._.🕷️")
        
    elif sayiSecim== 1:
        useDataURL.dataRead()
    elif sayiSecim == 2:
        useDataURL.dataWrite()
    elif sayiSecim == 3:
        useGetURL.getWeb()
    elif sayiSecim == 4:
        useGetURL.getList()
    elif sayiSecim == 0:
        useDataURL.dataBreak()
      
else:
       print("Lütfen numaraları verilen sayılar haricinde girmeyiniz.(SAYILAR: 0,1,2,3,4)!")
       print("Menü başa sarılıyor...")
    time.sleep(2)
  
      
