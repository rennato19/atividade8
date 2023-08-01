# test_pessoa.py
from pessoa import Pessoa, Funcionario

# Teste da classe Pessoa
pessoa1 = Pessoa(nome="Maria")
print("Nome da Pessoa: ", pessoa1.nome)

# Teste da classe Funcionario
funcionario1 = Funcionario(nome="João", cargo="Desenvolvedor")
print("Nome: ", funcionario1.nome)
print("Cargo: ", funcionario1.cargo)

