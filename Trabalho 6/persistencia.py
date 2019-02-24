import psycopg2
from modelo import *
import sys
import os
class Conexao:
	def abre(self):
		self.conexao = psycopg2.connect("dbname=trabalho5 port=5432 user=postgres password=postgres host=localhost")
		self.cursor = self.conexao.cursor()
	
	def encerra(self):
		self.conexao.close()
		self.cursor.close()
 
class JornalistaDAO:
	
	def obter_nomes(self, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT nome FROM jornalista WHERe id = %s;", [id])
		linha = conexaoObj.cursor.fetchone()
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		return linha[0]
	
	def testa(self, login, senha):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT login, senha from jornalista")
		vet = conexaoObj.cursor.fetchall()
		for a in vet:
			print a[0]
			if(a[0] == login):
				if(a[1] == senha):
					return True
				else: 
					return False
		conexaoObj.conexao.commit()
		conexaoObj.encerra()

	#def testando(self, matricula):
	#	conexaoObj = Conexao()
	#	conexaoObj.abre()
	#	conexaoObj.cursor.execute("SELECT matricula from aluno")
	#	print "here"
	#	vet = conexaoObj.cursor.fetchall()
	#	print vet
	#	print(len(vet) == 0)
	#	if(len(vet) == 0):
	#		return True
	#	for a in vet:
	#		print "entro"
	#		print"lalal"
	#		print a[0]
	#		print matricula
	#		if(a[0] == matricula):
	#			return False
	#		else:
	#			return True
	#	conexaoObj.conexao.commit()
	#	conexaoObj.encerra()
	
	def adiciona(self, jornalista):
		print "adiciona"
		print jornalista
		conexaoObj = Conexao()

		conexaoObj.abre()
		print "conectou"
		conexaoObj.cursor.execute("INSERT INTO jornalista (login,senha, nome) VALUES( %s, %s, %s);", [jornalista.login, jornalista.senha, jornalista.nome])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
	def excluir(self, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		id = str(id)
		conexaoObj.cursor.execute("DELETE FROM jornalista WHERE id = %s;", [id])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()


		
	def obter(self, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT * FROM jornalista WHERE id = %s;", [id])
		linha = conexaoObj.cursor.fetchone()
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		jornalista = Jornalista()
		jornalista.id = int(linha[0])
		jornalista.login = str(linha[1])
		jornalista.senha  = str(linha[2])
		jornalista.nome = str(linha[3])
		

		return jornalista


	def obter_id(self, login):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT id FROM jornalista WHERE login = %s;", [login])
		linha = conexaoObj.cursor.fetchone()
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		jornalista = Jornalista()
		jornalista.id = int(linha[0])
		return linha[0]

	def obter_nome(self, login):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT nome FROM jornalista WHERE login = %s;", [login])
		linha = conexaoObj.cursor.fetchone()
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		return linha[0]
	def listar(self):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT * FROM jornalista")
		vet = conexaoObj.cursor.fetchall()
		vetJornalista = []
		print vet
		for registro in vet:
			print registro[0]
			jornalista = Jornalista()
			jornalista.id = registro[0]
			jornalista.login = registro[1]
			jornalista.nome = registro[3]
			vetJornalista.append(jornalista)
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		return vetJornalista

	def alterar(self, jornalista):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("UPDATE jornalista SET login = %s, senha = %s, nome=%s WHERE id = %s;", [jornalista.login, jornalista.senha, jornalista.nome, jornalista.id])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()

	def adicionarNome(self, aluno):
		conexaoObj = Conexao()
		conexaoObj.abre()
		cur.execute("INSERT INTO aluno (nome) VALUES (%s) RETURNING id;", [str(jogador.nome)])
		conn.commit()
		id = cur.fetchone()[0]
		cur.close()
		conn.close()
		return int(id)

class AssuntoDAO:
	
	#def testa(self, login, senha):
	#	conexaoObj = Conexao()
	#	conexaoObj.abre()
	#	conexaoObj.cursor.execute("SELECT login, senha from jornalista")
	#	vet = conexaoObj.cursor.fetchall()
	#	for a in vet:
	#		print a[0]
	#		if(a[0] == login):
	#			if(a[1] == senha):
	#				return True
	#			else: 
	#				return False
	#	conexaoObj.conexao.commit()
	#	conexaoObj.encerra()

	#def testando(self, matricula):
	#	conexaoObj = Conexao()
	#	conexaoObj.abre()
	#	conexaoObj.cursor.execute("SELECT matricula from aluno")
	#	print "here"
	#	vet = conexaoObj.cursor.fetchall()
	#	print vet
	#	print(len(vet) == 0)
	#	if(len(vet) == 0):
	#		return True
	#	for a in vet:
	#		print "entro"
	#		print"lalal"
	#		print a[0]
	#		print matricula
	#		if(a[0] == matricula):
	#			return False
	#		else:
	#			return True
	#	conexaoObj.conexao.commit()
	#	conexaoObj.encerra()
	
	def adiciona(self, assunto):
		#print "adiciona"
		#print jornalista
		conexaoObj = Conexao()

		conexaoObj.abre()
		#print "conectou"
		conexaoObj.cursor.execute("INSERT INTO assunto (nome) VALUES( %s);", [assunto.nome])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
	def excluir(self, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		id = str(id)
		conexaoObj.cursor.execute("DELETE FROM assunto WHERE id = %s;", [id])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()


		
	def obter(self, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT * FROM assunto WHERE id = %s;", [id])
		linha = conexaoObj.cursor.fetchone()
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		assunto = Assunto()
		assunto.id = int(linha[0])
		assunto.nome = str(linha[1])
		return assunto

	def listar(self):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT * FROM assunto")
		vet = conexaoObj.cursor.fetchall()
		vetAssunto = []
		print vet
		for registro in vet:
			nome = registro[1]
			print registro[1]
			vetAssunto.append(nome)
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		return vetAssunto

	def alterar(self, assunto):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("UPDATE assunto SET nome=%s WHERE id = %s;", [assunto.nome, assunto.id])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()

	def obter_nome(self, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT nome FROM assunto WHERE id=%s",[id])
		nome = conexaoObj.cursor.fetchone()
		print nome[0]
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		return nome[0]

class NoticiaDAO:
	
	def noticia_por_jornalista(self):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT id_jornalista, titulo FROM noticia")
		vet = conexaoObj.cursor.fetchall()
		vetNoticia = []
		for registro in vet:
			noticia = Noticia()
			noticia.titulo = registro[1]
			noticia.jornalista = JornalistaDAO().obter_nomes(registro[0])
			print noticia.jornalista
			vetNoticia.append(noticia)
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		return vetNoticia

	def id_assunto(self, nome):
		conexaoObj = Conexao()
		conexaoObj.abre()
		nome = str(nome)
		conexaoObj.cursor.execute("SELECT id FROM assunto WHERE nome=%s", [nome])
		id = conexaoObj.cursor.fetchone()
		#print id
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		return id[0]
	
	def adiciona(self, titulo, texto, data, id_assunto, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("INSERT INTO noticia (titulo, texto, data, id_assunto, id_jornalista) VALUES( %s, %s, %s, %s,%s);", [titulo, texto, data, id_assunto, id])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
	
	def excluir(self, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		id = str(id)
		conexaoObj.cursor.execute("DELETE FROM comentario WHERE id_noticia = %s;", [id])
		conexaoObj.cursor.execute("DELETE FROM noticia WHERE id = %s;", [id])

		conexaoObj.conexao.commit()
		conexaoObj.encerra()


		
	def obter(self, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT * FROM noticia WHERE id = %s;", [id])
		linha = conexaoObj.cursor.fetchone()
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		noticia = Noticia()
		noticia.id = int(linha[0])
		noticia.titulo = str(linha[1])
		noticia.texto  = str(linha[2])
		noticia.data = str(linha[3])
		noticia.id_assunto = str(linha[4])

		return noticia

	def listar(self):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT * FROM noticia")
		vet = conexaoObj.cursor.fetchall()
		vetNoticia = []
		print vet
		for registro in vet:
			print registro[0]
			noticia = Noticia()
			noticia.id = registro[0]
			noticia.titulo = registro[1]
			noticia.texto = registro[2]
			noticia.data = registro[3]
			noticia.assunto = AssuntoDAO().obter_nome(registro[4])

			vetNoticia.append(noticia)
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		return vetNoticia

	def alterar(self, noticia):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("UPDATE noticia SET titulo = %s, texto = %s, data=%s, id_assunto=%s WHERE id = %s;", [noticia.titulo, noticia.texto, noticia.data,noticia.assunto, noticia.id])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()

	def busca(self, valor):
		con = psycopg2.connect("host=localhost user=postgres password=ana dbname=trabalho6")
		cursor = con.cursor()
		cursor.execute("select * from noticia where titulo ilike %s", [valor + "%"])
		resultado = cursor.fetchone()
		if (resultado is None):
			return Noticia()
			cursor.close()
			con.close()
		else:
			cursor.close()
			con.close()
			return Noticia(resultado[1], resultado[2], int(resultado[0]))

	def busca2(self, valor):
		con = psycopg2.connect("host=localhost user=postgres password=postgres dbname=trabalho5")
		cursor = con.cursor()
		cursor.execute("select * from noticia where titulo ilike %s", [valor + "%"])
		vet = cursor.fetchall()
		vetNoticia = []
		for resultado in vet:
			vetNoticia.append(Noticia(resultado[1], resultado[2], int(resultado[0])))		
		cursor.close()
		con.close()		
		return vetNoticia
class LeitorDAO:
	
	def testa(self, login, senha):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT login, senha from leitor")
		vet = conexaoObj.cursor.fetchall()
		for a in vet:
			print a[0]
			if(a[0] == login):
				if(a[1] == senha):
					return True
				else: 
					return False
		conexaoObj.conexao.commit()
		conexaoObj.encerra()

	#def testando(self, matricula):
	#	conexaoObj = Conexao()
	#	conexaoObj.abre()
	#	conexaoObj.cursor.execute("SELECT matricula from aluno")
	#	print "here"
	#	vet = conexaoObj.cursor.fetchall()
	#	print vet
	#	print(len(vet) == 0)
	#	if(len(vet) == 0):
	#		return True
	#	for a in vet:
	#		print "entro"
	#		print"lalal"
	#		print a[0]
	#		print matricula
	#		if(a[0] == matricula):
	#			return False
	#		else:
	#			return True
	#	conexaoObj.conexao.commit()
	#	conexaoObj.encerra()
	
	def adiciona(self, leitor):
		print "adiciona"
		print leitor
		conexaoObj = Conexao()

		conexaoObj.abre()
		print "conectou"
		conexaoObj.cursor.execute("INSERT INTO leitor (login,senha, nome) VALUES( %s, %s, %s);", [leitor.login, leitor.senha, leitor.nome])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
	def excluir(self, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		id = str(id)
		conexaoObj.cursor.execute("DELETE FROM leitor WHERE id = %s;", [id])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()


		
	def obter(self, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT * FROM leitor WHERE id = %s;", [id])
		linha = conexaoObj.cursor.fetchone()
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		leitor = Leitor()
		leitor.id = int(linha[0])
		leitor.login = str(linha[1])
		leitor.senha  = str(linha[2])
		leitor.nome = str(linha[3])
		

		return leitor


	def obter_p(self, login):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT * FROM leitor WHERE login = %s;", [login])
		linha = conexaoObj.cursor.fetchone()
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		leitor = Leitor()
		leitor.id = int(linha[0])
		leitor.login = str(linha[1])
		leitor.nome = str(linha[3])
		

		return leitor

	def obter_id(self, login):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT id FROM leitor WHERE login = %s;", [login])
		linha = conexaoObj.cursor.fetchone()
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		leitor = Leitor()
		leitor.id = int(linha[0])
		return linha[0]


	def obter_nome(self, login):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT nome FROM leitor WHERE login = %s;", [login])
		linha = conexaoObj.cursor.fetchone()
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		return linha[0]

	def obter_nome_para_listar(self, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT nome FROM leitor WHERE id = %s;", [id])
		linha = conexaoObj.cursor.fetchone()
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		return linha[0]


	def listar(self):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT * FROM leitor")
		vet = conexaoObj.cursor.fetchall()
		vetJornalista = []
		print vet
		for registro in vet:
			print registro[0]
			leitor = Leitor()
			leitor.id = registro[0]
			leitor.login = registro[1]
			leitor.nome = registro[3]
			vetJornalista.append(leitor)
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		return vetLeitor

	def alterar(self, leitor):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("UPDATE leitor SET login = %s, senha = %s, nome=%s WHERE id = %s;", [leitor.login, leitor.senha, leitor.nome, leitor.id])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()


	def obter_nome_por_id(self, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT nome FROM leitor WHERE id=%s",[id])
		nome = conexaoObj.cursor.fetchone()
		print nome[0]
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		return nome[0]
	

class ComentarioDAO:
	
	def testa(self, login, senha):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT login, senha from leitor")
		vet = conexaoObj.cursor.fetchall()
		for a in vet:
			print a[0]
			if(a[0] == login):
				if(a[1] == senha):
					return True
				else: 
					return False
		conexaoObj.conexao.commit()
		conexaoObj.encerra()

	#def testando(self, matricula):
	#	conexaoObj = Conexao()
	#	conexaoObj.abre()
	#	conexaoObj.cursor.execute("SELECT matricula from aluno")
	#	print "here"
	#	vet = conexaoObj.cursor.fetchall()
	#	print vet
	#	print(len(vet) == 0)
	#	if(len(vet) == 0):
	#		return True
	#	for a in vet:
	#		print "entro"
	#		print"lalal"
	#		print a[0]
	#		print matricula
	#		if(a[0] == matricula):
	#			return False
	#		else:
	#			return True
	#	conexaoObj.conexao.commit()
	#	conexaoObj.encerra()
	
	def adiciona(self, comentario):
		print "adiciona"
		print comentario
		conexaoObj = Conexao()
		conexaoObj.abre()
		print "conectou"
		conexaoObj.cursor.execute("INSERT INTO comentario (texto,data, id_leitor, id_noticia) VALUES( %s, %s, %s, %s);", [comentario.texto, comentario.data, comentario.leitor, comentario.noticia])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
	def excluir(self, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		id = str(id)
		conexaoObj.cursor.execute("DELETE FROM comentario WHERE id = %s;", [id])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()


		
	def obter(self, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT * FROM comentario WHERE id = %s;", [id])
		linha = conexaoObj.cursor.fetchone()
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		comentario = Comentario()
		comentario.id = int(linha[0])
		comentario.texto = str(linha[1])
		comentario.data  = str(linha[2])
		comentario.leitor = LeitorDAO().obter_nome(linha[3])
		return comentario



	def obter_id(self, texto):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT id FROM comentario WHERE texto = %s;", [texto])
		linha = conexaoObj.cursor.fetchone()
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		comentario = comentario()
		comentario.id = int(linha[0])
		return linha[0]

	def obter_id_noticia(self, id):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT id_noticia FROM comentario WHERE id = %s;", [id])
		linha = conexaoObj.cursor.fetchone()
		conexaoObj.conexao.commit()
		conexaoObj.encerra()

		return linha[0]
	def listar(self):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("SELECT * FROM comentario")
		vet = conexaoObj.cursor.fetchall()
		vetComentario = []
		print vet
		for registro in vet:
			print registro[0]
			comentario = Comentario()
			comentario.id = registro[0]
			comentario.texto = registro[1]
			comentario.data = registro[2]
			comentario.leitor = LeitorDAO().obter_nome(linha[3])
			vetComentario.append(comentario)
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		return vetComentario

	def listar_por_noticia(self,id):
		print "entrei no listar_por_noticia"
		conexaoObj = Conexao()
		conexaoObj.abre()
		id = str(id)
		conexaoObj.cursor.execute("SELECT * FROM comentario WHERE id_noticia = %s ", [id])
		vet = conexaoObj.cursor.fetchall()
		#print vet
		vetComentario = []

		for registro in vet:
			comentario = Comentario()
			comentario.id = registro[0]
			comentario.texto = registro[1]
			comentario.data = registro[2]
		#	print LeitorDAO().obter_nome_para_listar(registro[3])
			comentario.leitor = LeitorDAO().obter_nome_para_listar(registro[3])
			comentario.noticia = registro[4]
		#	print comentario
			vetComentario.append(comentario)
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
		print vetComentario
		return vetComentario

	def alterar(self, comentario):
		conexaoObj = Conexao()
		conexaoObj.abre()
		conexaoObj.cursor.execute("UPDATE comentario SET texto = %s, data = %s, id_leitor=%s, id_noticia=%s WHERE id = %s;", [comentario.texto, comentario.data, comentario.id_leitor, comentario.id_noticia])
		conexaoObj.conexao.commit()
		conexaoObj.encerra()
	