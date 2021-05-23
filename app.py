from flask import Flask, jsonify, request
import json

app = Flask(__name__)


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


@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    if request.method == 'GET':
        try:
            response = developers[id]
        
        except IndexError:
            msg = f'Desenvolvedor de ID {id} nao existe.'
            response = {'status': 'error', 'mensagem': msg}
            
        except Exception:
            msg = f'Erro desconhecido. Procure o administrada da API'
            response = {'status': 'erro', 'mensagem': msg}
            
        return jsonify(response)
    
    elif request.method == 'PUT':
        data = json.loads(request.data)
        developers[id] = data
        return jsonify(data)
    
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'registro excluido.'})


@app.route('/dev/', methods=['POST', 'GET'])
def develpers():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(developers)
        dados['id'] = posicao
        developers.append(dados)
        return jsonify(developers[posicao])
    
    elif request.method == 'GET':
        return jsonify(developers)
        

if __name__ == '__main__':
    app.run(debug=True)