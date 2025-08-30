"""
El ORM sirve para mapear objetos a una base de datos
y abstraer el lenguaje del CRUD de la base de datos
No me salva de hacer triggers en la base de datos

documentacion en docs.pewee-orm.com/en/lastest/

primero instalar pewee: pip install pewee
pewee va a ir en la parte de modelo
ponemos el import: from pewee import *
ya no necesito crear la base, ni la conexión
le tengo que indicar con qué base de datos voy a trabajar
Ejemplo:
    database=SqliteDatabase("mi_base.db")
utilizamos la clase BaseModel y declaramos con que base trabajamos
creo una clase para usar como tabla
creo la conexión y la tabla

"""
from peewee import *

#le indico que trabajo con sqlite3 y con la base mi_base.db
db=SqliteDatabase("mi_base.db") 

#declaro base
class BaseModel(Model):
    class Meta:
        database=db

#declaro tabla
class Noticia(BaseModel):
    titulo = CharField(unique=True) # es clave
    descripcion = CharField()

db.connect()
db.create_tables([Noticia])