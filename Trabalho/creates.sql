create table quarto(
id serial primary key, 
dtHrAtualizacao timestamp, 
quant_pessoas varchar, 
);

create table cliente(
id serial primary key, 
dtHrAtualizacao timestamp, 
nome varchar, 
cpf varchar
);

create table reserva(
id serial primary key, 
dtHrAtualizacao timestamp,
cliente int
foreign key (cliente) references cliente (id)
quarto int
foreign key (quarto) references quarto (id),
entrada date, 
saida date, 
valor int
);