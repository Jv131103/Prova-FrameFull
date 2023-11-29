def Json(sucess, response, text, status, data=None):
        d = {
            "sucess": sucess,
            "response": response,
            "text": text,
            "status": status,
            "data": data
        }
        return d
