from flask import Flask, render_template, abort
from lxml import etree
app = Flask (__name__)

@app.route('/')
def inicio():
    return render_template("principal.html")


@app.route('/potencia/<base>/<exponente>')
def potencia(base, exponente):

    if int(exponente) > 0:
        resultado = int(base)**int(exponente)
    elif int(exponente) == 0:
        resultado = 1
    elif int(exponente) < 0:
        resultado = 1/(int(base)**int(exponente))
    else:
        return abort(404)
    
    return render_template('potencia.html', resultado=resultado, base=base, exponente=exponente)

@app.route('/cuentaletras/<palabra>/<letra>')
def cuentaletras(palabra,letra):
        if len(letra) == 1:
            aparece = palabra.count(letra)
        else:
            abort(404)
        return render_template('cuentaletras.html',palabra=palabra, letra=letra, apariciones=aparece)

app.run(debug=True)