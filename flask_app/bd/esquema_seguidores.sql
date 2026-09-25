DROP DATABASE IF EXISTS esquema_seguidores;
CREATE DATABASE IF NOT EXISTS esquema_seguidores;
USE esquema_seguidores;

CREATE TABLE IF NOT EXISTS usuarios(
    id_usuario  INT AUTO_INCREMENT PRIMARY KEY,
    nombre      VARCHAR(45) NOT NULL,
    apellido    VARCHAR(45) NOT NULL,
    email       VARCHAR(50) UNIQUE NOT NULL,
    contrasena  VARCHAR(255) NOT NULL,          -- 👈 ampliado
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS seguidores(
    id           INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id   INT NOT NULL,
    seguidor_id  INT NOT NULL,
    created_at   DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at   DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT uq_usuario_seguidor UNIQUE (usuario_id, seguidor_id),  -- 👈 evita duplicados
    CONSTRAINT fk_usuario_seguidor
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_seguidor_usuario
        FOREIGN KEY (seguidor_id) REFERENCES usuarios(id_usuario)
        ON DELETE CASCADE ON UPDATE CASCADE
)