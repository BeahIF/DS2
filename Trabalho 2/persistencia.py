from modelo import *
import os
import psycopg2

class SpoilerDAO:
	def listar(self):
		vetObj = []
		
		try:
			conn = psycopg2.connect("dbname=spoiler port=5432 host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			cur.execute("SELECT * FROM spoiler")
			vet = cur.fetchall()	
			for linha in vet:
				vetObj.append(Spoiler(linha[1],linha[2], linha[3], linha[4], linha[5], linha[0]))
			cur.close()
			conn.close()
		except Exception as e:
			print "Erro"
	
		return vetObj

	def nomeSerie(self, id_serie):
		try:
			conn = psycopg2.connect("dbname=spoiler port=5432 host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			cur.execute("SELECT * FROM serie")
			#print cur.rowcount
			vet = cur.fetchall()	
			for linha in vet:
				print linha[0]
				if(linha[0] == id_serie):
					nome = linha[1]
			cur.close()
			conn.close()
		except Exception as e:
			print "Erro"
		return nome	

	def listarPSerie (self, id_serie):
		vetObj = []
		try:
			#print "here"
			conn = psycopg2.connect("dbname=spoiler port=5432 host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			cur.execute("SELECT * FROM spoiler")
			#print cur.rowcount
			vet = cur.fetchall()	
		#	print vet		
			for linha in vet:

				#print linha[0]
				#print linha[1]
				#print linha[2]
				#print linha[3]
				#print linha[4]
				#print linha[5]
				if(linha[5] == id_serie):

			#	spoiler = Spoiler()
			#	spoiler = Spoiler(linha[1],linha[2], linha[3], linha[4], linha[5], linha[0])
			#	print spoiler
					vetObj.append(Spoiler(linha[1],linha[2], linha[3], linha[4], linha[5], linha[0]))
			cur.close()
			conn.close()
		except Exception as e:
			print "Erro"
	
		return vetObj		
	def carregar(self, id):
		# vetObj = []
		spoiler = Spoiler()
		try:
			conn = psycopg2.connect("dbname=spoiler port=5432 host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			cur.execute("SELECT * FROM spoiler WHERE id = %s", [id])
			linha = cur.fetchone()
			spoiler = Spoiler( linha[4], linha[3],linha[2], linha[1], int(linha[0]))
		except Exception as e:
			print "Erro"
		cur.close()
		conn.close()
		return spoiler


	def adicionar(self, spoiler):
		dat = spoiler.data
		separa = dat.split()
		#print(separa)
		dat = separa[0]
		#print(data)
		separadata = dat.split("-")
		#print(separadata)
		dia = int(separadata[0])
		mes = int(separadata[1])
		ano = int(separadata[2])
		#print(dia)
		#print(mes)
		#print(ano)
		validade = "true"
		i = 0
		while (validade == "true" and i == 0):
			#print("aqui")
    			if ((ano%4 == 0 and ano%100!= 0) or ano%400 == 0):
       				bissexto = "sim"
    			else:
        			bissexto = "nao"
				if (mes < 1 or mes > 12):	validade = "false"
				if dia > 31 or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30): 		validade = "false"
				if (mes == 2 and bissexto == "nao" and dia > 28) or ( mes == 2 and bissexto == "sim" and dia > 29): 	validade = "false"
    			i = i + 1
			if validade == "true":    			print("data valida! ") 
			else:
				print("data invalida! ") 
				exit()
		datam = spoiler.datamodificacao
		separa = datam.split()
	#	print(separa)
		datam = separa[0]
		#print(data)
		separadata = datam.split("-")
		#print(separadata)
		dia = int(separadata[0])
		mes = int(separadata[1])
		ano = int(separadata[2])
		#print(dia)
		#print(mes)
		#print(ano)
		validade = "true"
		i = 0
		while (validade == "true" and i == 0):
			#print("aqui")
    			if ((ano%4 == 0 and ano%100!= 0) or ano%400 == 0):
    	   			bissexto = "sim"
    			else:
        			bissexto = "nao"
				if (mes < 1 or mes > 12):	validade = "false"
				if dia > 31 or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30): 		validade = "false"
				if (mes == 2 and bissexto == "nao" and dia > 28) or ( mes == 2 and bissexto == "sim" and dia > 29): 	validade = "false"
   				i = i + 1
			if validade == "true":    			print("data valida! ")
			else:
				print("data invalida! ") 
				exit()
		try:
			conn = psycopg2.connect("dbname=spoiler  port=5432 host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			data = [spoiler.descricao, spoiler.episodio, spoiler.data, spoiler.datamodificacao, spoiler.serie]
			#print data
			cur.execute("INSERT INTO spoiler (descricao, episodio, data, datamodificacao, id_serie) VALUES ( %s, %s, %s, %s, %s);", data)
			# vet = cur.fetchall()			
			# for linha in vet:
				# vetObj.append(Aniversariante(linha[2], linha[1], int(linha[0])))
			conn.commit()	
			cur.close()
			conn.close()
		except Exception as e:
			print "Erro"
	
	# def listarMes(self,mes):
	# 	vet = self.listar()
	# 	for n in vet:
	# 		if n.mes == mes: 
	# 			print n.nome

	def excluir(self, id):
		try:
			conn = psycopg2.connect("dbname=spoiler port=5432 host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			cur.execute("DELETE FROM spoiler WHERE id_spoiler = %s", [id])
			conn.commit()	
			cur.close()
			conn.close()

		except Exception as e:
			print "Erro"
		
	def editar(self, spoiler, id_spoiler):
		try:
			conn = psycopg2.connect("dbname=spoiler port=5432 host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			#print spoiler.descricao
			#print id_spoiler
			cur.execute("UPDATE spoiler SET descricao = %s, episodio = %s , data = %s, datamodificacao = %s,  id_serie = %s WHERE id_spoiler = %s", [spoiler.descricao, spoiler.episodio, spoiler.data, spoiler.datamodificacao, spoiler.serie, spoiler.id_spoiler ])
			conn.commit()
			cur.close()
			conn.close()	
		except Exception as e:
			print "Erro"
	

	def adicionarSerie(self,spoilerzao, nome_serie):
		try:
			conn = psycopg2.connect("dbname=spoiler port=5432 host=localhost user=postgres password=postgres")
			print spoilerzao.descricao
			descricao = spoilerzao.descricao
			cur = conn.cursor()
			#cur.execute("SELECT descricao FROM spoiler WHERE (descricao = spoilerzao.descricao")
			cur.execute("SELECT * FROM serie")
			vet = cur.fetchall()			
			print vet
			for linha in vet:
				print linha[0]
				id_serie = linha[0]
				nome = linha[1]
				#print linha[2]
				#print linha[3]
				#print linha[4]
		#		serie=Serie(linha[1],linha[2], linha[3],linha[4])
		#		print serie
		#	for linha1 in vet1:
		#		print linha1[0]
		#		id_spoiler = linha1[0]
			#	print nome
				if(nome == nome_serie):
					#print "here"
					#cur.execute("SELECT descricao FROM spoiler WHERE (descricao = spoilerzao.descricao")
					cur.execute("INSERT INTO spoiler (id_serie) VALUES (%s) WHERE (spoiler.descricao = descricao);", id_serie)
			conn.commit()
			cur.close()
		#	cur1.close()
			conn.close()
		except Exception as e:
			print "Erro"

	def menor(self):
		try:			
			conn = psycopg2.connect("dbname=spoiler port=5432 host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			cur.execute("SELECT id_serie, count(id_serie), (select nome from serie where spoiler.id_serie = serie.id_serie) from spoiler group by id_serie order by count(id_serie)")
			vet = cur.fetchall()
			print vet
			for linha in vet:
				#print linha[0]

				print "Serie com menos spoiler e:"
				print linha[2]
				exit()
		#		maior = linha
		#	print vet[0][0]
		except Exception as e:
			print "Erro"

	def maior(self):
		try:			
			conn = psycopg2.connect("dbname=spoiler port=5432 host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			cur.execute("SELECT id_serie, count(id_serie), (select nome from serie where spoiler.id_serie = serie.id_serie) from spoiler group by id_serie order by count(id_serie) desc")
			vet = cur.fetchall()
			print vet
			for linha in vet:
				#print linha[0]

				print "Serie com mais spoiler e:"
				print linha[2]
				exit()
		#		maior = linha
		#	print vet[0][0]
		except Exception as e:
			print "Erro"

	def cria(self):
		vet = self.listar()
        #print vet
        	arquivo = open("spoiler.csv", "w")
	    	arquivo.close()
		for linha in vet:
			arquivo = open("spoiler.csv", "a")
			arquivo.write(linha.obj2CSV())
			arquivo.close()

	def procuraSerie(self, idspoiler):
		vet = self.listar()
		#print vet
		#print idspoiler
		resultado = 0
		for spoiler in vet:
			#print spoiler.id_spoiler
			id_spoiler = spoiler.id_spoiler
			if(int(id_spoiler) == int(idspoiler)):
			#	print spoiler.serie
				resultado = spoiler.serie
		return resultado

class SerieDAO:
	def __init(self):
		pass
	def listar(self):
		vetObj = []
		try:
			conn = psycopg2.connect("dbname=spoiler  port=5432 host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			cur.execute("SELECT * FROM serie")
		#	print cur.rowcount
			vet = cur.fetchall()			
			for linha in vet:
				
			#	vetObj.append(linha[0])
				vetObj.append(Serie(linha[1],linha[2], linha[3],linha[4], linha[0]))
			cur.close()
			conn.close()
		except Exception as e:
			print "Erro"
		
		return vetObj

	def carregar(self, id):
		# vetObj = []
		serie = Serie()
		try:
			conn = psycopg2.connect("dbname=spoiler host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			cur.execute("SELECT * FROM serie WHERE id = %s", [id])
			linha = cur.fetchone()
			serie = Serie(linha[5], linha[4], linha[3],linha[2], linha[1], int(linha[0]))
		except Exception as e:
			print "Erro"
		cur.close()
		conn.close()
		return serie


	def adicionar(self, serie):
		dat = serie.data
		separa = dat.split()
		#print(separa)
		dat = separa[0]
	#	print(data)
		separadata = dat.split("-")
	#	print(separadata)
		dia = int(separadata[0])
		mes = int(separadata[1])
		ano = int(separadata[2])
	#	print(dia)
	#	print(mes)
	#	print(ano)
		validade = "true"	
		i = 0
		while (validade == "true" and i == 0):
			#print("aqui")
    			if ((ano%4 == 0 and ano%100!= 0) or ano%400 == 0):
      				bissexto = "sim"
    			else:
    	   			bissexto = "nao"
				if (mes < 1 or mes > 12):	validade = "false"
				if dia > 31 or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30): 		validade = "false"
				if (mes == 2 and bissexto == "nao" and dia > 28) or ( mes == 2 and bissexto == "sim" and dia > 29): 	validade = "false"
    			i = i + 1
			if validade == "true":    			print("data valida! ")
			else:
				print("data invalida! ") 
				exit()
		try:
			conn = psycopg2.connect("dbname=spoiler port=5432 host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			data = [serie.nome, serie.quantidadeep, serie.quantidadetemp, serie.data]
			print data
			cur.execute("INSERT INTO serie (nome, quantidadeep, quantidadetemp, data) VALUES ( %s, %s, %s, %s);", data)
			# vet = cur.fetchall()			
			# for linha in vet:
				# vetObj.append(Aniversariante(linha[2], linha[1], int(linha[0])))
			conn.commit()
			cur.close()
			conn.close()	
		except Exception as e:
			print "Erro"


	def excluir(self, id):
		try:
			conn = psycopg2.connect("dbname=spoiler port=5432 host=localhost user=postgres password=postgres")
			#print id
			idserie = id
			print idserie
			cur = conn.cursor()
			cur.execute("BEGIN; DELETE FROM spoiler WHERE id_serie = %s; DELETE FROM serie WHERE id_serie = %s; COMMIT;", [id, id])
			conn.commit()	
			cur.close()
			conn.close()
		except Exception as e:
			print "Erro"

	def editar(self, serie, id_serie):
		try:
			conn = psycopg2.connect("dbname=spoiler port=5432 host=localhost user=postgres password=postgres")
			cur = conn.cursor()
			cur.execute("UPDATE serie SET nome = %s, quantidadetemp = %s , quantidadeep = %s, data = %s WHERE id_serie = %s", [serie.nome, serie.quantidadetemp, serie.quantidadeep, serie.data, id_serie])
			conn.commit()	
			cur.close()
			conn.close()
		except Exception as e:
			print "Erro"
		
	def cria(self):
		vet = self.listar()
		print vet
		arquivo = open("serie.csv", "w")
		arquivo.close()
		for linha in vet:

			arquivo = open("serie.csv", "a")
			arquivo.write(linha.obj2CSV())
			arquivo.close()

	
		
	
	

