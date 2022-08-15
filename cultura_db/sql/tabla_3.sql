DROP TABLE IF EXISTS tabla_3;
CREATE TABLE tabla_3 (
    provincia VARCHAR(80),
    pantallas INTEGER,
    butacas INTEGER,
    espacio_incaa INTEGER,
    fecha_carga DATE NOT NULL DEFAULT CURRENT_DATE
);