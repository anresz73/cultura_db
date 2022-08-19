ALTER TABLE tabla_1
    ADD CONSTRAINT fk_provincias_id
    FOREIGN KEY (id_provincia)
    REFERENCES tabla_3 (id_provincia);