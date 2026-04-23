from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Gerador de Orçamento</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial; max-width: 600px; margin: 20px auto; padding: 20px; }
        input, textarea { width: 100%; padding: 10px; margin: 8px 0; box-sizing: border-box; }
        button { background: #25D366; color: white; padding: 12px; border: none; width: 100%; font-size: 16px; cursor: pointer; }
        .orcamento { border: 1px solid #ccc; padding: 20px; margin-top: 20px; }
        .footer { text-align: center; margin-top: 30px; color: #666; }
    </style>
</head>
<body>
    <h2>Gerador de Orçamento</h2>
    <form method="POST">
        <input type="text" name="cliente" placeholder="Nome do Cliente" required>
        <textarea name="servico" placeholder="Descrição do Serviço" required></textarea>
        <input type="number" name="valor" placeholder="Valor em Kz" required>
        <button type="submit">Gerar Orçamento</button>
    </form>
    
    {% if orcamento %}
    <div class="orcamento">
        <h3>Orçamento para {{ orcamento.cliente }}</h3>
        <p><strong>Serviço:</strong> {{ orcamento.servico }}</p>
        <p><strong>Valor:</strong> {{ orcamento.valor }} Kz</p>
    </div>
    {% endif %}
    
    <div class="footer">
        HENERÁRIO<br>
        Desenvolvedor - Lunda-Sul, Angola<br>
        WhatsApp: +244 973574928
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    orcamento = None
    if request.method == "POST":
        orcamento = {
            "cliente": request.form["cliente"],
            "servico": request.form["servico"],
            "valor": request.form["valor"]
        }
    return render_template_string(HTML, orcamento=orcamento)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)