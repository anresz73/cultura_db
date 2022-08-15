DROP TABLE IF EXISTS tabla_1;
CREATE TABLE tabla_1 (
    cod_localidad VARCHAR(10),
    id_provincia INTEGER,
    id_departamento INTEGER,
    categoria VARCHAR(50),
    provincia VARCHAR(80),
    localidad VARCHAR(50),
    nombre VARCHAR(150),
    domicilio VARCHAR(200),
    codigo_postal VARCHAR(10),
    telefono VARCHAR(50) NULL,
    mail VARCHAR(100) NULL,
    web VARCHAR(200) NULL,
    fuente VARCHAR(80) NULL,
    fecha_carga DATE NOT NULL DEFAULT CURRENT_DATE
);