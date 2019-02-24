import datetime
class Spoiler:

	def __init__(self, descricao, episodio, data, datamodificacao, serie, id_spoiler=0):
		self.descricao = descricao
		self.episodio = episodio
		self.data = data
		self.datamodificacao = datamodificacao
		self.serie = serie
		self.id_spoiler = id_spoiler
	

		# self.mes = mes

	def obj2CSV(self):
	 	return self.descricao + ";"+ str(self.episodio) + ";" + str(self.data) + ";" + str(self.datamodificacao) +";"+ str(self.serie) +";"+ str(self.id_spoiler)+";\n"

	# def csv2OBJ(self, linha):
	# 	aux = linha.strip().split(";")
	# 	return Aniversariante(aux[0], aux[1], int(aux[2]), int(aux[3]))

	def __repr__(self):
		return self.descricao + " - " + str(self.episodio) + " - " +  str(self.data) + " - " + str(self.datamodificacao) + " - " + str(self.serie)

class Serie:

	def __init__(self, nome, quantidadetemp, quantidadeep, data, id_serie = 0):
		self.nome = nome
		self.quantidadeep = quantidadeep
		self.quantidadetemp = quantidadetemp
		self.data = data
		self.id_serie = id_serie
		# self.mes = mes


	def obj2CSV(self):
	 	return self.nome + ";"+ str(self.quantidadetemp) + ";" + str(self.quantidadeep) + ";" + str(self.data) + str(self.id_serie)+";\n"

	# def csv2OBJ(self, linha):
	# 	aux = linha.strip().split(";")
	# 	return Aniversariante(aux[0], aux[1], int(aux[2]), int(aux[3]))

	def __repr__(self):
		return self.nome + " - " + str(self.quantidadeep) + " - " +  str(self.quantidadetemp) + " - " + str(self.data)
