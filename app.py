from src.resolvedor import resolver
from src.gerador import gerar


if __name__ == "__main__":
    labirinto, posicao_inicial = gerar()

    resolver(posicao_inicial, labirinto)