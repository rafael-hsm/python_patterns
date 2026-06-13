from datetime import datetime
from pprint import pprint

class Pessoa:

    def __init__(self: object, nome: str):
        self.__nome = nome
        self.__nascimento = datetime.now()  # now.year, now.month, now.day, now.hour, now.minute, now.second
    
    def str(self: object) -> str:
        """Retorna uma representação em string do objeto Pessoa."""
        return f"Pessoa(nome={self.__nome}), nascimento={self.__nascimento})"
    
    def __repr__(self: object) -> str:
        """Retorna uma representação oficial do objeto Pessoa."""
        return self.str()


class Carro:
    
    def __init__(self: object, is_sedan: bool = False):
        self.__is_sedan = is_sedan
        self.__velocidade = 0
        self.__motorista = None
    
    def dirigir(self: object, motorista: Pessoa):
        self.__motorista = motorista
        self.acelerar(1)

    def acelerar(self: object, velocidade: int):
        self.__velocidade += velocidade
    
    def parar(self: object):
        self.__velocidade = 0


if __name__ == "__main__":
    pessoa1 = Pessoa("João")
    carro1 = Carro()
    carro1.dirigir(pessoa1)
    pprint(carro1.__dict__, indent=4)
    pprint(pessoa1.__dict__, indent=4)
    print("***" * 10)
    pessoa2 = Pessoa("Maria")
    print(pessoa2.__dict__)
