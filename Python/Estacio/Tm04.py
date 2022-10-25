class Carro():
    def __init__(self, name, valor):
        self.nome = name;
        self.valor = valor;

    def Total(self):
        return self.valor.Preco()
    


class Valor():
    def __init__(self,valor,imposto, descontos):
        self.valor = valor;
        self.imposto = imposto;
        self.descontos = descontos;

    def Preco(self):
        return self.valor + self.imposto - self.descontos;


preco = Valor(16000,1076,300)
carro1 = Carro("BMW", preco);
print(carro1.nome, carro1.Total)
