from flask import request
from flask_restx import Resource

from src.core.manege_planets import ManegePlanetsCore
from src.resource.payloads.manege_planets import *

manege_planets_core = ManegePlanetsCore()


class ManegePlanets(Resource):
    @manege_planets_ns.expect(create_payload, validate=True)
    def post(self):
        data = request.get_json()
        result = manege_planets_core.add_planets(data)
        return result

    @manege_planets_ns.expect(delete_payload, validate=True)
    def delete(self):
        data = request.get_json()
        result = manege_planets_core.remove_planets(data)
        return result
