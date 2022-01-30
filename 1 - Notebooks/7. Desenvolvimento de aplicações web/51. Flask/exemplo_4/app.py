# Importação da classe responsável pelo gerenciamento de rotas
# Importamos a função render_template, para criar e retornar a página
from flask import Flask, render_template, request

# Criação do objeto app, instanciando a classe e passando o nome do módulo
app = Flask(__name__)

# Criação da rota
# Podemos explicitar quais métodos serão tratados por esta view
@app.route('/', methods=['GET', 'POST'])
@app.route('/<nome>')
def index(nome=None):
    if request.method == "POST":
        nome = request.POST['nome']
    elif request.args.get('nome'):
        nome = request.args.get('nome')
    elif nome:
        nome = nome
    else:
        nome = 'mundo'

    return render_template('index.html', nome=nome)

# Bloco principal de código (executado apenas quando o arquivo é chamado)
if __name__ == '__main__':
    # inclusão de 2 parâmetros
    app.run(port=5000, debug=True)
