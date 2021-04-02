import GenelFonksiyonlar as genelFonksiyonlar


def Asama2Islemleri(urlDegeri):
    # içerik alınması için parsehtml komutu çalıştırılır ve sitedeki tüm textler get_text ile döndürülür.
    icerikAl = genelFonksiyonlar.parseHTML(urlDegeri)
    # içerik alınıp tüm harfler küçük harfe çevrilir.
    icerik = icerikAl.lower().split()

    # alınan içerik gereksiz sembollerden temizlenir.
    sayfaKelimeleri = genelFonksiyonlar.sembolTemizle(icerik)

    #temizlenmis cikarilacak kelimeler alinir
    cikarilacak_kelimeler = genelFonksiyonlar.csvOku()

    #sayfadaki kelimelerden çıkarılacak kelimeler çıkarılır.
    dizidenKelimeleriCikart = lambda list1, list2: list(filter(lambda element: element not in list2, list1))

    #sözlük oluşturulur
    tumSozluk = genelFonksiyonlar.sozlukOlustur(dizidenKelimeleriCikart(sayfaKelimeleri,cikarilacak_kelimeler))

    return genelFonksiyonlar.sozluguSirala(tumSozluk)


if __name__ == '__main__':
    Asama2Islemleri("https://www.tutorialspoint.com/python3/python_overview.htm/")