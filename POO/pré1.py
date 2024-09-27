class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.set_idade(idade)
    
    def set_idade(self, idade):
        while idade < 18:
            idade = int(input("Idade inválida. Por favor, insira uma idade maior ou igual a 18: "))
        self.idade = idade
    
    def get_idade(self):
        return self.idade


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.__salario = salario
    
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, salario):
        self.__salario = salario
    
    def calcular_salario_anual(self):
        return self.__salario * 12


class Departamento:
    def __init__(self):
        self.funcionarios = []
    
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def calcular_total_salarios(self):
        total = 0
        for funcionario in self.funcionarios:
            total += funcionario.calcular_salario_anual()
        return total
    
    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f"Nome: {funcionario.nome}, Salário Anual: R${funcionario.calcular_salario_anual()}")


departamento = Departamento()


p1 = Funcionario("João", 22, 4000)
p2 = Funcionario("Helo", 17, 2000)
p3 = Funcionario("Francisca", 25, 1560)


departamento.adicionar_funcionario(p1)
departamento.adicionar_funcionario(p2)
departamento.adicionar_funcionario(p3)


departamento.listar_funcionarios()
print(f"Total de salários anuais: R${departamento.calcular_total_salarios()}")