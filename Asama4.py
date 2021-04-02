from urllib.parse import urlparse, urljoin
from requests_html import HTMLSession
import GenelFonksiyonlar as genelFonksiyonlar

def Asama4Islemleri(birinciLink,urlKumesi):
    veriler=[]
    ##ANA LİNK İŞLEMLERİ
    # içerik alınması için parsehtml komutu çalıştırılır ve sitedeki tüm textler get_text ile döndürülür.
    birinciLinkIcerikAl = genelFonksiyonlar.parseHTML(birinciLink)
    # içerik alınıp tüm harfler küçük harfe çevrilir.
    birinciLinkIcerik = birinciLinkIcerikAl.lower().split()

    # alınan içerik gereksiz sembollerden temizlenir.
    birinciSayfaKelimeleri = genelFonksiyonlar.sembolTemizle(birinciLinkIcerik)

    # temizlenmis cikarilacak kelimeler alinir
    cikarilacak_kelimeler = genelFonksiyonlar.csvOku()

    # sayfadaki kelimelerden çıkarılacak kelimeler çıkarılır.
    dizidenKelimeleriCikart = lambda list1, list2: list(filter(lambda element: element not in list2, list1))

    # sözlük oluşturulur
    birinciSayfaTumSozluk = genelFonksiyonlar.sozlukOlustur(
    dizidenKelimeleriCikart(birinciSayfaKelimeleri, cikarilacak_kelimeler))

    urlKumesiListe = urlKumesi.split("\r\n")


    for urlKumesiLink in urlKumesiListe:
        urlKumesiAltLinkler = genelFonksiyonlar.getLinks(urlKumesiLink)


    for ikinciLink in urlKumesiAltLinkler:
        # İKİNCİ LİNK İŞLEMLERİ
        # içerik alınması için parsehtml komutu çalıştırılır ve sitedeki tüm textler get_text ile döndürülür.
        ikinciLinkIcerikAl = genelFonksiyonlar.parseHTML(ikinciLink)
        # içerik alınıp tüm harfler küçük harfe çevrilir.
        ikinciLinkIcerik = ikinciLinkIcerikAl.lower().split()

        # alınan içerik gereksiz sembollerden temizlenir.
        ikinciSayfaKelimeleri = genelFonksiyonlar.sembolTemizle(ikinciLinkIcerik)

        # temizlenmis cikarilacak kelimeler alinir
        cikarilacak_kelimeler = genelFonksiyonlar.csvOku()

        # sayfadaki kelimelerden çıkarılacak kelimeler çıkarılır.
        dizidenKelimeleriCikart = lambda list1, list2: list(filter(lambda element: element not in list2, list1))

        # sözlük oluşturulur
        ikinciSayfaTumSozluk = genelFonksiyonlar.sozlukOlustur(
            dizidenKelimeleriCikart(ikinciSayfaKelimeleri, cikarilacak_kelimeler))

        # LİNKLERİ KARSİLASTİRMA İSLEMLERİ
        ikiDiziyiKarsilastir = lambda list1, list2: list(filter(lambda element: element in list2, list1))
        ayniKelimeler = ikiDiziyiKarsilastir(birinciSayfaTumSozluk, ikinciSayfaTumSozluk)

        # ayni kelimelerden sozluk olustur
        ayniKelimelerSozluk = genelFonksiyonlar.sozlukOlustur(ayniKelimeler)

        karsilastirmaSonucu = genelFonksiyonlar.ikiLinkiKarsilastirSkorHesapla(birinciSayfaTumSozluk,ikinciSayfaTumSozluk,ayniKelimelerSozluk)

        x = {
            "birinciLink": birinciLink,
            "ikinciLink": ikinciLink,
            "birinciSayfaKelimeSayisi": len(birinciSayfaTumSozluk),
            "ikinciSayfaKelimeSayisi": len(ikinciSayfaTumSozluk),
            "ortakKelimeSayisi": len(ayniKelimelerSozluk),
            "karsilastirmaSonucu": karsilastirmaSonucu,
        }

        veriler.append(x)

    return sorted(veriler, key=lambda x: x['karsilastirmaSonucu'],reverse=True),urlKumesiAltLinkler

