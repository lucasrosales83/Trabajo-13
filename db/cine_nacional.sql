USE buv9i87h4otuvwok1mt2;

-- ==========================
-- Tabla: directores
-- ==========================
DROP TABLE IF EXISTS peliculas;
DROP TABLE IF EXISTS directores;

CREATE TABLE directores (
    id_director INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50) NOT NULL DEFAULT 'Argentina'
);

-- ==========================
-- Tabla: peliculas
-- ==========================
CREATE TABLE peliculas (
    id_pelicula INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    anio_estreno INT NOT NULL,
    duracion_minutos INT,
    genero VARCHAR(50),
    id_director INT NOT NULL,
    CONSTRAINT fk_peliculas_directores
        FOREIGN KEY (id_director) REFERENCES directores(id_director)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- ==========================
-- Datos de prueba
-- ==========================

INSERT INTO directores (nombre, apellido, nacionalidad) VALUES
('Lucrecia', 'Martel', 'Argentina'),
('Damián', 'Szifron', 'Argentina'),
('Juan José', 'Campanella', 'Argentina'),
('Pablo', 'Trapero', 'Argentina');

INSERT INTO peliculas (titulo, anio_estreno, duracion_minutos, genero, id_director) VALUES
('La ciénaga', 2001, 103, 'Drama', 1),
('La niña santa', 2004, 106, 'Drama', 1),
('Relatos salvajes', 2014, 122, 'Comedia negra', 2),
('Tiempo de valientes', 2005, 118, 'Comedia', 2),
('El secreto de sus ojos', 2009, 129, 'Thriller', 3),
('El clan', 2015, 108, 'Crimen', 4);