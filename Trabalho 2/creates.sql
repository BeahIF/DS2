CREATE TABLE serie (
	id_serie SERIAL PRIMARY KEY, 
	nome VARCHAR, 
	quantidadeep int, 
	quantidadetemp int, 
	data date
);

CREATE TABLE spoiler (
	id_spoiler SERIAL PRIMARY KEY, 
	descricao VARCHAR, 
	episodio int, 
	data date, 
	datamodificacao date, 
	id_serie INT, 
	 FOREIGN KEY (id_serie) references serie(id_serie)
	 );


