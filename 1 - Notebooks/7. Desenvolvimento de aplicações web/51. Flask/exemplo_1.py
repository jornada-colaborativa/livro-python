# Importação da classe responsável pelo gerenciamento de rotas
from flask import Flask

# Criação do objeto app, instanciando a classe e passando o nome do módulo
app = Flask(__name__)

# Criação da rota
@app.route('/')
def index():
    return '<h1>Olá Mundo!!!</h1>'

# Bloco principal de código (executado apenas quando o arquivo é chamado)
if __name__ == '__main__':
    app.run()
