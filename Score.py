import pickle

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

    def poeNaLista(self, listaDeRankings):
        listaDeRankings[5] = self
        outFile = open('save.pkl', 'wb')
        pickle.dump(listaDeRankings, outFile)
        return listaDeRankings

    def resetSave(self, listaDeRankings):
        rank = Ranking(" ", 00000000)
        listaDeRankings = [rank, rank, rank, rank, rank, rank]
        outFile = open('save.pkl', 'wb')
        pickle.dump(listaDeRankings, outFile)
        return listaDeRankings

    def arrumaLista(self, listaDeRankings):
        listaDeRankings = sorted(listaDeRankings, key = Ranking.get_pontos, reverse = True)
        outFile = open('save.pkl', 'wb')
        pickle.dump(listaDeRankings, outFile)
        return listaDeRankings



