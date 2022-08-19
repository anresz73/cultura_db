DROP TABLE IF EXISTS tabla_3 CASCADE;
CREATE TABLE IF NOT EXISTS tabla_3 (
    id_provincia INTEGER PRIMARY KEY,
    provincia VARCHAR(80),
    pantallas INTEGER,
    butacas INTEGER,
    espacio_incaa INTEGER,
    fecha_carga DATE NOT NULL DEFAULT CURRENT_DATE
);