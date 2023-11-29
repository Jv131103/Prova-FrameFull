from flask import Flask
from controller.verificar_produtos import *
from controller.verificar_usuarios import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir requisições de origens diferentes (Cross-Origin Resource Sharing)


# Criar uma instância do ControlProduct
control_product = ControlProduct()
control_user = ControlUsers()

# Rotas
@app.route('/allproducts', methods=['GET'])
def get_products():
    return control_product.ReadProducts()

@app.route('/products/<int:id_produto>', methods=['GET'])
def get_product(id_produto):
    return control_product.ReadProduct(id_produto)

@app.route('/products', methods=['POST'])
def create_product():
    json_data = request.get_json()
    return control_product.Create(json_data)

@app.route('/users', methods=['GET'])
def get_users():
    return control_user.ReadUsers()

@app.route('/user/<string:atributo>/<string:dado>', methods=['GET'])
def get_user(atributo, dado):
    if dado.isnumeric():
        dado = int(dado)
    return control_user.ReadUser(atributo, dado)

if __name__ == '__main__':
    app.run(debug=True)
