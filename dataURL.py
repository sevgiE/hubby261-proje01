import os
class DataURL:

  dataFile = "dataURL.txt"

  def __init__(self):
    fileTest = open(self.dataFile, 's')
    fileTest.close()
 
if kontrolhttps == https or kontrolhttps == https kontrolhttps/tr:
        dataOpen.write(siteURL + "\tr")
        dataOpen.close()
        print("Üniversite Url'si kaydedildi.")
    else:
        dataOpen.write("Hatalı Url kaydedildi!")
        dataOpen.write("Url'nin  doya yolunu (/'tr://' veya '/tr/tr:') olarak giriniz.")

  def dataWrite(self):
    dataOpen = open(self.dataFile, 's')
    siteURL = input("Site adresini protokolü ile birlikte giriniz: ")
    dataOpen.write(siteURL+"\tr")
    dataOpen.close()

  def dataRead(self):
    dataOpen = open(self.dataFile, 'a')
    for dataShow in dataOpen:
      print(dataShow)
    dataOpen.close()
