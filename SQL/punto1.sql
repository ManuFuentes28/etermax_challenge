CREATE TABLE IF NOT EXISTS DATA_LIST_MOVIMIENTOS(
    fecha date not null sortkey,
    desc_cli varchar(100),
    desc_prov varchar(100),
    desc_prod varchar(100),
    desc_mar varchar(100),
    cantidad integer not null,
    costo decimal(18,2) not null,
    venta decimal(18,2) not null,
    ganancia_neta decimal(18,2) not null
);
