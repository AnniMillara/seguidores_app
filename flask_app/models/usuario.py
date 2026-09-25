from flask_app.config.mysqlconnection import connectToMySQL

class Usuarios:
    def __init__(self, data):
        self.id_usuario = data["id_usuario"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.contrasena = data["contrasena"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def all(cls):
        query = """
        SELECT
            id_usuario,
            nombre,
            apellido,
            email,
            contrasena,
            created_at,
            updated_at
        FROM usuarios
        ORDERED BY id_usuario;
        """
        
        resultados = connectToMySQL("esquema_seguidores").query(query)
        usuarios = []
        for user in resultados:
            usuarios.append(cls(user))
        
        return usuarios

    @classmethod
    def por_id(cls, id):
        query = """
        SELECT
            id_usuario,
            nombre,
            apellido,
            contrasena,
            email,
            created_at,
            updates_at
        FROM usuarios WHERE id_usuario = %(id_usuario)s;
        """
        
        data = {"id_usuario" : id}
        resultados = connectToMySQL("esquema_seguidores").query(query, data)
        
        if resultados:
            return cls(resultados[0])
        
        return None
    
    @classmethod
    def guardar(cls, data):
        query = """
        INSERT INTO usuarios(
            nombre,
            apellido,
            contrasena,
            email,
        VALUES(
            %(nombre)s,
            %(apellido)s,
            %(contrasena)s,
            %(email)s
        )
        """
        
        return connectToMySQL("esquema_seguidores".query(query, data))