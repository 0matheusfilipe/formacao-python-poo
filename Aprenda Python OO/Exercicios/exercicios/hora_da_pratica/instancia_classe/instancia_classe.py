#Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão.

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

#Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo.

    def __str__(self):
        status = "Ligado" if self._ligado else "Desligado"
        return f'{self.marca} | {self.modelo} | {self._ligado}'  
#Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.

class Carro(Veiculo): 
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

 #Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro    

    def __str__(self):
        status = 'Ligado' if self._ligado else 'Desligado'
        return f'{self.marca} | {self.modelo} | {self._ligado} - Portas: {self.portas}'

# 5- Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

# 6- Implemente o Método Especial __str__ na Classe Filha (Moto): Adicione um método especial __str__ à classe Moto que estenda o método da classe pai (Veiculo).

    def __str__(self):
        status = 'Ligado' if self._ligado else 'Desligado'
        return f'{self.marca} | {self.modelo} | {self._ligado} - Tipo: {self.tipo}'

# 7- Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.
