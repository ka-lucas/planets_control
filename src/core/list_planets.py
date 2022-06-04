from src.util.file import get_data


class GetAllCore:
    def search(self):
        return get_data()


class GetByNameCore:
    def search(self, name):
        all_planets = get_data()
        for planet in all_planets:
            if name == planet['name']:
                return planet

        return f'O planeta {name} nao foi encontrado'


class GetByIdCore:
    def search(self, _id):
        all_planets = get_data()
        for planet in all_planets:
            if _id == planet['_id']:
                return planet

        return f'O planeta {_id} nao foi encontrado'
