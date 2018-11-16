import pickle
import Constants


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

    def poeNaLista(self, rank, listaDeRankings):
        listaDeRankings[5] = rank
        return listaDeRankings

    def printaLista(self, font, background_image, listaDeRankings):
        Constants.screen.blit(background_image, [0, 0])
        primeiroLugar = font.render("Primeiro Lugar:" + str(listaDeRankings[0]), True, Constants.WHITE)
        Constants.screen.blit(primeiroLugar, [Constants.X / 2 - primeiroLugar.get_rect().size[0] / 2, Constants.Y / 3])
        segundoLugar = font.render("Segundo Lugar" + str(listaDeRankings[1]), True, Constants.WHITE)
        Constants.screen.blit(segundoLugar, [Constants.X / 2 - segundoLugar.get_rect().size[0] / 2, Constants.Y / 2])
        terceiroLugar = font.render("Terceiro Lugar:" + str(listaDeRankings[2]), True, Constants.WHITE)
        Constants.screen.blit(terceiroLugar, [Constants.X / 2 - terceiroLugar.get_rect().size[0] / 2, Constants.Y / 1.80])
        quartoLugar = font.render("Quarto Lugar:" + str(listaDeRankings[3]), True, Constants.WHITE)
        Constants.screen.blit(terceiroLugar, [Constants.X / 2 - quartoLugar.get_rect().size[0] / 2, Constants.Y / 1.30])
        quintoLugar = font.render("Quinto Lugar:" + str(listaDeRankings[4]), True, Constants.WHITE)
        Constants.screen.blit(terceiroLugar, [Constants.X / 2 - quintoLugar.get_rect().size[0] / 2, Constants.Y / 0.80])

    def save(self, listaDeRankings):
        outFile = open('Classes/save.pkl', 'wb')
        pickle.dump(listaDeRankings, outFile)
        outFile.close()

    def resetSave(self, listaDeRankings):
        rank = Ranking("Vazio", 00000)
        listaDeRankings = [rank, rank, rank, rank, rank, rank]
        outFile = open('Classes/save.pkl', 'wb')
        pickle.dump(listaDeRankings, outFile)
        outFile.close()
        return listaDeRankings


    def arruma(self, listaDeRankings):
        listaDeRankings = sorted(listaDeRankings, key=Ranking.get_pontos, reverse=True)
        return listaDeRankings
