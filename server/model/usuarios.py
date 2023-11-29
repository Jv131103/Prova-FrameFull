from model.config import Connection

class Usuario(Connection):
    def __init__(self):
        super().__init__()

    def UserExists(self, atributo, dado_inserido):
        try:
            # Construa a consulta SQL com base no atributo fornecido
            query = f"SELECT * FROM usuario WHERE {atributo} = %s"
            self.cursor.execute(query, (dado_inserido,))
            result = self.cursor.fetchone()

            # Verifique se um usuário foi encontrado
            if result:
                return True  # O usuário existe
            else:
                return False  # O usuário não existe

        except Exception as e:
            print(f"Erro ao verificar se o usuário existe: {e}")
            return False

    
    def ReadAllUsers(self):
        try:
            query = "SELECT * FROM usuario"
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            lista_usuarios = []
            if results:
                for result in results:
                    user_d = {
                        "id": result[0],
                        "username": result[1],
                        "email": result[2],
                        "senha": result[3]
                    }
                    lista_usuarios.append(user_d)
                return lista_usuarios
            else:
                print("Banco de dados Vazio!")
                return lista_usuarios
        except Exception as e:
            print("Houve um erro ao verificar usuários")
            print(e)
            return False, e
        
    
    def ReadUser(self, atributo, dado_inserido):
        try:
            if self.UserExists(atributo, dado_inserido):
                query = f"SELECT * FROM usuario WHERE {atributo} = %s"
                self.cursor.execute(query, (dado_inserido,))
                result = self.cursor.fetchone()
                if result:
                    user_unique = {
                        "id": result[0],
                        "username": result[1],
                        "email": result[2],
                        "senha": result[3]
                    }
                    return user_unique
                else:
                    print("Usuário não encontrado")
                    return None
            else:
                print("Usuário não encontrado")
                return None
        except Exception as e:
            print("Houve um erro ao verificar um usuário")
            print(e)
            return False, e


if __name__ == '__main__':
    db = Usuario()
    print(db.ReadUser("id", 100))

