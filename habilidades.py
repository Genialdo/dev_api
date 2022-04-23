from flask_restful import Resource

habilidades = ['Python', 'Java', 'CSS', 'C++', 'C#', 'Flask', 'PHP']

class Habilidades(Resource):
    def get(self):
        return habilidades
        

