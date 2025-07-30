from flask import Flask, request, jsonify
from flask_cors import CORS
from commands import process_command

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Assistente pessoal rodando com Flask + Gunicorn!"

@app.route('/api/command', methods=['POST'])
def handle_command():
    try:
        data = request.get_json()
        user_input = data.get('command', '')
        if not user_input:
            return jsonify({'error': 'Nenhum comando fornecido'}), 400
        result = process_command(user_input)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoints auxiliares
@app.route('/api/email', methods=['POST'])
def api_email():
    return jsonify({"mensagem": "Requisição de envio de e-mail recebida.", "dados": request.get_json()})

@app.route('/api/reuniao', methods=['POST'])
def api_reuniao():
    return jsonify({"mensagem": "Requisição de criação de reunião recebida.", "dados": request.get_json()})

@app.route('/api/teams', methods=['POST'])
def api_teams():
    return jsonify({"mensagem": "Requisição de mensagem no Teams recebida.", "dados": request.get_json()})

@app.route('/api/nfe', methods=['POST'])
def api_nfe():
    return jsonify({"mensagem": "Requisição de comparação de nota fiscal recebida.", "dados": request.get_json()})

@app.route('/api/planilha', methods=['POST'])
def api_planilha():
    return jsonify({"mensagem": "Requisição de atualização de planilha recebida.", "dados": request.get_json()})

@app.route('/api/powerbi', methods=['POST'])
def api_powerbi():
    return jsonify({"mensagem": "Requisição de geração de relatório Power BI recebida.", "dados": request.get_json()})

@app.route('/api/proteus', methods=['POST'])
def api_proteus():
    return jsonify({"mensagem": "Requisição de criação de PCs no Proteus recebida.", "dados": request.get_json()})

@app.route('/api/ia', methods=['POST'])
def api_ia():
    return jsonify({"mensagem": "Requisição de consulta à IA recebida.", "dados": request.get_json()})

@app.route('/api/pesquisa', methods=['POST'])
def api_pesquisa():
    return jsonify({"mensagem": "Requisição de pesquisa recebida.", "dados": request.get_json()})

@app.route('/api/fornecedores', methods=['POST'])
def api_fornecedores():
    return jsonify({"mensagem": "Requisição de busca de fornecedores recebida.", "dados": request.get_json()})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
