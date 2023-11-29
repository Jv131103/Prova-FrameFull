import mysql.connector


class Connection:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Joao$131103",
            database="Produtos"
        )
        self.cursor = self.connection.cursor()

    def CloseSQL(self):
        try:
            self.connection.close()
        except Exception as e:
            print("Um erro ocorreu ao fechar o banco de dados")
            return False
        else:
            print("Banco de dados fechado com sucesso!")
            return True

    '''
    def GerarJson(self, sucess, response, text, status, data=None):
        d = {
            "sucess": sucess,
            "response": response,
            "text": text,
            "status": status,
            "data": data
        }
        return d
    '''
