from flask import Flask, render_template, request, redirect, url_for
import Asama1 as asama1functions
import Asama2 as asama2functions
import Asama3 as asama3functions
import Asama4 as asama4functions
import Asama5 as asama5functions
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

####ASAMA 1 : FREKANS HESAPLAMA###
@app.route("/asama1", methods=["POST", "GET"])
def asama1():
    if request.method == "POST":
        linkDegeri = request.form["linkDegeri"]
        if request.form["button"] == "Gonder":
            return redirect(url_for("islem1", linkDegeri=linkDegeri))
    return render_template("asama1.html")

@app.route("/islem1", methods=["GET","POST"])
def islem1():
    if request.method == 'POST':
        linkDegeri = request.form.get('linkDegeri')
        kelimeler = asama1functions.Asama1Islemleri(linkDegeri)
        return render_template("islem1.html", linkDegeri=linkDegeri,kelimeler=kelimeler)
    else:
        return render_template("islem1.html", linkDegeri="hata olustu")

#### ASAMA2: ANAHTAR KELİME BULMA
@app.route("/asama2", methods=["POST", "GET"])
def asama2():
    if request.method == "POST":
        linkDegeri = request.form["linkDegeri"]
        if request.form["button"] == "Gonder":
            return redirect(url_for("islem2", linkDegeri=linkDegeri))
    return render_template("asama2.html")

@app.route("/islem2", methods=["POST", "GET"])
def islem2():
    if request.method == 'POST':
        linkDegeri = request.form.get('linkDegeri')
        kelimeler = asama2functions.Asama2Islemleri(linkDegeri)
        return render_template("islem2.html", linkDegeri=linkDegeri,kelimeler=kelimeler)
    else:
        return render_template("islem2.html", linkDegeri="hata olustu")

#### ASAMA3: İKİ URL ARASINDAKİ BENZERLİK SKORLAMASI
@app.route("/asama3", methods=["POST", "GET"])
def asama3():
    if request.method == "POST":
        birinciLink = request.form["birinciLink"]
        ikinciLink = request.form["ikinciLink"]
        if request.form["button"] == "Gonder":
            return redirect(url_for("islem3", birinciLink=birinciLink,ikinciLink=ikinciLink))
    return render_template("asama3.html")

@app.route("/islem3", methods=["POST", "GET"])
def islem3():
    if request.method == 'POST':
        birinciLink = request.form.get('birinciLink')
        ikinciLink = request.form.get('ikinciLink')
        birinciLinkKelimeler, ikinciLinkKelimeler , ayniKelimeler , karsilastirmaSonucu= asama3functions.Asama3Islemleri(birinciLink,ikinciLink)
        return render_template("islem3.html", birinciLink=birinciLink,ikinciLink=ikinciLink,birinciLinkKelimeler=birinciLinkKelimeler,ikinciLinkKelimeler=ikinciLinkKelimeler,ayniKelimeler=ayniKelimeler,karsilastirmaSonucu=karsilastirmaSonucu)
    else:
        return render_template("islem3.html", birinciLink="hata olustu",ikinciLink="hata olustu")

##### ASAMA 4 : SİTE INDEXLEME VE SIRALAMA
@app.route("/asama4", methods=["POST", "GET"])
def asama4():
    if request.method == "POST":
        anaLink = request.form["anaLink"]
        urlKumesi = request.form["urlKumesi"]
        if request.form["button"] == "Gonder":
            return redirect(url_for("islem4", anaLink=anaLink,urlKumesi = urlKumesi))
    return render_template("asama4.html")

@app.route("/islem4", methods=["POST", "GET"])
def islem4():
    if request.method == 'POST':
        anaLink = request.form.get('anaLink')
        urlKumesi = request.form.get('urlKumesi')
        tumSonuclar , urlKumesiAltLinkler = asama4functions.Asama4Islemleri(anaLink,urlKumesi)
        return render_template("islem4.html", anaLink=anaLink, urlKumesi = urlKumesi , tumSonuclar = tumSonuclar , urlKumesiAltLinkler = urlKumesiAltLinkler)
    else:
        return render_template("islem4.html", anaLink="hata olustu")


##### ASAMA 5 : SEMANTİK ANALİZ
@app.route("/asama5", methods=["POST", "GET"])
def asama5():
    if request.method == "POST":
        anaLink = request.form["anaLink"]
        urlKumesi = request.form["urlKumesi"]
        if request.form["button"] == "Gonder":
            return redirect(url_for("islem5", anaLink=anaLink,urlKumesi = urlKumesi))
    return render_template("asama5.html")

@app.route("/islem5", methods=["POST", "GET"])
def islem5():
    if request.method == 'POST':
        anaLink = request.form.get('anaLink')
        urlKumesi = request.form.get('urlKumesi')
        tumSonuclar,urlKumesiAltLinkler = asama5functions.Asama5Islemleri(anaLink,urlKumesi)
        print(tumSonuclar)
        return render_template("islem5.html",tumSonuclar=tumSonuclar,anaLink=anaLink,urlKumesi=urlKumesi,urlKumesiAltLinkler=urlKumesiAltLinkler)
    else:
        return render_template("islem5.html", anaLink="hata olustu")


if __name__ == '__main__':
    app.run(port=5555,debug=True)

