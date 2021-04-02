import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from requests_html import HTMLSession

####ASAMA1 ISLEMLERİ#####
#verilen urldeki html içeriği get_text() sayesinde tüm textler alınır. sonrasında semboller temizlenir.
def parseHTML(urlDegeri):
   r = requests.get(urlDegeri)
   soup = BeautifulSoup(r.content,"lxml")

   return soup.get_text()

#htmlden parse edilen verileri küçük harf şeklinde alır ve sembolleri temizler.
def sembolTemizle(tumKelimeler):
    temizlenmisKelimeler = []
    tumSemboller = "!@#$%^&*()_−+={[}]|\;:<>?/.,−--"
    for kelime in tumKelimeler:
        for sembol in tumSemboller :
          if sembol in kelime :
            kelime = kelime.replace(sembol,"")
        if(len(kelime)>0 and len(kelime)<20):
            temizlenmisKelimeler.append(kelime)
    return temizlenmisKelimeler


#temizlenen kelimeleri alıp sayısını sayar.
def sozlukOlustur(tumKelimeler):
    kelimeSayisi = {}
    for kelime in tumKelimeler:
        if kelime in kelimeSayisi:
            kelimeSayisi[kelime] +=1
        else:
            kelimeSayisi[kelime] = 1
    return kelimeSayisi

#sözlük oluşturulup frekansları belirlendikten sonra büyükten küçüğe sıralama yapılır.
def sozluguSirala(tumSozluk):
    return {key:value for key,value in sorted(tumSozluk.items(),key=lambda x:x[1],reverse=True)}


#### ASAMA2 ISLEMLERİ ####
def csvOku():
    yeniListe = []

    # burada veriler csv den array içinde array yapısında gelmektedir. yani [['the'],['and']] gibi. tek arraya düşüreceğiz
    dosya = [line.strip() for line in open("cikarilacak_kelimeler.csv", 'r')]
    data = [[word.lower() for word in text.split()] for text in dosya]

    for i in range(len(data)):
        yeniListe.append(data[i][0])
    return yeniListe


#### ASAMA 4 ISLEMLERİ ####
yeniListe = {}

def recursiveUrl(link, depth,yeniListe,anaLink):
    domain_name = urlparse(link).netloc
    count=0
    if depth < 3:
        session = HTMLSession()
        response = session.get(link)
        sayfaLinkleri = response.html.absolute_links

        for sayfaLinki in sayfaLinkleri:
            if count==3:
                break
            ##linkler sadeleştirildi ve sadece domaindeki linkler alındı.
            parsed_href = urlparse(sayfaLinki)
            sayfaLinki = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
            if domain_name not in sayfaLinki:
                continue
            if sayfaLinki == link:
                continue
            if sayfaLinki == parsed_href.scheme + "://" + parsed_href.netloc:
                continue
            if anaLink == link:
                continue
            ##linkler sadeleştirildi ve sadece domaindeki linkler alındı.
            if sayfaLinki in yeniListe:
                continue
            else:
                yeniListe[sayfaLinki] = 3
            count=count+1

def getLinks(url):
    session = HTMLSession()
    response = session.get(url)
    count =0

    domain_name = urlparse(url).netloc
    links = response.html.absolute_links

    for link in links :
        if count==3:
            break
        ##linkler sadeleştirildi ve sadece domaindeki linkler alındı.
        parsed_href = urlparse(link)
        link = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if domain_name not in link:
            continue
        if url == link:
            continue
        if link in yeniListe:
            continue
        ##linkler sadeleştirildi ve sadece domaindeki linkler alındı.
        if link not in yeniListe:
            if len(yeniListe)==5:
                break
            yeniListe[link]=2
        recursiveUrl(link,2,yeniListe,url)
        count = count+1
    return yeniListe

def ikiLinkiKarsilastirSkorHesapla(birinciLinkTumSozluk,ikinciLinkTumSozluk,ayniKelimelerTumSozluk):
    birinciLinkKelimeSayisi = len(birinciLinkTumSozluk)
    ikinciLinkKelimeSayisi = len(ikinciLinkTumSozluk)
    ayniKelimeSayisi = len(ayniKelimelerTumSozluk)
    if(ayniKelimeSayisi>0):
        islem = (((ayniKelimeSayisi/birinciLinkKelimeSayisi)+(ayniKelimeSayisi/ikinciLinkKelimeSayisi))/2)*100
    else:
        islem=0
    islem = round(islem,2)

    return islem

def karsilastirmaSonuclariniSirala(tumSozluk):
    return {key:value for key,value in sorted(tumSozluk.items(),key=lambda x:x[1][3],reverse=True)}


#### ASAMA 5 ISLEMLERİ ####
def apiyiAl(anahtarKelimeler):

    synonymKelimeler = {}
    for key,value in anahtarKelimeler.items():
        url = "https://api.datamuse.com/words"
        r = requests.get(url, params={"rel_syn": key})
        jsonVerisi = r.json()

        if jsonVerisi:
            for yakinAnlamliKelime in jsonVerisi:
                synonymKelimeler[key] = yakinAnlamliKelime["word"]
                print("Anahtar Kelime="+ key +" -> "+  synonymKelimeler[key])
                break
        else:
            continue

    return synonymKelimeler



def tumSozluktenAnahtarKelimeleriAl(tumSozluk):
    anahtarKelimeler = {}
    for key,value in tumSozluk.items():
       if len(anahtarKelimeler)==10:
           break
       else:
         anahtarKelimeler[key]= value

    return anahtarKelimeler
