#from operator import length_hint
#from sqlalchemy.orm import backref
from app.db import db, BaseModelMixin

class Usuario(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    password = db.Column(db.String)
    status = db.Column(db.String)

    def __init__(self, nombre, password, status):
        self.nombre = nombre
        self.password = password
        self.status = status

    def __repr__(self):
        return f'Usuario({self.nombre})'
    def __str__(self):
        return f'{self.nombre}'

class Task(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    date_creation = db.Column(db.DateTime)
    status = db.Column(db.String)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __init__(self, title, description, date_creation, status, usuario_id):
        self.title = title
        self.description = description
        self.date_creation = date_creation
        self.status = status
        self.usuario_id = usuario_id
    
    def __repr__(self):
        return f'Task({self.title})'
    def __str__(self):
        return f'{self.title}'    

class Execution_logs(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    duracion = db.Column(db.DateTime)
    status = db.Column(db.String)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __init__(self, duracion, status, task_id, usuario_id):
        self.duracion = duracion
        self.status = status
        self.task_id = task_id
        self.usuario_id = usuario_id
    
    def __repr__(self):
        return f'Execution_logs({self.status})'
    def __str__(self):
        return f'{self.status}'
