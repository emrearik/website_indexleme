import GenelFonksiyonlar as genelFonksiyonlar

def Asama3Islemleri(birinciLink,ikinciLink):

    ##BİRİNCİ LİNK İŞLEMLERİ
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
    birinciSayfaTumSozluk = genelFonksiyonlar.sozlukOlustur(dizidenKelimeleriCikart(birinciSayfaKelimeleri, cikarilacak_kelimeler))


    #İKİNCİ LİNK İŞLEMLERİ
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

    #LİNKLERİ KARSİLASTİRMA İSLEMLERİ
    ikiDiziyiKarsilastir = lambda list1, list2: list(filter(lambda element: element in list2, list1))
    ayniKelimeler = ikiDiziyiKarsilastir(birinciSayfaTumSozluk,ikinciSayfaTumSozluk)

    #ayni kelimelerden sozluk olustur
    ayniKelimelerSozluk = genelFonksiyonlar.sozlukOlustur(ayniKelimeler)

    #iki sayfa karşılaştırılır ve skor hesaplanır.
    karsilastirmaSonucu = genelFonksiyonlar.ikiLinkiKarsilastirSkorHesapla(birinciSayfaTumSozluk,ikinciSayfaTumSozluk,ayniKelimelerSozluk)

    return genelFonksiyonlar.sozluguSirala(birinciSayfaTumSozluk),genelFonksiyonlar.sozluguSirala(ikinciSayfaTumSozluk),genelFonksiyonlar.sozluguSirala(ayniKelimelerSozluk),karsilastirmaSonucu
