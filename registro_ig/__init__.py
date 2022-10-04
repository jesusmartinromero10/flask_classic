from flask import Flask

app = Flask(__name__, instance_relative_config=True)#le estamos diciendo que vamos a configurar relativa tb nosotros es para lo de la clave incriptada

app.config.from_object("config") # es para añadir las claves, entre parentesis hay que poner el nombre del fichero donde esta las claves

from registro_ig.routes import *