from flask_restx import Namespace, fields

# Namespaces
manege_planets_ns = Namespace('manege-planets')

# Payload
create_payload = manege_planets_ns.model('CreatePayload', {
    'name': fields.String(required=True),
    'clima': fields.String(required=True),
    'terreno': fields.String(required=True)
}, strict=True)

delete_payload = manege_planets_ns.model('DeletePayload', {
    '_id': fields.Integer(required=True)
}, strict=True)
