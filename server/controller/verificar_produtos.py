from flask import Flask, make_response, jsonify, request
from model.produtos import Produto
from controller.js import Json

class ControlProduct:
    def __init__(self) -> None:
        self.produto = Produto()
    

    def ReadProducts(self):
        dados = self.produto.ReadAllProduct()
        if isinstance (dados, list):
            return make_response(jsonify(Json(True, 200, "Listagem de Produtos", "ok", dados)))
        elif dados == []:
            return make_response(jsonify(Json(False, 500, "Não há produtos no banco de dados", "fail", None)))
        else:
            if dados[0] == False:
                return make_response(jsonify(Json(False, 500, f"Erro interno ao verificar os produtos: {dados[1]}", "fail", "")))
            return make_response(jsonify(Json(False, 500, "Um erro inesperado aconteceu ao verificar os produtos", "fail", "")))


    def ReadProduct(self, id_produto):
        dados = self.produto.ReadProduct("id", id_produto)
        if isinstance (dados, dict):
            return make_response(jsonify(Json(True, 200, "Listagem de Produto", "ok", data=dados)))
        else:
            if dados == None:
                return make_response(jsonify(Json(False, 404, "Produto procurado não encontrado", "fail", None)))
            elif dados == False:
                return make_response(jsonify(Json(False, 404, "O produto não existe", "fail", None)))
            elif dados[1]:
                return make_response(jsonify(Json(False, 500, f"houve um erro interno: {dados[1]}", "fail", None)))
            return make_response(jsonify(Json(False, 500, f"houve um erro interno ao verificar um produto", "fail", None)))
        
    
    def Create(self, json):
        dados = self.produto.CreateProduct(json)
        if dados == True:
            return make_response(jsonify(Json(True, 200, "Produto cadastrado com sucesso", "ok", data=json)))
        else:
            if dados[1]:
                return make_response(jsonify(Json(False, 500, f"Houve um erro ao cadatrar produto: {dados[1]}", 'fail', None)))
            return make_response(jsonify(Json(False, 500, f"Houve um erro interno ao cadastrar o produto", 'fail', None)))
