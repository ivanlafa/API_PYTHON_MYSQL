# pip install Flask       :: framework para crear app de manera rapida y con pocas
#                            lineas de codigo

# pip install flask-mysql :: extension que me permite conectar a una base de datos
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "987897asdf7987sad"

app.config["MYSQL_HOST"]        = "localhost"
app.config["MYSQL_USER"]        = "root"
app.config["MYSQL_PASSWORD"]    = ""
app.config["MYSQL_DB"]          = "BDESTUDIANTE"

mysql = MySQL(app)

# rutas: registrar, editar, eliminar, listar, principal 
@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/frmEstudiante")
def frmEstudiante():
    return render_template("frmEstudiante.html")

@app.route("/registro", methods=["POST"])
def registro():
    if request.method == "POST":
        nombre      = request.form["nombre"]
        primerApellido = request.form["primerApellido"]
        segundoApellido = request.form["segundoApellido"]
        codigo = request.form["codigo"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        fecha = request.form["fecha"]
        c = mysql.connection.cursor()
        
        
        c.execute("INSERT INTO t_estudiantes(EST_NOMBRE,EST_PRIMER_APELLIDO, EST_SEGUNDO_APELLIDO,EST_CODIGO,EST_CORREO,EST_TELEFONO,EST_FECHA_NAC)VALUES(%s,%s,%s,%s,%s,%s,%s)",(
            nombre, primerApellido,segundoApellido,codigo,correo,telefono,fecha ))
        mysql.connection.commit()
        # flash("Producto registrado")
        return jsonify({"mensaje":"Estudiante registrado", "estado": 1})
        # return redirect(url_for("frmEstudiante")) # nombre de la funcion


@app.route('/eliminar/<id>', methods=["DELETE"])
def eliminar(id):
    c = mysql.connection.cursor()
    c.execute("DELETE FROM t_estudiantes WHERE EST_ID = %s", (id,))
    mysql.connection.commit()
    return jsonify({"mensaje": "Estudiante eliminado", "estado": 1})

@app.route('/frmEditar/<id>')
def frmEditar(id):
    c = mysql.connection.cursor()
    c.execute("SELECT *  FROM t_estudiantes WHERE EST_ID = %s", (id))
    datos = c.fetchall()
    return render_template("frmPEdicion.html", persona = datos[0])


#VAMOS POR AQUI
@app.route("/editar/<id>", methods=["POST"])
def editar(id):
    if request.method == "POST":
        nombre      = request.form["nombre"]
        primerApellido = request.form["primerApellido"]
        segundoApellido = request.form["segundoApellido"]
        codigo = request.form["codigo"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        fecha = request.form["fecha"]
        
        
        c = mysql.connection.cursor()
        c.execute("""
                UPDATE t_estudiantes SET EST_NOMBRE =  %s , EST_PRIMER_APELLIDO =  %s , EST_SEGUNDO_APELLIDO = %s , EST_CODIGO = %s, EST_CORREO = %s, EST_TELEFONO = %s, EST_FECHA_NAC = %s
                WHERE EST_ID = %s
            """,(nombre, primerApellido, segundoApellido, codigo,correo,telefono, fecha, id ))
        mysql.connection.commit()
        # flash("Producto editado")
        # return jsonify({"estado":"Producto registrado"})
        # return redirect(url_for("frmEditar", id = id )) # nombre de la funcion
        return jsonify({"mensaje":"Estudiante editado", "estado": 1})
    # CRUD : CREATE, READ, UPDATE, DELETE


@app.route("/ADMESTUDIANTE")
def AdmEstudiante():
    c = mysql.connection.cursor()
    c.execute("SELECT * FROM t_estudiantes")
    datos = c.fetchall()
    return render_template("AdmEstudiante.html", personas = datos)

if __name__ == "__main__":
    app.run(debug=True, port= 3000)