#Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
c1 = Carro(modelo='Honda Civic', cor='Preto', ano=2018)

#Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    def __init__(self, nome, categoria, ativo, preco_medio, franqueado):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.preco_medio = preco_medio
        self.franqueado = franqueado

rest1 = Restaurante(nome='Outback', categoria='Steakhouse', ativo=True, preco_medio=3, franqueado=True)

# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

class Restaurante:
    def __init__(self, nome, categoria, preco_medio, franqueado, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.preco_medio = preco_medio
        self.franqueado = franqueado

rest2 = Restaurante(nome='Gennaro', categoria='Italiano')

#Adicione um método especial `__str__` à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

class Restaurante:
    def __init__(self, nome, categoria, preco_medio, franqueado, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.preco_medio = preco_medio
        self.franqueado = franqueado
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

rest3 = Restaurante(nome='Spoleto', categoria='Italiano')
print(rest3)

#Crie uma classe chamada `Cliente` e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self, nome, idade, telefone, email):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email

cl1 = Cliente(nome='Matheus', idade=20, telefone='985176967', email='matheusfilipedesilva@gmail.com')
cl2 = Cliente(nome='Shrek', idade=36, telefone='987654321', email='shrekdasilva@gmail.com')
cl3 = Cliente(nome='Gato de Botas', idade=26, telefone='123456789', email='enfrentemeseforcapaz@gmail.com')