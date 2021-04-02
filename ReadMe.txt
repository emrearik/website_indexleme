Projenin çalışması için;
1. İlk olarak masaüstünde bir klasör oluşturun. Örneğin bu klasörün ismi yazlab2.1 olsun
2. Sonrasında cmd yi açıp pip modülünü aşağıdaki komutla upgrade edin.
   -python -m pip install –upgrade pip
3. Masaüstünde oluşturduğunuz klasör içerisine cd yazlab2.1 ismiyle giriş yapın.
4. Virtual environment kurulumu yapmak için aşağıdaki komutları sırasıyla çalıştırınız.
   -pip install virtualenv
   -virtualenv venv
   -virtualenv venv\Scripts\activate
   Bu aşamada virtual environment kurulumu yaptık ve venv ismini verdik. Üçüncü komutta virtual environmenti aktif ettik.
5. Bu aşamada proje dosyalarını yazlab2.1 klasörünün içerisine kopyalayın.
6. Projeyi PyCharm aracılığıyla Open Folder ile açın. App.py dosyasını run ettiğinizde Flask hatası verecektir.
7. Flask kurulumu için aşağıdaki komutu terminale yazın:
   -pip install Flask
8. Yine run ettiğinizde requests-html kütüphanesi isteyecektir. Kurulum için aşağıdaki komutu terminale yazın:
   -pip install requests-html
9. Modüller kurulduktan sonra app.py dosyasını run edin. Debug'da flask size bir link verecektir. Varsayılan olarak bu 
   http://127.0.0.1:5555/ linkidir. Bu linki tarayıcıdan açıp projeyi çalıştırabilirsiniz.