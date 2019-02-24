require_relative("cliente.rb")
require_relative("clienteDAO.rb")
require_relative("quarto.rb")
require_relative("quartoDAO.rb")
require_relative("reserva.rb")
require_relative("reservaDAO.rb")

#QUARTOS
q1 = {quant_pessoas: 2}
quarto1 = Quarto.new q1
#q2 = {quant_pessoas: 4}
#quarto2 = Quarto.new q2
qdao = QuartoDAO.new
#p qdao.salvar(quarto1)
#p qdao.salvar(quarto2)

#quarto2 = qdao.get(3)
quarto1 = qdao.get(2)
q3 = {id: quarto1.id, quant_pessoas: 1}
#p quarto1
quarto3 = Quarto.new q3
p qdao.salvar(quarto3)

q4 = {quant_pessoas: 2}
quarto4 = Quarto.new q4
#p qdao.salvar(quarto4)
#p qdao.excluir(quarto1)
#puts "quarto"
quarto1 = qdao.get(8)
#qdao.excluir(quarto1)
#p qdao.listar

#CLIENTES
c1 = {nome: "aluno", cpf: "01977856041"}
cliente1 = Cliente.new c1
cdao = ClienteDAO.new
#p cdao.salvar(cliente1)
#cliente1 = cdao.get(2)
#p cdao.listar
c2 = {nome: "fulano", cpf: "01977856040"}
cliente2 = Cliente.new c2
#p cdao.salvar(cliente2)
#puts "cliente"
cliente1 = cdao.get(3)
#cliente1 = cdao.get(1)
#puts cliente1
#cdao.excluir(cliente1)

#RESERVAS
r1 = {  cliente: cliente1,quarto: quarto1, entrada: "28/09/2018", saida: "25/10/2018",valor:130.0, quant_pessoas: 3 }
reserva1 = Reserva.new r1
#p reserva1
rdao = ReservaDAO.new
p rdao.salvar(reserva1)
p rdao.listar
r2 = { cliente: cliente2, quarto:quarto4, entrada: "27/09/2018", saida: "26/10/2018", valor: 149.0, quant_pessoas: 2}
reserva2 = Reserva.new r2
#p rdao.salvar(reserva2)
reserva3 = rdao.get(2)
id = reserva3.id
r3 = {id:id, cliente: cliente2, quarto:quarto4, entrada: "28/09/2018", saida: "26/10/2018", valor: 148.0, quant_pessoas: 1}
reserva3 = Reserva.new r3
#rdao.salvar(reserva3)
#reserva4 = rdao.get(3)
#rdao.excluir(reserva4)