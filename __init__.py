from flask import Flask
from routes.home import home_route
from routes.usuarios import usuarios_route  # Nova rota para login/cadastro

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

# Registrar rotas
app.register_blueprint(home_route)
app.register_blueprint(usuarios_route)

app.run(debug=True)
