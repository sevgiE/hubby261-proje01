import urllib.request
from bs4 import BeautifulSoup

class GetURL:

    dataFile = "dataURL.txt"
    getFile = "getURL.txt"

    def __init__(self):
        fileTest = open(self.getFile, 'a')
        fileTest.close()

    def getWeb(self):

        print("Mini örümcek yükleniyor... Lütfen bekleyiniz._.")

        dataOpen = open(self.dataFile, 'r')
        getOpen = open(self.getFile, 'w')

        for dataGet in dataOpen:
            webSite = urllib.request.urlopen(dataGet)
            getBytes = webSite.read()
            webPage = getBytes.decode("utf8")
            webSite.close()
            soup = BeautifulSoup(webPage, 'html.parser')
            getOpen.write(dataGet.strip() + " - " + soup.title.contents[0] + "\n")
        dataFile.close()
        getFile.close()

        print("Çalışma oluşturuldu!")

    def getList(self):

        getOpen = open(self.getFile, 'w')
        for dataShow in getOpen:
          print(dataShow)
        getFile.close()
        
        dataFile = open(self.dataFile, 'r')
        for dataShow in dataFile:
          print(dataShow)
        dataFile.close()
