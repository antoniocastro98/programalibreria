from flask import Flask, render_template, abort
from lxml import etree
app = Flask (__name__)

@app.route('/')
def inicio():
    return render_template("principal.html")


@app.route('/potencia/<int:base>/<int:exponente>')
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

@app.route('/libros/<int:codigo>')
def buscar(codigo):
    doc = etree.parse('libros.xml')
    if str(codigo) in doc.xpath("/biblioteca/libro/codigo/text()"):
        titulo=doc.xpath("/biblioteca/libro[codigo/text()='%s']/titulo/text()"%codigo)[0]
        autor=doc.xpath("/biblioteca/libro[codigo/text()='%s']/autor/text()"%codigo)[0]
    else:
        abort(404)
    return render_template("libros.html",titulo=titulo,autor=autor)

app.run(debug=True)