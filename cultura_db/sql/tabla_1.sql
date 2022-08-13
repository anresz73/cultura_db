CREATE TABLE tabla_1 (
    cod_localidad INTEGER,
    id_provincia INTEGER,
    id_departamento INTEGER,
    categoria VARCHAR(50),
    provincia VARCHAR(80),
    localidad VARCHAR(50),
    nombre VARCHAR(150),
    domicilio VARCHAR(100)
    codigo_postal INTEGER,
    telefono VARCHAR(50),
    mail VARCHAR(100),
    web VARCHAR(200),
    fuente VARCHAR(80),
    fecha_carga NOT NULL DEFAULT CURRENT_DATE
);