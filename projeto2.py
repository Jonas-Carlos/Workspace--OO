from math import sqrt, pi

class Cubo:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return 6 * self.lado * self.lado

    def calcular_perimetro(self):
        return 12 * self.lado

class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura

    def calcular_perimetro(self):
        return 2 * (self.comprimento + self.largura)

class Cilindro:
    def __init__(self, raio_base, altura):
        self.raio_base = raio_base
        self.altura = altura

    def calcular_area(self):
        return 2 * pi * self.raio_base * (self.raio_base + self.altura)

    def calcular_perimetro(self):
        return 2 * pi * self.raio_base

class Piramide:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * (self.base + sqrt((self.altura**2) + (self.base/2)**2))

    def calcular_perimetro(self):
        # Considerando que a pirâmide é uma pirâmide de base retangular
        return 4 * self.base

def main():
    print("Escolha o sólido a ser calculado:")
    print("1. Cubo")
    print("2. Retângulo")
    print("3. Cilindro")
    print("4. Pirâmide")

    escolha = int(input("Digite o número correspondente ao sólido desejado: "))

    if escolha == 1:
        lado = float(input("Digite o lado do Cubo: "))
        cubo = Cubo(lado)
        print("Área do Cubo:", cubo.calcular_area())
        print("Perímetro do Cubo:", cubo.calcular_perimetro())

    elif escolha == 2:
        comprimento = float(input("Digite o comprimento do Retângulo: "))
        largura = float(input("Digite a largura do Retângulo: "))
        retangulo = Retangulo(comprimento, largura)
        print("Área do Retângulo:", retangulo.calcular_area())
        print("Perímetro do Retângulo:", retangulo.calcular_perimetro())

    elif escolha == 3:
        raio_base = float(input("Digite o raio da base do Cilindro: "))
        altura = float(input("Digite a altura do Cilindro: "))
        cilindro = Cilindro(raio_base, altura)
        print("Área do Cilindro:", cilindro.calcular_area())
        print("Perímetro da base do Cilindro:", cilindro.calcular_perimetro())

    elif escolha == 4:
        base_piramide = float(input("Digite o comprimento da base da Pirâmide: "))
        altura_piramide = float(input("Digite a altura da Pirâmide: "))
        piramide = Piramide(base_piramide, altura_piramide)
        print("Área da Pirâmide:", piramide.calcular_area())
        print("Perímetro da base da Pirâmide:", piramide.calcular_perimetro())

    else:
        print("Escolha inválida. Por favor, escolha um número válido.")

if __name__ == "__main__":
    main()
