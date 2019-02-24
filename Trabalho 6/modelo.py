
class Jornalista:
	def __init__(self, login="",  senha="", nome="", id = 0 ):
		self.login = login
		self.senha = senha
		self.nome = nome	
		self.id = id
		
		
	def __repr__(self):
		return self.login + ";" + self.nome + ";" + self.senha 

class Assunto:
	def __init__(self, nome="", id=0):
		self.nome = nome
		self.id =id
	def __repr__(self):
		return self.nome + ";" + str(self.id)

class Comentario:
	def __init__(self, texto="", data="", leitor=0,noticia=0, id=0 ):
		self.texto = texto
		self.data = data
		self.leitor = leitor
		self.noticia = noticia
		self.id = id
	def __repr__(self):
		return self.texto + ";"+ str(self.data)+";"+str(self.leitor)+";"+str(self.noticia)

class Leitor:
	def __init__(self, login="",  senha="", nome="", id = 0 ):
		self.login = login
		self.senha = senha
		self.nome = nome	
		self.id = id
		
		
	def __repr__(self):
		return self.login + ";" + self.nome + ";" + self.senha 

class Noticia:
	def __init__(self,titulo="", texto="", data="", assunto="", jornalista="", id=0 ):
		self.titulo = titulo
		self.texto = texto
		self.data = data
		self.assunto = assunto
		self.jornalista = jornalista
		self.id = id


	def __repr__(self):
		return self.titulo+";"+self.texto+";"+str(self.data)+";"+str(self.assunto)