DROP TABLE IF EXISTS tabla_2;
CREATE TABLE tabla_2 (
    items VARCHAR(200),
    cantidad_registros INTEGER,
    fecha_carga DATE NOT NULL DEFAULT CURRENT_DATE
);