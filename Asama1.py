import GenelFonksiyonlar as genelFonksiyonlar

#verilen urldeki html içeriği get_text() sayesinde tüm textler alınır. sonrasında semboller temizlenir.
def Asama1Islemleri(urlDegeri):
   #içerik alınması için parsehtml komutu çalıştırılır ve sitedeki tüm textler get_text ile döndürülür.
   icerikAl = genelFonksiyonlar.parseHTML(urlDegeri)
   #içerik alınıp tüm harfler küçük harfe çevrilir.
   icerik = icerikAl.lower().split()

   #alınan içerik gereksiz sembollerden temizlenir.
   tumKelimeler = genelFonksiyonlar.sembolTemizle(icerik)
   #temizlenen içerik sözlük oluşturulması için fonksiyona gönderilir.
   tumSozluk = genelFonksiyonlar.sozlukOlustur(tumKelimeler)


   return genelFonksiyonlar.sozluguSirala(tumSozluk)


