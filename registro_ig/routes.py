
from crypt import methods
from datetime import date
from flask import redirect, render_template, request, url_for, flash
from registro_ig import app
from registro_ig.forms import MovementForm
from registro_ig.models import insert, select_all, select_by, delete_by, modifica

@app.route("/")
def index():
    registros = select_all()
    return render_template("index.html", pageTitle = 'Todos', data=registros)

@app.route("/new", methods=["GET", "POST"])
def new():
    form = MovementForm()#creo la instancia de la clase movementform que hemos creado en forms.py
    if request.method == "GET":
        
        return render_template('new.html', pageTitle = "Alta_Nuevo", el_formulario = form)
    else:
        #errores = validarFormulario(request.form)# ya con el form te lo valida los errores tb

        if form.validate():#validate te valida los errores es lo mismo que if not errores
            insert([form.date.data.isoformat(),
                    form.concept.data,
                    form.quantity.data#form.nombrecampo.data para meter el dato del nombre del campo que hemos definido en form.py
                    ])
            
            
            return redirect(url_for('index'))
        else:
            return render_template('new.html', pageTitle='Alta_nuevo', el_formulario = form)

@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    if request.method == "GET":
        registro_eliminar = select_by(id)

        if registro_eliminar:

            return render_template("delete.html", pageTitle = "Borrar", movement = registro_eliminar)
        else:
            flash(f"El registro {id} no existe.")
            return redirect(url_for('index'))
    else:
        delete_by(id)
        flash("Regitro borrado correctamente.")
        return redirect(url_for('index'))

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    form = MovementForm()
    if request.method== "GET":
        nuevo_registro = select_by(id)

        if nuevo_registro:
            return render_template("update.html", pageTitle = "Modificar", el_formulario = form, mod = nuevo_registro)
    else:

        if form.validate():
            modifica([form.date.data.isoformat(),
                    form.concept.data,
                    form.quantity.data,
                    id])
            return redirect(url_for("index"))
        else:
            nuevo_registro = select_by(id)
            return render_template('update.html', pageTitle='Alta_nuevo', el_formulario = form, mod = nuevo_registro)
