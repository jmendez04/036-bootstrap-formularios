from flask import Flask, render_template, request

app = Flask(__name__)

USUARIOS = {"admin": "1234"}


@app.route("/")
def inicio():
    return render_template("inicio.html")


@app.route("/clientes", methods=["GET", "POST"])
def clientes():
    if request.method == "POST":
        nombre = request.form["nombre"]
        nit = request.form["nit"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        direccion = request.form["direccion"]

        return render_template(
            "clientes_confirmacion.html",
            nombre=nombre,
            nit=nit,
            correo=correo,
            telefono=telefono,
            direccion=direccion
        )

    return render_template("clientes.html")


@app.route("/proveedores", methods=["GET", "POST"])
def proveedores():
    if request.method == "POST":
        empresa = request.form["empresa"]
        contacto = request.form["contacto"]
        nit = request.form["nit"]
        tipo = request.form["tipo"]
        condicion = request.form["condicion"]
        activo = "Sí" if "activo" in request.form else "No"

        return render_template(
            "proveedores_confirmacion.html",
            empresa=empresa,
            contacto=contacto,
            nit=nit,
            tipo=tipo,
            condicion=condicion,
            activo=activo
        )

    return render_template("proveedores.html")


@app.route("/login", methods=["GET", "POST"])
def iniciar_sesion():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contrasena = request.form["contrasena"]
        acceso = USUARIOS.get(usuario) == contrasena

        return render_template(
            "login_resultado.html",
            usuario=usuario,
            acceso=acceso
        )

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)