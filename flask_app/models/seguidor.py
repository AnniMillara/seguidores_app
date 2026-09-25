from flask_app.config.mysqlconnection import connectToMySQL

class Seguidores:
    @classmethod
    def todos(cls):
        query = """
        SELECT
            u.id_usuario AS usuario_id,
            CONCAT(
                u.nombre,
                " ",
                u.apellido
            ) AS usuario_nombre,
            
            s.id_usuario AS seguidor_id,
            CONCAT(
                s.nombre,
                ' ',
                s.apellido
            ) AS seguidor_nombre
            
            FROM seguidores f
            INNER JOIN usuarios u
                ON f.usuario_id = u.id_usuario
            
            INNER JOIN usuarios s
                ON f.seguidor_id = s.id_usuario
        """
        
        return connectToMySQL("esquema_seguidores").query_db(query)

    @classmethod
    def existe(cls, data):
        query = """
        SELECT 
            id
        FROM seguidores
        WHERE usuario_id = %(usuario_id)s
        AND seguidor_id = %(seguidor_id)s;
        """
        
        resultado = connectToMySQL("esquema_seguidores").query_db(query, data)
        return bool(resultado)
    
    @classmethod
    def seguir(cls, data):
        query = """
        INSERT INTO seguidores(
            usuario_id,
            seguidor_id
        )VALUES(
            %(usuario_id)s,
            %(seguidor_id)s
        )
        """
        
        return connectToMySQL("esquema_seguidores").query_db(query, data)