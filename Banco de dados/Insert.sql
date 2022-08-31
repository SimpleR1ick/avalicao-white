
-- 5) Faça um script que insira um novo cargo e um novo usuário.
INSERT INTO Cargo (CODG_CARGO, DESC_CARGO) VALUES 
(1, "Gerente de tecnologia"),
(2, "Estagiario");

INSERT INTO Pessoa (DESC_NOME, DATA_NASCIMENTO, CODG_CARGO) VALUES 
("Sergio Almeida Costa", "1992-01-01", 1),
("Henrique Dalmagro", "2004-09-28", NULL),
("Rafael Barros", "2004-11-11", NULL);
