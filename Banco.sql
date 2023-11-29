CREATE DATABASE Produtos;
USE Produtos;

CREATE TABLE usuario(
	id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL,
    senha VARCHAR(150) NOT NULL,
    CONSTRAINT pk_id_usuario PRIMARY KEY (id),
    CONSTRAINT uk_email_usuario UNIQUE (email)
);

CREATE TABLE produtos(
	id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(150) NOT NULL,
    objeto VARCHAR(150),
    CONSTRAINT pk_id_produtos PRIMARY KEY (id)
);


DROP TABLE usuario;
DROP TABLE produtos;


INSERT INTO usuario(username, email, senha)
VALUE('user_comum', 'user@user', 'senha'), ('user_adm', 'adm@adm', '12345'), ('joão', 'jv@jv.com', 'senha'),
('batata', 'batata@batata', '54321');

INSERT INTO produtos(nome, objeto)
VALUES('produtox', 'produto'), ('produtoy', 'produto');

SELECT * FROM usuario;
SELECT * FROM produtos;


