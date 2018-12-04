import pickle

inFile = open('save.txt', 'rb')
listaDeRankings = pickle.load(inFile)
print(listaDeRankings)
inFile.close()
