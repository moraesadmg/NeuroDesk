from flask import Flask, request, jsonify
from agentes.comparar_nf import comparar_nf_com_pedido
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/executar', methods=['POST'])
def executar():
    dados = request.json
    acao = dados.get("ação")
    parametros = dados.get("parametros", {})
    comando_original = dados.get("comando_original")

    if acao == "comparar_nf_pedido":
        nf_path = os.path.join(UPLOAD_FOLDER, parametros["nota_fiscal"])
        pedido_path = os.path.join(UPLOAD_FOLDER, parametros["pedido"])
        relatorio = comparar_nf_com_pedido(nf_path, pedido_path)
        return jsonify(relatorio)

    return jsonify({"erro": "Ação não reconhecida", "comando": comando_original})

if __name__ == '__main__':
    import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

