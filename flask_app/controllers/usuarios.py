from flask_app import app

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_app.models.usuario import Usuarios
from flask_app.models.seguidor import Seguidores

@app.route("/")
def inicio():
    return redirect(url_for("usuarios"))

# USUARIOS RUTAS
@app.route("/usuarios")
def usuarios():
    lista_usuarios = Usuarios.all()
    lista_seguidores = Seguidores.todos()
    
    return render_template(
        "usuarios.html",
        users = lista_usuarios,
        relaciones = lista_seguidores
    )

@app.route("/usuarios/crear", methods=["POST"])
def registrar():
    nombre = request.form.get("nombre", " ").strip()
    apellido = request.form.get("apellido", " ").strip()
    contrasena = request.form.get("contrasena", " ").strip()
    email = request.form.get("email", " ").strip()
    
    if not nombre or not apellido or not contrasena or not email:
        flash("Todos los campos son obligatorios", "danger")
        return redirect(url_for("usuarios"))
    
    data = {
        "nombre" : nombre,
        "apellido" : apellido,
        "email" : email,
        "contrasena" : contrasena
    }
    resultado = Usuarios.guardar(data)
    if resultado is False:
        flash("Ups, parece que algo salio mal", "danger")
        return redirect(url_for("usuarios"))
    
    flash("Usuario creado correctamente!!", "success")
    return redirect(url_for("usuarios"))

# CREAR RELACIONES(seguidores)
@app.route("/seguir", methods=["POST"])
def seguir():
    usuario_texto = request.form.get("usuario_id")
    seguidor_texto = request.form.get("seguidor_id")
    
    if not usuario_texto or not seguidor_texto:
        flash("Todos los campos son obligatorios", "danger")
        return redirect(url_for("usuarios"))
    
    try:
        usuario_id = int(usuario_texto)
        seguidor_id = int(seguidor_texto)
    except ValueError:
        flash("Ups, identificadores no válidos", "danger")
        return redirect(url_for("usuarios"))
    
    if usuario_id == seguidor_id:
        flash("Un usuario no puede seguirse a sí mismo", "danger")
        return redirect(url_for("usuarios"))
    
    user = Usuarios.por_id(usuario_id)
    if user is None:
        flash("Ups, parece que el usuario no exite", "danger")
        return redirect(url_for("usuarios"))
    
    seg = Usuarios.por_id(seguidor_id)
    if seg is None:
        flash("Ups, parece que el seguidor no exite", "danger")
        return redirect(url_for("usuarios"))
    
    data = {
        "usuario_id" : usuario_id,
        "seguidor_id" : seguidor_id
    }
    
    resultado = Seguidores.seguir(data)
    if resultado is False:
        flash("Ups, parece que algo fallo en la unión", "danger")
        return redirect(url_for("usuarios"))
    
    flash("Unión hecha correctamente!!", "success")
    return redirect(url_for("usuarios"))