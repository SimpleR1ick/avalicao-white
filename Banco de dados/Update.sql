
-- 6) Faça um script que atualiza o Usuario inserido na questão anterior e insira o cargo definido na questão anterior.
UPDATE Pessoa SET CODG_CARGO = 2 WHERE CODG_PESSOA = 2;

-- 7) Faça um script que retorna como resultado todos os usuários ativos de um cargo selecionado ordenados pelo nome do usuário.
SELECT * FROM Pessoa WHERE CODG_CARGO = 2 ORDER BY DESC_NOME;