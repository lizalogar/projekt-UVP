import bottle
import os
from datetime import date
from model import Igra

igra_pokanje_balonckov = Igra()

@bottle.get("/")
def osnovna_stran():
    global igra_pokanje_balonckov
    igra_pokanje_balonckov = Igra()
    return bottle.template("osnovni_zaslon.html")


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
    print(igra_pokanje_balonckov.konec_igre())

    try:
        
        vrstica = int(bottle.request.forms.get("vrstica")) - 1
        stevilka = int(bottle.request.forms.get("baloni"))

        igra_pokanje_balonckov.igraj_spletni_vmesnik(vrstica, stevilka)
        if igra_pokanje_balonckov.konec_igre() == 1:
            bottle.redirect("/koncna_stran_poraz/")
        elif igra_pokanje_balonckov.konec_igre() == 2:
            bottle.redirect("/koncna_stran_zmaga/")
        else:
            bottle.redirect("/igra/")

    except (IndexError, ValueError):
        return bottle.template("igra.html", stanje = igra_pokanje_balonckov.baloni, napaka="Neveljavna poteza! Poskusi ponovno.")    

@bottle.get("/koncna_stran_poraz/")
def poraz_get():
    global igra_pokanje_balonckov
    igra_pokanje_balonckov = Igra() 
    return bottle.template("koncna_stran_poraz.html")

@bottle.get("/koncna_stran_zmaga/")
def zmaga_get():
    global igra_pokanje_balonckov
    igra_pokanje_balonckov = Igra()
    return bottle.template("koncna_stran_zmaga.html")

@bottle.route('/static/<filename:path>')
def send_static(filename):
    return bottle.static_file(filename, root='static')

@bottle.error(404)
def error_404(error):
    return "Ta stran ne obstaja!"


bottle.run(reloader=True, debug=True)