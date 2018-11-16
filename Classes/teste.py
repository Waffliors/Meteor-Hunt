import pickle
import Classes.Score as Score

chamaMetodo = Score.Ranking('', 0)


inFile = open('save.pkl', 'rb')
listaDeRankings = pickle.load(inFile)

listaDeRankings = chamaMetodo.resetSave(listaDeRankings)
print(listaDeRankings)

rank = Score.Ranking('aaa', 123)
chamaMetodo.poeNaLista(rank, listaDeRankings)
print(listaDeRankings)
listaDeRankings = chamaMetodo.arruma(listaDeRankings)
print(listaDeRankings)

chamaMetodo.save(listaDeRankings)

'''

#listaDeRankings = sorted(listaDeRankings, key = Score.Ranking.get_pontos, reverse=True)
#teste = Score.Ranking('', 0)
listaDeRankings = chamaMetodo.arruma(listaDeRankings)


print(listaDeRankings)'''




