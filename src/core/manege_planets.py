from src.util.file import insert_data, get_data
import random


class ManegePlanetsCore:
    def add_planets(self, data):
        data['_id'] = random.randint(1, 9999999999)
        all_planets = get_data()
        all_planets.append(data)
        insert_data(all_planets)
        return all_planets

    def remove_planets(self, data):
        all_planets = get_data()
        for index, planet in enumerate(all_planets):
            if data['_id'] == planet['_id']:
                del(all_planets[index])
        insert_data(all_planets)
        return all_planets

