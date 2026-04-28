CREATE DATABASE gastos;
USE gastos;

CREATE TABLE cadastro_gastos (
id_compra INT PRIMARY KEY AUTO_INCREMENT,
nome_compra VARCHAR(25) NOT NULL,
preco_compra DECIMAL(10, 2) NOT NULL,
data_compra DATE NOT NULL,
categoria_compra VARCHAR(25) NOT NULL
);

