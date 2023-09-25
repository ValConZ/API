from marshmallow import fields

from app.ext import ma

class UsuarioSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String()
    password = fields.String()
    status = fields.String()

class TaskSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    description = fields.String()
    date_creation = fields.DateTime()
    status = fields.String()
    usuario_id = fields.Integer()

class Execution_logsSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    duracion = fields.DateTime()
    status = fields.String()
    task_id = fields.Integer()
    usuario_id = fields.Integer()
