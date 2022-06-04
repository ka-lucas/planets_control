from flask_restx import Resource

from src.core.list_planets import *


class GetAll(Resource):
    def get(self):
        get_all_core = GetAllCore()
        result = get_all_core.search()
        return result


class GetByName(Resource):
    def get(self,name):
        get_by_name_core = GetByNameCore()
        result = get_by_name_core.search(name)
        return result


class GetById(Resource):
    def get(self,_id):
        get_by_id_core = GetByIdCore()
        result = get_by_id_core.search(_id)
        return result
