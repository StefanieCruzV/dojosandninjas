from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        # guarda el resultado de la bd

        dojos = []
        # crea arreglo para guiardar los valores
        for dojo in results:  # itera los nombres de la base de datos
            dojos.append(cls(dojo))
            # flos mete en el arreglo -y los convierte en una clkase ususario
        return dojos


    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name ,created_at, updated_at ) VALUES ( %(name)s ,  NOW() , NOW() );"
        # los nombres deben ser los de la bd / los valores los del html
        return connectToMySQL('dojos_ninjas').query_db(query, data)



    @classmethod
    def get_ninjas_by_dojoid(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id Where dojos.id= %(id)s"
        # los nombres deben ser los de la bd / los valores los del html
        results = connectToMySQL('dojos_ninjas').query_db(query, data)
        print(results)
        
        # dojo_data = {
        #     "id" : results[0]["id"],
        #     "name" : results[0]["name"],
        #     "created_at" : results[0]["created_at"],
        #     "updated_at" : results[0]["updated_at"]
        # }
        # dojo = cls(dojo_data) 
        # print(dojo.id)
        # print(dojo.name)
        # print(dojo.created_at)
        # print(dojo.updated_at)
        # print()
        # solo la primera parte soplo los dojos
        dojo_ob = cls( results[0] )  #primera parte
        for row_from_db in results:
          
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            # vamos a meter el objeto ninja en el arreglo de objeto dojo
            dojo_ob.ninjas.append(Ninja(ninja_data)) #primera parte mas ninjas
         
        return dojo_ob

