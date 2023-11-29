from flask import Flask, Blueprint
from controller.verificar_produtos import ControlProduct
from controller.verificar_usuarios import ControlUsers

blueprint = Blueprint('blueprint', __name__)

c = ControlProduct()
u = ControlUsers()

blueprint.route('/api/produtos', methods=['GET'])(c.ReadProducts)
blueprint.route('/api/produtos', methods=['POST'])(c.Create)

blueprint.route('/api/users', methods=['GET'])(u.ReadUsers)
