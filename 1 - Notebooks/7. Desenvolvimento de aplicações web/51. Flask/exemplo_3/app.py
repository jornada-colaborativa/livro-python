# Importação da classe responsável pelo gerenciamento de rotas
# Importamos a função render_template, para criar e retornar a página
from flask import Flask, render_template

# Criação do objeto app, instanciando a classe e passando o nome do módulo
app = Flask(__name__)

# Criação da rota
# Podemos explicitar quais métodos serão tratados por esta view
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Bloco principal de código (executado apenas quando o arquivo é chamado)
if __name__ == '__main__':
    # inclusão de 2 parâmetros
    app.run(port=5000, debug=True)
