from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Gerador de Orçamento Rápido</title>
    <style>
        body { font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px; }
        input, textarea { width: 100%; padding: 10px; margin: 10px 0; }
        button { background: #007bff; color: white; padding: 15px; border: none; width: 100%; font-size: 18px; }
        .resultado { background: #f0f0f0; padding: 20px; margin-top: 20px; white-space: pre-wrap; }
    </style>
</head>
<body>
    <h1>Gerador de Orçamento Rápido</h1>
    <form method="POST">
        <input name="cliente" placeholder="Nome do Cliente" required>
        <input name="servico" placeholder="Serviço" required>
        <input name="valor" type="number" placeholder="Valor em Kz" required>
        <textarea name="detalhes" placeholder="Detalhes do serviço"></textarea>
        <button type="submit">GERAR ORÇAMENTO</button>
    </form>
    {% if orcamento %}
    <div class="resultado">{{ orcamento }}</div>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    orcamento = None
    if request.method == 'POST':
        cliente = request.form['cliente']
        servico = request.form['servico']
        valor = request.form['valor']
        detalhes = request.form['detalhes']
        orcamento = f'''
ORÇAMENTO - {cliente}

Serviço: {servico}
Detalhes: {detalhes}

VALOR TOTAL: {valor} Kz

Validade: 15 dias
Pagamento: 50% entrada, 50% entrega

HENERÁRIO
Desenvolvedor
WhatsApp: +244 973574928
'''
    return render_template_string(HTML, orcamento=orcamento)

if __name__ == '__main__':
app.run(host='0.0.0.0', port=10000)