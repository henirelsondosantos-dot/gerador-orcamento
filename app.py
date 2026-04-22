from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Gerador de Orçamento</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
        input, textarea { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; }
        button { background: #28a745; color: white; padding: 12px 20px; border: none; border-radius: 4px; cursor: pointer; width: 100%; }
        button:hover { background: #218838; }
        .resultado { background: #f8f9fa; padding: 20px; margin-top: 20px; border-radius: 4px; white-space: pre-wrap; }
        .footer { margin-top: 30px; text-align: center; color: #666; font-size: 14px; }
    </style>
</head>
<body>
    <h2>Gerador de Orçamento Rápido</h2>
    <form method="post">
        <label>Nome do Cliente:</label>
        <input name="cliente" required>
        
        <label>Serviço:</label>
        <input name="servico" required>
        
        <label>Valor (Kz):</label>
        <input name="valor" type="number" step="0.01" required>
        
        <button type="submit">Gerar Orçamento</button>
    </form>
    
    {% if orcamento %}
    <div class="resultado">
        <h3>Orçamento Gerado:</h3>
        {{ orcamento }}
    </div>
    {% endif %}
    
    <div class="footer">
        HENERÁRIO<br>
        Desenvolvedor - Luanda, Angola<br>
        WhatsApp: +244 973574928
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    orcamento = None
    if request.method == "POST":
        cliente = request.form["cliente"]
        servico = request.form["servico"]
        valor = float(request.form["valor"])
        orcamento = f"Cliente: {cliente}\\nServiço: {servico}\\nValor Total: {valor:,.2f} Kz\\n\\nOrçamento válido por 15 dias."
    return render_template_string(HTML, orcamento=orcamento)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)