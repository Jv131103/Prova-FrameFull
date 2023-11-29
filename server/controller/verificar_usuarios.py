from flask import Flask, make_response, jsonify, request
from model.usuarios import Usuario
from controller.js import Json

class ControlUsers:
    def __init__(self) -> None:
        self.usuario = Usuario()

    
    def ReadUsers(self):
        user = self.usuario.ReadAllUsers()
        if isinstance (user, list):
            return make_response(jsonify(Json(True, 200, "Usuários Retornados", "ok", data=user)))
        elif user == []:
            return make_response(jsonify(Json(False, 500, "Não há usuários cadastrados", "false", None)))
        else:
            if user[0] == False:
                return make_response(jsonify(Json(False, 500, f"Houve um erro ao verificar usuário: {user[1]}", 'fail', None)))
            return make_response(jsonify(Json(False, 500, "Um erro inesperado aconteceu ao verificar os usuários", 'fail', None)))
    

    def ReadUser(self, atributo, dado):
        user = self.usuario.ReadUser(atributo, dado)
        if isinstance(user, dict):
            return make_response(jsonify(Json(True, 200, "Usuário encontrado", "ok", data=user)))
        else:
            if user == None:
                return make_response(jsonify(Json(False, 404, "Usuário procurado não encontrado", "fail", None)))
            elif user == False:
                return make_response(jsonify(Json(False, 404, "O usuário não existe", "fail", None)))
            elif user[1]:
                return make_response(jsonify(Json(False, 500, f"houve um erro interno ao verificar usuário: {user[1]}", "fail", None)))
            return make_response(jsonify(Json(False, 500, f"houve um erro interno ao verificar um usuário", "fail", None)))


