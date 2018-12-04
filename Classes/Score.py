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

    def poeNaLista(self):
        listaDeRankings[5] = rank

    def printaLista(self):
        #
        #
        # SUBSTITUIR PELO PRINT NO PYGAME DPS
        # COM BLIT, UPDATE ETC
        #
        #
        i = 0
        while i < 5:
            print(listaDeRankings[i])
            i = i + 1



rank = Ranking("Vazio", 00000)
listaDeRankings = [rank, rank, rank, rank, rank, rank]
outFile = open('save.txt', 'wb')
pickle.dump(listaDeRankings, outFile)
outFile.close()


score = 300 # veio do main
player = "aza" # tbm veio do main
rank = Ranking(player, score)
Ranking.poeNaLista(rank)
listaDeRankings = sorted(listaDeRankings, key=Ranking.get_pontos, reverse=True)
#print(listaDeRankings)
'''
rank = Ranking('mbc', 150)
Ranking.poeNaLista(rank)
listaDeRankings = sorted(listaDeRankings, key=Ranking.get_pontos, reverse=True)
#print(listaDeRankings)

rank = Ranking('jjj', 2000)
Ranking.poeNaLista(rank)

listaDeRankings = sorted(listaDeRankings, key=Ranking.get_pontos, reverse=True)
#print(listaDeRankings)

#Main
nome = 'awe'
score = 300
rank = Ranking(nome, score)

#Ranking.printaLista(listaDeRankings)
Ranking.poeNaLista(rank)
listaDeRankings = sorted(listaDeRankings, key=Ranking.get_pontos, reverse=True)
#print('----')
#Ranking.printaLista(listaDeRankings)

rank = Ranking('Joao', 9000)
#Ranking.printaLista(listaDeRankings)
Ranking.poeNaLista(rank)
listaDeRankings = sorted(listaDeRankings, key=Ranking.get_pontos, reverse=True)
#print('----')
#Ranking.printaLista(listaDeRankings)

rank = Ranking('bb', 10)
#Ranking.printaLista(listaDeRankings)
Ranking.poeNaLista(rank)
listaDeRankings = sorted(listaDeRankings, key=Ranking.get_pontos, reverse=True)
#print('----')
#Ranking.printaLista(listaDeRankings)

outFile = open('save.txt', 'wb')
pickle.dump(listaDeRankings, outFile)
outFile.close()'''
