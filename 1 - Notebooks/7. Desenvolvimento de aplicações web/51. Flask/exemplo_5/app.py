# Importamos a função render_template, para criar e retornar a página
from flask import Flask, render_template
import pandas as pd

# Criação de um dataframe a partir de um dicionário
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

# Geração de código html contendo o dataframe
table = df.to_html()

# Criação do objeto app, instanciando a classe e passando o nome do módulo
app = Flask(__name__)

# Criação da rota
@app.route('/')
def index():
    # Renderiza o template passando a tabela em html
    return render_template('index.html', table=table)

# Bloco principal de código (executado apenas quando o arquivo é chamado)
if __name__ == '__main__':
    app.run(port=5000, debug=True)
