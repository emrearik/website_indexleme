import GenelFonksiyonlar as genelFonksiyonlar
import requests
import json


def Asama5Islemleri(birinciLink, urlKumesi):
    veriler = []

    ##ANA LİNK İŞLEMLERİ
    # 1.içerik alınması için parsehtml komutu çalıştırılır ve sitedeki tüm textler get_text ile döndürülür.
    birinciLinkIcerikAl = genelFonksiyonlar.parseHTML(birinciLink)
    # 2.içerik alınıp tüm harfler küçük harfe çevrilir.
    birinciLinkIcerik = birinciLinkIcerikAl.lower().split()
    # 3.alınan içerik gereksiz sembollerden temizlenir.
    birinciSayfaKelimeleri = genelFonksiyonlar.sembolTemizle(birinciLinkIcerik)
    # 4.temizlenmis cikarilacak kelimeler alinir
    cikarilacak_kelimeler = genelFonksiyonlar.csvOku()
    # 5.sayfadaki kelimelerden çıkarılacak kelimeler çıkarılır.
    dizidenKelimeleriCikart = lambda list1, list2: list(filter(lambda element: element not in list2, list1))
    # 6.sözlük oluşturulur
    birinciSayfaTumSozluk = genelFonksiyonlar.sozlukOlustur(
        dizidenKelimeleriCikart(birinciSayfaKelimeleri, cikarilacak_kelimeler))

    # İKİNCİ LİNK İŞLEMLERİ
    urlKumesiListe = urlKumesi.split("\r\n")

    for urlKumesiLink in urlKumesiListe:
        urlKumesiAltLinkler = genelFonksiyonlar.getLinks(urlKumesiLink)

    for ikinciLink in urlKumesiAltLinkler:
        # 1.içerik alınması için parsehtml komutu çalıştırılır ve sitedeki tüm textler get_text ile döndürülür.
        ikinciLinkIcerikAl = genelFonksiyonlar.parseHTML(ikinciLink)
        # 2.içerik alınıp tüm harfler küçük harfe çevrilir.
        ikinciLinkIcerik = ikinciLinkIcerikAl.lower().split()
        # 3.alınan içerik gereksiz sembollerden temizlenir.
        ikinciSayfaKelimeleri = genelFonksiyonlar.sembolTemizle(ikinciLinkIcerik)
        # 4.temizlenmis cikarilacak kelimeler alinir
        cikarilacak_kelimeler = genelFonksiyonlar.csvOku()
        # 5.sözlük oluşturulur
        ikinciSayfaTumSozluk = genelFonksiyonlar.sozlukOlustur(
            dizidenKelimeleriCikart(ikinciSayfaKelimeleri, cikarilacak_kelimeler))

        # LİNKLERİ KARSİLASTİRMA İSLEMLERİ
        ikiDiziyiKarsilastir = lambda list1, list2: list(filter(lambda element: element in list2, list1))
        ayniKelimeler = ikiDiziyiKarsilastir(birinciSayfaTumSozluk, ikinciSayfaTumSozluk)

        # ayni kelimelerden sozluk olustur
        ayniKelimelerSozluk = genelFonksiyonlar.sozlukOlustur(ayniKelimeler)

        # karşılaştırma sonucu alınır ve return edilir.
        karsilastirmaSonucu = genelFonksiyonlar.ikiLinkiKarsilastirSkorHesapla(birinciSayfaTumSozluk,
                                                                               ikinciSayfaTumSozluk,
                                                                               ayniKelimelerSozluk)

        # ANAHTAR KELİMELERİN YAKIN ANLAMLARININ BULUNMASI
        # sayfadaki tüm kelimelerden anahtar kelimeler alınır.
        anahtarKelimelerTumSozluk = genelFonksiyonlar.tumSozluktenAnahtarKelimeleriAl(
            genelFonksiyonlar.sozluguSirala(ikinciSayfaTumSozluk))

        apiVerileri = genelFonksiyonlar.apiyiAl(anahtarKelimelerTumSozluk)

        x = {
            "birinciLink": birinciLink,
            "ikinciLink": ikinciLink,
            "birinciSayfaKelimeSayisi": len(birinciSayfaTumSozluk),
            "ikinciSayfaKelimeSayisi": len(ikinciSayfaTumSozluk),
            "ortakKelimeSayisi": len(ayniKelimelerSozluk),
            "karsilastirmaSonucu": karsilastirmaSonucu,
            "anahtarKelimeler": apiVerileri
        }
        veriler.append(x)

    return sorted(veriler, key=lambda x: x['karsilastirmaSonucu'],reverse=True), urlKumesiAltLinkler

