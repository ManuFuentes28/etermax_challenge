/* Generar una tabla, con el listado de todos los Movimientos, con el siguiente contenido :
. Fecha
. Descripción de Cliente
. Descripción de Proveedor
. Descripción de Producto
. Descripcion de Marca
. Cantidad
. Costo
. Venta
. Ganancia Neta*/
CREATE TABLE IF NOT EXISTS DATA_LIST_MOVIMIENTOS
(
    fecha           date not null sortkey,
    desc_cliente    varchar(50),
    desc_proveedor  varchar(50),
    desc_producto   varchar(50),
    desc_marca      varchar(50),
    cantidad        integer not null,
    costo           decimal(18, 2) not null,
    venta           decimal(18, 2) not null,
    ganancia_neta   decimal(18, 2) not null,
    --primary key (fecha)
);


-- Listado de todas las Marcas que no tuvieron Ventas
SELECT dmar.cod_marca, dmar.descripcion FROM (
    SELECT 
        dprod.cod_marca
    FROM DATA_MOVIMIENTOS AS dmov
    INNER JOIN DATA_PRODUCTOS AS dprod
        ON dmov.cod_prod = dprod.cod_prod
    GROUP BY dprod.cod_marca
) AS join1
RIGHT JOIN DATA_MARCA AS dmar
    ON dmar.cod_marca = join1.cod_marca
    WHERE join1.cod_marca IS NULL

/* En base a la tabla generada en a, consultar, ordenando por fecha y descripción del cliente:
. Fecha
. Descripción de Cliente
. Ganancia Neta Acumulada en las últimas 7 operaciones
La idea del punto c es, dado un cliente y una fecha de operación, mostrar la sumatoria de
las ganancias derivadas de las últimas siete operaciones que haya realizado.*/
select 
    desc_cliente,
    sum(ganancia_neta)
FROM (
	SELECT 
		fecha,
    	desc_cliente,
    	ganancia_neta
	from data_list_movimientos 
    WHERE desc_cliente = 'Andy' AND fecha::text LIKE '%2021-01-10%'
    order by fecha desc
    LIMIT 7
) as t1
GROUP BY 1

/*====== CREATE BD ======*/
CREATE TABLE DATA_MARCAS(
  COD_MARCA INTEGER,
  DESCRIPCION VARCHAR);

CREATE TABLE DATA_PROVEEDORES(
  COD_PROVEEDOR INTEGER,
  DESCRIPCION VARCHAR);

CREATE TABLE DATA_CLIENTES(
  COD_CLIENTE INTEGER,
  DESCRIPCION VARCHAR);

create TABLE DATA_PRODUCTOS(
  COD_PROD INTEGER,
  COD_MARCA INTEGER,
  COD_PROVEEDOR INTEGER,
  DESCRIPCION VARCHAR);

create TABLE DATA_MOVIMIENTOS(
  COD_PROD INTEGER,
  COD_CLIENTE INTEGER,
  FECHA DATE,
  CANTIDAD DECIMAL,
  COSTO DECIMAL,
  VENTA DECIMAL);

CREATE TABLE IF NOT EXISTS DATA_LIST_MOVIMIENTOS
(
    fecha           timestamp not null,
    desc_cliente    varchar(50),
    desc_proveedor  varchar(50),
    desc_producto   varchar(50),
    desc_marca      varchar(50),
    cantidad        integer not null,
    costo           decimal(18, 2) not null,
    venta           decimal(18, 2) not null,
    ganancia_neta   decimal(18, 2) not null
);

INSERT INTO DATA_MARCA VALUES (1,'NIKE'),(2,'ADIDAS'),(3,'PUMAS');
INSERT INTO DATA_PRODUCTOS VALUES (1,1,1,'VENTA1'),(2,2,2,'VENTA2'),(3,2,2,'VENTA3');
INSERT INTO DATA_MOVIMIENTOS VALUES (1,1,'2021-01-08',1,1,1),(2,2,'2021-01-08',1,1,1),(3,3,'2021-01-08',1,1,1);
INSERT INTO DATA_LIST_MOVIMIENTOS VALUES 
	('2021-01-10 10:00:01','Andy','Lea Perea','Remera','ADIDAS',5,2,10,30),
    ('2021-01-10 11:00:01','Andy','Lea Perea','Remera','ADIDAS',5,2,10,20),
    ('2021-01-09 10:00:01','Andy','Lea Perea','Remera','ADIDAS',5,2,10,50),
    ('2021-01-08 10:00:01','Andy','Lea Perea','Remera','ADIDAS',5,2,10,10),
    ('2021-01-07 10:00:01','Andy','Lea Perea','Remera','ADIDAS',5,2,10,10),
    ('2021-01-06 10:00:01','Andy','Lea Perea','Remera','ADIDAS',5,2,10,30),
    ('2021-01-05 10:00:01','Andy','Lea Perea','Remera','ADIDAS',5,2,10,30),
    ('2021-01-01 10:00:01','Andy','Lea Perea','Remera','ADIDAS',5,2,10,30),
    ('2021-01-01 10:00:01','Andy','Lea Perea','Remera','ADIDAS',5,2,10,30)


CREATE TABLE IF NOT EXISTS DATA_LIST_MOVIMIENTOS_1
(
    fecha           date not null,
    desc_cliente    varchar(50),
    desc_proveedor  varchar(50),
    desc_producto   varchar(50),
    desc_marca      varchar(50),
    cantidad        integer not null,
    costo           decimal(18, 2) not null,
    venta           decimal(18, 2) not null,
    ganancia_neta   decimal(18, 2) not null
);

INSERT INTO DATA_LIST_MOVIMIENTOS_1 VALUES 
	('2021-01-10','Andy','Lea Perea','Remera','ADIDAS',5,2,10,30),
    ('2021-01-10','Andy','Lea Perea','Remera','ADIDAS',5,2,10,20),
    ('2021-01-09','Andy','Lea Perea','Remera','ADIDAS',5,2,10,50),
    ('2021-01-08','Andy','Lea Perea','Remera','ADIDAS',5,2,10,10),
    ('2021-01-07','Andy','Lea Perea','Remera','ADIDAS',5,2,10,10),
    ('2021-01-06','Andy','Lea Perea','Remera','ADIDAS',5,2,10,30),
    ('2021-01-05','Andy','Lea Perea','Remera','ADIDAS',5,2,10,30),
    ('2021-01-01','Andy','Lea Perea','Remera','ADIDAS',5,2,10,30),
    ('2021-01-01','Andy','Lea Perea','Remera','ADIDAS',5,2,10,30)
