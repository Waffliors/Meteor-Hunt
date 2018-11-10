import pickle

score = 300 # veio do main
player = "aaa" # tbm veio do main
listaDeRankings = []

class Ranking(object):

    def __init__(self, nome, pontos):
        self.__nome = nome
        self.__pontos = pontos

    def __repr__(self):
        return "%s %s" % (self.__nome, self.__pontos)

    def get_nome(self):
        return self.__nome

    def get_pontos(self):
        return self.__pontos

    def poeNaLista(self, rank):
        listaDeRankings.append(self)



rank = Ranking(player, score)
print(rank)
