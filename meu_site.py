# Flask FrameWork API
from flask import Flask, render_template

app = Flask(__name__)

# criar a 1 pagina no ar
# toda pagina tem um route e uma função 
# route() rota para o site representada pela função 
# a função representa o conteudo do site (pagina)
# Decorete no Python atribui uma nova funcionalidade para a função
# templetes 

# criar pagina homepage
@app.route('/')
def homepage():
#    return '<p><h1>Esse é o meu primeiro site </h1></p><br><h2>Python WEB  </h2>'
    return render_template('homepage.html')

# ciar pagina contatos
@app.route('/contatos')
def contatos():
#    return '<h1><center>Nossos contatos são email:pythonemail@gmail.com - Fone 999-999'
    return render_template('contatos.html')

# Criar uma pagina dinamica no templete usuarios
@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)


# Executar o arquivo  quando for chamado e não importado
# deploy do site, consiste no processo de disponibilizar na internet a aplicação já conscluida 
if __name__ == '__main__':
    app.run(debug=True)