
from flask import Flask, request, jsonify
from flask_cors import CORS
from commands import process_command

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

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

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
