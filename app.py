from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    result = None
    if request.method == 'POST':
        try:
            number1 = float(request.form['number1'])
            number2 = float(request.form['number2'])
            result = number1 + number2
        except ValueError:
            error = "Tots els camps han de contenir números vàlids!"
    
    html = '''
    <!DOCTYPE html>
    <html lang="ca">
    <head>
        <meta charset="UTF-8">
        <title>Calculadora de Suma</title>
    </head>
    <body>
        <h1>Calculadora de Suma</h1>
        <form method="post">
            <label for="number1">Primer número:</label>
            <input type="text" id="number1" name="number1"><br><br>
            <label for="number2">Segon número:</label>
            <input type="text" id="number2" name="number2"><br><br>
            <button type="submit">Calcular Suma</button><br><br>
            <label for="result">Resultat:</label>
            <input type="text" id="result" name="result" value="{{ result }}" readonly><br><br>
            {% if error %}
                <p style="color: red;">{{ error }}</p>
            {% endif %}
        </form>
    </body>
    </html>
    '''
    return render_template_string(html, error=error, result=result)

if __name__ == '__main__':
    app.run(debug=True)