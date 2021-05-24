from flask_restful import Resource


list_habilitys = ["python", "java", "flask", "php"]


class Habilitys(Resource):
    def get(self):
        return list_habilitys
    
    def post(self):
        pass
    
class Hability(Resource):
    def put(self, id):
        pass
    
    def delete(self, id):
        pass