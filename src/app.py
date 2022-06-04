from flask import Flask
from flask_restx import Api

from src.resource.list_planets import GetById, GetByName, GetAll
from src.resource.manege_planets import ManegePlanets
from src.resource.payloads.list_planets import list_planets_ns
from src.resource.payloads.manege_planets import manege_planets_ns

# configs
app = Flask(__name__)
api = Api(app)

# namespaces
api.add_namespace(manege_planets_ns)
api.add_namespace(list_planets_ns)

# routes
list_planets_ns.add_resource(GetById, '/<int:_id>')
list_planets_ns.add_resource(GetByName, '/<name>')
list_planets_ns.add_resource(GetAll, '')
manege_planets_ns.add_resource(ManegePlanets, '')
