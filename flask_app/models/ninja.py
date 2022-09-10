from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age= data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        # guarda el resultado de la bd
        
        ninjas = []
        # crea arreglo para guiardar los valores 
        for ninja in results: #itera los nombres de la base de datos 
            ninjas.append(cls(ninja))
            # flos mete en el arreglo -y los convierte en una clkase ususario
        return ninjas

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas ( first_name , last_name , age , created_at, updated_at, dojo_id) VALUES ( %(first_name)s , %(last_name)s , %(age)s , NOW() , NOW() ,%(dojo_id)s );"
        # los nombres deben ser los de la bd / los valores los del html
        return connectToMySQL('dojos_ninjas').query_db(query, data)

  