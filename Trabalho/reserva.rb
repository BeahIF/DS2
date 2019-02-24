class Reserva
		require 'date'
		require 'time'
	attr_accessor :quarto
	attr_accessor :cliente
	attr_accessor :id
	attr_accessor :dthratualizacao
	attr_accessor :valor
	attr_accessor :entrada
	attr_accessor :saida
	attr_accessor :quant_pessoas
	attr_accessor :salva
	def initialize(h)

		@id = (h[:id]||h["id"]).to_i if h[:id]||h["id"]
		#puts @id
		@quarto  	= h[:quarto]||h["quarto"]
		@cliente= (h[:cliente]||h["cliente"])
		#puts h[:entrada].class
		if(h[:entrada] == nil)
			@entrada = h[:entrada]||h["entrada"] 
		else 
			dia = h[:entrada][0..1]
		#			puts dia
			#@dia = dia
			mes = h[:entrada][3..4]
			#@mes = mes
			ano = h[:entrada][6..10]
			#@ano = ano
		entrada = Time.new(ano, mes, dia).to_date
		#puts entrada
		@entrada = entrada
		end	
		if(h[:saida] == nil)
			@saida = h[:saida]||h["saida"]
		else
			dia = h[:saida][0..1]
		#			puts dia
			#@dia = dia
			mes = h[:saida][3..4]
			#@mes = mes
			ano = h[:saida][6..10]
			#@ano = ano
		saida = Time.new(ano, mes, dia).to_date
		

		@saida = saida
		end
				@dthratualizacao = Time.now
		@valor  = (h[:valor]||h["valor"])
		#puts h[:quant_pessoas]
		@quant_pessoas = h[:quant_pessoas].to_i
		#puts @quant_pessoas
		if quarto.class != Quarto
			@quant_pessoas = h[:quant_pessoas]||h["quant_pessoas"]
		else
		teste = quarto.quant_pessoas.to_i
		#puts teste
		
		if @quant_pessoas <= teste
			@salva = true
		else 
			@salva = false
		end
		end
	end


	def to_s
		cdao = ClienteDAO.new
		cliente = cdao.get(@cliente)
	
		"Reserva :id #{@id}, cliente: #{cliente.nome}, quarto: #{@quarto}, data de entrada: #{@entrada}, data de saida: #{@saida}, valor pago: #{@valor}, quantidade de pessoas: #{@quant_pessoas}"
	end

	def to_a
		v = []
		v << @id if @id
		v << @cliente.id
		v << @quarto.id
		v << @entrada
		v << @saida
		v << @valor
		v << @quant_pessoas
		v << @dthratualizacao
		
	end

	

end
