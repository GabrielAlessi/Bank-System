from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/predizer_fraude', methods=['POST'])
def predizer_fraude():
    dados = request.json
    transacao = np.array(dados['transacao'])
    resultado = model.predict(transacao)
    return jsonify({'fraude': bool(resultado > 0.5)})

if __name__ == '__main__':
    app.run(debug=True)
