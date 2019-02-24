from persistencia import *
from modelo import *
serieDAO = SerieDAO()
spoilerDAO = SpoilerDAO()
tam = 0
maior = 0
menor = 1
aux = 0
escolha = int(input('''
   Menu
1 - Cria Serie
2 - Cria Spoiler
3 - Listar Spoiler
4 - Listar Serie
5 - Apagar Serie
6 - Apagar Spoiler
7 - Alterar Serie
8 - Alterar Spoiler
9 - Detalhar Serie
10 - Serie com mais Spoilers
11 - Serie com meno Spoilers
12 - Cria arquivo
13 - Altera serie por spoiler
Escolha: '''))
if escolha == 1:
	nome = raw_input("Digite o nome da serie:")
	print nome;
	quantidadetemp = input("Digite o total de temporadas:")
	print quantidadetemp
	quantidadeep = input("Digite o total de episodios:")
	print quantidadeep
	data = raw_input("Digite a data da serie (dd-mm-aa):")
	print data
	serie = Serie(nome,quantidadetemp, quantidadeep,data)
	serieDAO = SerieDAO()
	serieDAO.adicionar(serie)
if escolha == 2:
	descricao = raw_input("Digite a descricao do spoiler:")
	#print descricao;
	episodio = input("Digite o episodio:")
	#print episodio
	data = raw_input("Digite a data (dd-mm-aa):")
	#print data
	datamodificacao = raw_input("Digite a data da modificacao (dd-mm-aa):")
	#print datamodificacao
	id_serie = raw_input("Digite o id da serie que esse spoiler acontece:")
	#print id_serie
	spoiler = Spoiler(descricao, episodio, data, datamodificacao, id_serie )
	spoilerDAO = SpoilerDAO()
	spoilerDAO.adicionar(spoiler)
	#spoilerDAO.adicionarSerie(spoiler, serie)
if escolha == 3:
	vet = spoilerDAO.listar()
	#print vet
	for spoiler in vet:
		print "Id:"
		#print vet[0]
		print spoiler.id_spoiler
		print "Descricao:"
		#serie = vet[1].split("-")
		#print vet[1]
		
		#print serie
		descricao = spoiler.descricao
		print descricao
		print "Episodio:"
		episodio = spoiler.episodio
		print episodio
		print "Data:"
		data = spoiler.data
		print data
		print "Data Modificacao:"
		datam = spoiler.datamodificacao
		print datam
		print "Serie"
		serie = spoilerDAO.nomeSerie(spoiler.serie)
		print serie
if escolha == 4:
	vet = serieDAO.listar()
	#print vet
	for serie in vet:
		print "Id:"
		#print vet[0]
		print serie.id_serie
		print "Nome:"
		#serie = vet[1].split("-")
		#print vet[1]
		
		#print serie
		nome = serie.nome
		print nome
		print "Quantidade de temporada:"
		quantidadetemp = serie.quantidadetemp
		print quantidadetemp
		print "Quantidade de episodio:"
		quantidadeep = serie.quantidadeep
		print quantidadeep
		print "Data:"
		data = serie.data
		print data
if escolha == 5:
	id_serie = raw_input("Digite o id da serie que voce deseja apagar:")
	serieDAO.excluir(id_serie)

if escolha == 6:
	id_spoiler = raw_input("Digite o id do spoiler que voce deseja apagar:")
	spoilerDAO.excluir(id_spoiler)

if escolha == 7:
	id_serie = raw_input("Digite o id da serie que voce deseja alterar:")
	novonome = raw_input("Digite o novo nome da serie:")
	quantidadeep = raw_input("Digite a quantidadeep:")
	quantidadetemp = raw_input("Digite a quantidadetemp:")
	data = raw_input("Digite a nova data (dd-mm-aa) :")
	serie = Serie(novonome,quantidadetemp, quantidadeep,data)
	serieDAO = SerieDAO()
	serieDAO.editar(serie, id_serie)


if escolha == 8:
	id_spoiler = raw_input("Digite o id do spoiler que voce deseja alterar:")
	novadescricao = raw_input("Digite a nova descricao do spoiler:")
	episodio = raw_input("Digite o episodio:")
	data = raw_input("Digite a nova data (dd-mm-aa) :")
	datamodificacao = raw_input("Digite a data da modificacao (dd-mm-aa) :")
	id_serie = raw_input("Digite o novo id da serie:")
	spoiler = Spoiler(novadescricao,episodio, data, datamodificacao, id_serie, id_spoiler)
	spoilerDAO = SpoilerDAO()
	spoilerDAO.editar(spoiler, id_spoiler)

if escolha == 9:
	vet = serieDAO.listar()
	for serie in vet:
		print "Id serie:"
		#print vet[0]
		print serie.id_serie
		print "Nome:"
		#serie = vet[1].split("-")
		#print vet[1]
		
		#print serie
		nome = serie.nome
		print nome
		print "Quantidade de temporada:"
		quantidadetemp = serie.quantidadetemp
		print quantidadetemp
		print "Quantidade de episodio:"
		quantidadeep = serie.quantidadeep
		print quantidadeep
		print "Data:"
		data = serie.data
		print data
		print "Spoilers"
		vets = spoilerDAO.listarPSerie(serie.id_serie)
		for spoiler in vets:
			
			print "Id:"
		#print vet[0]
			print spoiler.id_spoiler
			print "Descricao:"
		#serie = vet[1].split("-")
		#print vet[1]
		
		#print serie
			descricao = spoiler.descricao
			print descricao
			print "Episodio:"
			episodio = spoiler.episodio
			print episodio
			print "Data:"
			data = spoiler.data
			print data
			print "Data Modificacao:"
			datam = spoiler.datamodificacao
			print datam
	
	#	print vet[2]
	#	print vet[3]
	#	print vet[4]

if escolha == 10:
	spoilerDAO.maior()

if escolha == 11:
	spoilerDAO.menor()

if escolha == 12:
	serieDAO.cria()
	spoilerDAO.cria()

if escolha == 13:
	spoiler = raw_input("Digite o id do spoiler:")
	id_serie = spoilerDAO.procuraSerie(spoiler)
	#print id_serie
	novonome = raw_input("Digite o novo nome da serie:")
	quantidadeep = raw_input("Digite a quantidadeep:")
	quantidadetemp = raw_input("Digite a quantidadetemp:")
	data = raw_input("Digite a nova data (dd-mm-aa) :")
	serie = Serie(novonome,quantidadetemp, quantidadeep,data)
	serieDAO = SerieDAO()
	serieDAO.editar(serie, id_serie)
#	vet = serieDAO.listar()
#	vetid= []
#	for serie in vet:
		#print serie.id_serie
#		id = serie.id_serie
		#print id
#		vetid.append(id)
#		print vetid


#		vets = spoilerDAO.listarPSerie(serie.id_serie)
#		tam = len(vets)
#		print tam

#		if(tam > maior):
#			maior = tam
#		if(tam < menor):
#			menor = tam
#	vets = spoilerDAO.listar()
#	print vets
#	for spoiler in vet:
#		for ide in vetid:
#			print spoiler.serie
			#if(spoiler.serie == ide):
			#	aux = aux + 1
			#	vett.append(ide)
			#	vett.append(aux)
#	print "Serie com mais spoiler:"
#	print vett