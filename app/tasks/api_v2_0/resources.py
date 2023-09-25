from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import TaskSchema, Execution_logsSchema, UsuarioSchema
from ..models import Task, Execution_logs, Usuario

tasks_v2_0_bp = Blueprint('tasks_v2_0_bp', __name__)

task_schema = TaskSchema()
execution_logs_schema = Execution_logsSchema()
usuario_schema = UsuarioSchema()

api = Api(tasks_v2_0_bp)

class UsuarioListResource(Resource):
    def get(self):
        usuarios = Usuario.get_all()
        result = usuario_schema.dump(usuarios, many=True)
        return result
    
    def post(self):
        data = request.get_json()
        usuario_dict = usuario_schema.load(data)
        usuario = Usuario(nombre=usuario_dict['nombre'], password=usuario_dict['password'], status=usuario_dict['status'])
        usuario.save()
        resp = usuario_schema.dump(usuario)
        return resp, 201

class UsuarioResource(Resource):
    def get(self, usuario_id):
        usuario = Usuario.get_by_id(usuario_id)
        if usuario is None:
            raise ObjectNotFound('El usuario no existe')
        resp = usuario_schema.dump(usuario)
        return resp
    
    def put(self, usuario_id):
        usuario = Usuario.get_by_id(usuario_id)
        data = request.get_json()
        usuario_dict = usuario_schema.load(data)
        usuario.nombre = usuario_dict["nombre"]
        usuario.password = usuario_dict["password"]
        usuario.status = usuario_dict["status"]
        usuario.save()
        resp = usuario_schema.dump(usuario)
        return resp, 200

    #def delete(self, usuario_id):
    #    usuario = Usuario.get_by_id(usuario_id)
    #    usuario.delete()
    #    return "", 204
    
    # Borrado Lógico
    def delete(self, usuario_id):
        usuario = Usuario.get_by_id(usuario_id)
        usuario.status = 'I'
        usuario.save()
        resp = usuario_schema.dump(usuario)
        return resp, 200

class TaskListResource(Resource):
    def get(self):
        tasks = Task.get_all()
        result = task_schema.dump(tasks, many=True)
        return result
    
    def post(self):
        data = request.get_json()
        task_dict = task_schema.load(data)
        task = Task(title=task_dict['title'], description=task_dict['description'], date_creation=task_dict['date_creation'], status=task_dict['status'], usuario_id=task_dict['usuario_id'])
        task.save()
        resp = task_schema.dump(task)
        return resp, 201

class TaskResource(Resource):
    def get(self, task_id):
        task = Task.get_by_id(task_id)
        if task is None:
            raise ObjectNotFound('La tarea no existe')
        resp = task_schema.dump(task)
        return resp
    
    def put(self, task_id):
        task = Task.get_by_id(task_id)
        data = request.get_json()
        task_dict = task_schema.load(data)
        task.title = task_dict["title"]
        task.description = task_dict["description"]
        task.date_creation = task_dict["date_creation"]
        task.status = task_dict["status"]
        task.usuario_id = task_dict["usuario_id"]
        task.save()
        resp = task_schema.dump(task)
        return resp, 200

    #def delete(self, task_id):
    #    task = Task.get_by_id(task_id)
    #    task.delete()
    #    return "", 204
    
    # Borrado Lógico
    def delete(self, task_id):
        task = Task.get_by_id(task_id)
        task.status = 'I'
        task.save()
        resp = task_schema.dump(task)
        return resp, 200

class Execution_logsListResource(Resource):
    def get(self):
        execution_logs = Execution_logs.get_all()
        result = execution_logs_schema.dump(execution_logs, many=True)
        return result
    
    def post(self):
        data = request.get_json()
        execution_logs_dict = execution_logs_schema.load(data)
        execution_logs = Execution_logs(duracion=execution_logs_dict['duracion'], status=execution_logs_dict['status'], task_id=execution_logs_dict['task_id'], usuario_id=execution_logs_dict['usuario_id'])
        execution_logs.save()
        resp = execution_logs_schema.dump(execution_logs)
        return resp, 201

class Execution_logsResource(Resource):
    def get(self, execution_logs_id):
        execution_logs = Execution_logs.get_by_id(execution_logs_id)
        if execution_logs is None:
            raise ObjectNotFound('No se encuentra registrado ningun log')
        resp = execution_logs_schema.dump(execution_logs)
        return resp
    
    def put(self, execution_logs_id):
        execution_logs = Execution_logs.get_by_id(execution_logs_id)
        data = request.get_json()
        execution_logs_dict = execution_logs_schema.load(data)
        execution_logs.duracion = execution_logs_dict["duracion"]
        execution_logs.status = execution_logs_dict["status"]
        execution_logs.task_id = execution_logs_dict["task_id"]
        execution_logs.usuario_id = execution_logs_dict["usuario_id"]
        execution_logs.save()
        resp = execution_logs_schema.dump(execution_logs)
        return resp, 200

    #def delete(self, execution_logs_id):
    #    execution_logs = Execution_logs.get_by_id(execution_logs_id)
    #    execution_logs.delete()
    #    return "", 204
    
    # Borrado Lógico
    def delete(self, execution_logs_id):
        execution_logs = Execution_logs.get_by_id(execution_logs_id)
        execution_logs.status = 'I'
        execution_logs.save()
        resp = execution_logs_schema.dump(execution_logs)
        return resp, 200

api.add_resource(UsuarioListResource, '/api/v2.0/usuario/', endpoint='usuario_list_resource')
api.add_resource(UsuarioResource, '/api/v2.0/usuario/<int:usuario_id>', endpoint='usuario_resource')
api.add_resource(TaskListResource, '/api/v2.0/task/', endpoint='task_list_resource')
api.add_resource(TaskResource, '/api/v2.0/task/<int:task_id>', endpoint='task_resource')
api.add_resource(Execution_logsListResource, '/api/v2.0/execution_logs/', endpoint='execution_logs_list_resource')
api.add_resource(Execution_logsResource, '/api/v2.0/execution_logs/<int:execution_logs_id>', endpoint='execution_logs_resource')