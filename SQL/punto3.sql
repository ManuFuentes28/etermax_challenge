create TABLE DATA_LIST_MOVIMIENTOS(
  FECHA TIMESTAMP NOT NULL,
  DESC_CLI VARCHAR NOT NULL,
  DESC_PROV VARCHAR NOT NULL,
  DESC_PROD VARCHAR NOT NULL,
  DESC_MAR VARCHAR NOT NULL,
  CANTIDAD DECIMAL,
  COSTO DECIMAL,
  VENTA DECIMAL,
  GANANCIA_NETA DECIMAL
)

select 
    desc_cliente,
    sum(ganancia_neta)
FROM (
    SELECT 
        fecha,
        desc_cliente,
        ganancia_neta
    FROM data_list_movimientos 
    WHERE desc_cliente = 'Andy' AND fecha::text LIKE '%2021-01-10%'
    ORDER BY fecha DESC
    LIMIT 7
) AS t1
GROUP BY 1

insert into DATA_LIST_MOVIMIENTOS VALUES
	('2001-09-28 01:10','pepe','coca','botella','coca','10','40.00','100','40'),
	('2001-09-28 01:20','pepe','coca','botella','coca','10','40.00','100','30'),
	('2001-09-28 01:30','pepe','coca','botella','coca','10','40.00','100','20'),
  	('2001-09-28 01:40','pepe','coca','botella','coca','10','40.00','100','10'),
  	('2001-09-28 01:50','pepe','coca','botella','coca','10','40.00','100','50'),
  	('2001-09-28 01:15','pepe','coca','botella','coca','10','40.00','100','60'),
  	('2001-09-28 01:25','pepe','coca','botella','coca','10','40.00','100','70'),
  	('2001-09-28 01:35','pepe','coca','botella','coca','10','40.00','100','80'),
  	('2001-09-28 01:45','pepe','coca','botella','coca','10','40.00','100','90'),
  	('2001-09-28 01:55','pepe','coca','botella','coca','10','40.00','100','100'),
  	('2001-09-28 01:10','andy','coca','botella','coca','10','40.00','100','40'),
	('2001-09-28 01:20','andy','coca','botella','coca','10','40.00','100','30'),
	('2001-09-28 01:30','andy','coca','botella','coca','10','40.00','100','20'),
  	('2001-09-28 01:40','andy','coca','botella','coca','10','40.00','100','10'),
  	('2001-09-28 01:50','andy','coca','botella','coca','10','40.00','100','50'),
  	('2001-09-28 01:15','andy','coca','botella','coca','10','40.00','100','60'),
  	('2001-09-28 01:25','andy','coca','botella','coca','10','40.00','100','70'),
  	('2001-09-28 01:35','andy','coca','botella','coca','10','40.00','100','80'),
  	('2001-09-28 01:45','andy','coca','botella','coca','10','40.00','100','90'),
  	('2001-09-28 01:55','andy','coca','botella','coca','10','40.00','100','100'),
    ('2001-09-21 01:10','pepe','coca','botella','coca','10','40.00','100','40'),
	('2001-09-21 01:20','pepe','coca','botella','coca','10','40.00','100','30'),
	('2001-09-21 01:30','pepe','coca','botella','coca','10','40.00','100','20'),
  	('2001-09-21 01:40','pepe','coca','botella','coca','10','40.00','100','10'),
  	('2001-09-21 01:50','pepe','coca','botella','coca','10','40.00','100','50'),
  	('2001-09-21 01:15','pepe','coca','botella','coca','10','40.00','100','60'),
  	('2001-09-21 01:25','pepe','coca','botella','coca','10','40.00','100','70'),
  	('2001-09-21 01:35','pepe','coca','botella','coca','10','40.00','100','80'),
  	('2001-09-21 01:45','pepe','coca','botella','coca','10','40.00','100','90'),
  	('2001-09-21 01:55','pepe','coca','botella','coca','10','40.00','100','100'),
  	('2001-09-21 01:10','andy','coca','botella','coca','10','40.00','100','40'),
	('2001-09-21 01:20','andy','coca','botella','coca','10','40.00','100','30'),
	('2001-09-21 01:30','andy','coca','botella','coca','10','40.00','100','20'),
  	('2001-09-21 01:40','andy','coca','botella','coca','10','40.00','100','10'),
  	('2001-09-21 01:50','andy','coca','botella','coca','10','40.00','100','50'),
  	('2001-09-21 01:15','andy','coca','botella','coca','10','40.00','100','60'),
  	('2001-09-21 01:25','andy','coca','botella','coca','10','40.00','100','70'),
  	('2001-09-21 01:35','andy','coca','botella','coca','10','40.00','100','80'),
  	('2001-09-21 01:45','andy','coca','botella','coca','10','40.00','100','90'),
  	('2001-09-21 01:55','andy','coca','botella','coca','10','40.00','100','100');
