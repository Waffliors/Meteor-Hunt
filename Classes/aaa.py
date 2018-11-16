import pickle
import Classes.Score as Score

chamaMetodo = Score.Ranking('', 0)


inFile = open('save.pkl', 'rb')
listaDeRankings = pickle.load(inFile)
print(listaDeRankings)