
from datetime import date
from flask import redirect, render_template, request, url_for
from registro_ig import app
from registro_ig.models import insert, select_all

@app.route("/")
def index():
    registros = select_all()
    return render_template("index.html", pageTitle = 'Todos', data=registros)

@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "GET":
        
        return render_template('new.html', pageTitle = "Alta_Nuevo", dataForm = "")
    else:
        errores = validarFormulario(request.form)

        if errores == []:
            insert([request.form['date'],
                    request.form['concept'],
                    request.form['quantity']
                    ])
            
            
            return redirect(url_for('index'))
        else:
            return render_template('new.html', pageTitle='Alta_nuevo', msgError = errores, dataForm = dict(request.form))
    

def validarFormulario(camposFormularios):
    errores = []

    hoy = date.today().isoformat()
    if camposFormularios['date'] > hoy:
        errores.append('Introduce fecha que no sea futuro')
    if camposFormularios['concept'] == "":
        errores.append("Introduce un concepto")
    if camposFormularios['quantity'] == "" or camposFormularios == 0:
        errores.append('No se puede introducir un valor igual a 0 o sin valor')
    return errores