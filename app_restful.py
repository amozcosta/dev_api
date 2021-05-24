from flask import Flask, request
from flask_restful import Resource, Api
import json

from habilitys import Habilitys

app = Flask(__name__)
api = Api(app)

developers = [
    {
        'id': '0',
        'nome': 'Jose da fonseca',
        'habilidades': ['python', 'flask']
    },
    {
        'id': '1',
        'nome': 'Pedro da Silva',
        'habilidades': ['python', 'django']
    }
]


class Developer(Resource):
    def get(self, id):
        try:
            response = developers[id]
        
        except IndexError:
            msg = f'Desenvolvedor de ID {id} nao existe.'
            response = {'status': 'error', 'mensagem': msg}
            
        except Exception:
            msg = f'Erro desconhecido. Procure o administrada da API'
            response = {'status': 'erro', 'mensagem': msg}
        return response
    
    def put(self, id):
        data = json.loads(request.data)
        developers[id] = data
        return data
    
    def delete(self, id):
        developers.pop(id)
        return {'status': 'sucesso', 'mensagem': 'registro excluido.'}


class Developers(Resource):
    def get(self):
        return developers
    
    def post(self):
        data = json.loads(request.data)
        posicao = len(developers)
        data['id'] = posicao
        developers.append(data)
        return developers[posicao]
    

api.add_resource(Developer, '/dev/<int:id>')
api.add_resource(Developers, '/dev/')
api.add_resource(Habilitys, '/habilitys/')


if __name__ == '__main__':
    app.run(debug=True)