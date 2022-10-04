from flask_wtf import FlaskForm
from wtforms import DateField, StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length

class MovementForm(FlaskForm):
    date = DateField("Fecha", validators=[DataRequired()]) #para validar las fechas le estamos diciendo datefield es para decirle que ese campo es de tipo fecha
                                                            #entre llaves primero el nombre que va a aparecer en la web y el validador datarequired es que es campo obligatorio
    
    concept = StringField("Concepto", validators = [DataRequired(), Length(min = 4, message="El texto tiene que tener m as de 4 caracteres, por favor")]) #para el formulario los tres conceptos

    quantity = FloatField("Cantidad", validators =[DataRequired()])

    submit = SubmitField("Aceptar")