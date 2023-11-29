from model.config import Connection

class Produto(Connection):
    def __init__(self):
        super().__init__()

    
    def ProductExists(self, atributo, dado_inserido):
        try:
            # Construa a consulta SQL com base no atributo fornecido
            query = f"SELECT * FROM produtos WHERE {atributo} = %s"
            self.cursor.execute(query, (dado_inserido,))
            result = self.cursor.fetchone()

            # Verifique se um usuário foi encontrado
            if result:
                return True  # O usuário existe
            else:
                return False  # O usuário não existe

        except Exception as e:
            print(f"Erro ao verificar se o produto existe: {e}")
            return False

    
    def CreateProduct(self, json):
        try:
            query = 'INSERT INTO produtos(nome, objeto) VALUES (%(nome)s, %(objeto)s)'
            self.cursor.execute(query, json)
            self.connection.commit()
        except Exception as e:
            print("Houve um erro ao criar o produto")
            print(e)
            return False
        else:
            print("Produto criado com sucesso!")
            return True
        
    
    def ReadAllProduct(self):
        try:
            query = "SELECT * FROM produtos"
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            lista_produtos = []
            if results:
                for result in results:
                    prod_d = {
                        "id": result[0],
                        "nome": result[1],
                        "objeto": result[2]
                    }
                    lista_produtos.append(prod_d)
                return lista_produtos
            else:
                print("Banco de dados Vazio")
                return lista_produtos
        except Exception as e:
            print("Houve um erro ao verificar os produtos")
            print(e)
            return False, e
        
    
    def ReadProduct(self, atributo, dado_inserido):
        try:
            if self.ProductExists(atributo, dado_inserido):
                query = f"SELECT * FROM produtos WHERE {atributo} = %s"
                self.cursor.execute(query, (dado_inserido,))
                result = self.cursor.fetchone()
                if result:
                    prod_unique = {
                        "id": result[0],
                        "nome": result[1],
                        "objeto": result[2]
                    }
                    return prod_unique
                else:
                    print("Produto não encontrado")
                    return None
            else:
                print("O produto não existe")
                return False
        except Exception as e:
            print("Houve um erro ao verificar um produto")
            print(e)
            return False, e
        
    
    def UpdateProduct(self, update_json):
        try:
            query = "UPDATE produtos SET nome = %(nome)s, objeto = %(objeto)s WHERE id = %(id)s"
            self.cursor.execute(query, update_json)
            return True
        except Exception as e:
            print("Houve um erro ao atualizar dados de um produto")
            print(e)
            return False


    def DeleteProducts(self, id_product):
        try:
            if self.ReadProduct(id_product):
                query = "DELETE FROM produtos WHERE id = %s"
                self.cursor.execute(query, (id_product, ))
                self.connection.commit()
                return True
            else:
                print("Produto não encontrado para remover")
                return None
        except Exception as e:
            print("Houve um erro ao remover um produto")
            print(e)
            return False


if __name__ == "__main__":
    db = Produto()
    #json_create = {"nome": "produtoa", "objeto": "produto"}
    #print(db.CreateProduct(json_create))
    #print(db.ReadAllProduct())
    #print(db.ReadProduct("id", 1))
    #json_update = {"id": 4, "nome": "produtow", "objeto": "produto"}
    #print(db.UpdateProduct(json_update))
    #print(db.DeleteProducts(4))
