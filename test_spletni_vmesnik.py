import bottle

@bottle.get('/')
def osnovni_zaslon():
    return bottle.template(
        'osnovni_zaslon.tpl'
    )

@bottle.get('/igra/')
def igra():
    return bottle.template('igra.tpl')

bottle.run(debug=True, reloader=True)
