from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def index():
    dojos = Dojo.get_all() # regresa los valores del metodo get all y almacena todos los datos de lbd
    print(dojos)
    return render_template("dojos.html",dojos=dojos) 

@app.route('/show/<int:id>')
def show_user(id):
    print(id)
    data = {
        "id": id
        }
    print(data)
    dojo_ninjas= Dojo.get_ninjas_by_dojoid(data)
    print(dojo_ninjas.ninjas)
    return render_template("show.html",dojo_ninjas=dojo_ninjas) 

@app.route("/show_ninja_page")
def show_ninja_page():
    dojos = Dojo.get_all() # regresa los valores del metodo get all y almacena todos los datos de lbd
    print(dojos)
    return render_template("ninjas.html",dojos=dojos)

@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    # for key in request.form:
    #     print(key)
    #     print(request.form[key])
    print(request.form["location"])    
    print(request.form["last_name"])
    print(request.form["first_name"])
    print(request.form["age"])
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["location"]
        # guarda los valores del formulario
        }
   
    ninja_id=Ninja.save(data) # manda llamar al metodo para guardar
    print(ninja_id)
   
    return redirect("/")# lo que me regreso de la base al html
        # si es otra pagina 

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"] 
        }
   
    dojo_id=Dojo.save(data) # manda llamar al metodo para guardar
    print(dojo_id)
   
    return redirect("/")# lo que me regreso de la base al html
        # si es otra pagina 
