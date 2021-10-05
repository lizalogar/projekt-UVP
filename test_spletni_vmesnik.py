import bottle
import os
from datetime import date
from model import Igra

igra_pokanje_balonckov = Igra()

def nalozi_uporabnikovo_stanje():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime")
    if uporabnisko_ime:
        return Stanje.preberi_iz_datoteke(uporabnisko_ime)
    else:
        bottle.redirect("/prijava/")


def shrani_uporabnikovo_stanje(stanje):
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime")
    stanje.shrani_v_datoteko(uporabnisko_ime)


@bottle.get("/")
def osnovna_stran():
    global igra_pokanje_balonckov
    igra_pokanje_balonckov = Igra()
    return bottle.template("osnovni_zaslon.html")


@bottle.get("/registracija/")
def registracija_get():
    return bottle.template("registracija.html", napake={}, polja={}, uporabnisko_ime=None)


@bottle.post("/registracija/")
def registracija_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    if os.path.exists(uporabnisko_ime):
        napake = {"uporabnisko_ime": "Uporabniško ime že obstaja."}
        return bottle.template("registracija.html", napake=napake, polja={"uporabnisko_ime": uporabnisko_ime}, uporabnisko_ime=None)
    else:
        bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/")
        Stanje().shrani_v_datoteko(uporabnisko_ime)
        bottle.redirect("/")

@bottle.get("/prijava/")
def prijava_get():
    return bottle.template("prijava.html", napake={}, polja={}, uporabnisko_ime=None)


@bottle.post("/prijava/")
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    if not os.path.exists(uporabnisko_ime):
        napake = {"uporabnisko_ime": "Uporabniško ime ne obstaja."}
        return bottle.template("prijava.html", napake=napake, polja={"uporabnisko_ime": uporabnisko_ime}, uporabnisko_ime=None)
    else:
        bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/")
        bottle.redirect("/")


@bottle.post("/odjava/")
def odjava_post():
    bottle.response.delete_cookie("uporabnisko_ime", path="/")
    print("piškotek uspešno pobrisan")
    bottle.redirect("/")



@bottle.get('/igra/')
def igra_get():
    return bottle.template('igra.html', 
    stanje = igra_pokanje_balonckov.baloni, 
    st_balonov_v_vrstici = igra_pokanje_balonckov.st_balonov_v_vrstici, 
    kdo_je_na_vrsti = igra_pokanje_balonckov.kdo_je_na_vrsti,
    racunalnik = igra_pokanje_balonckov.racunalnik,
    igralec = igra_pokanje_balonckov.igralec,
    napaka=None
    )

@bottle.post("/igra/")
def igra_post():
    vrstica = int(bottle.request.forms.get("vrstica")) - 1
    stevilka = int(bottle.request.forms.get("baloni"))
    try:
        igra_pokanje_balonckov.igraj_spletni_vmesnik(vrstica, stevilka)
        bottle.redirect("/igra/")
    except IndexError as e:
        return bottle.template("igra.html", stanje = igra_pokanje_balonckov.baloni, napaka="neveljavna poteza")    

@bottle.error(404)
def error_404(error):
    return "Ta stran ne obstaja!"


bottle.run(reloader=True, debug=True)