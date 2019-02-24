class Cliente
		require 'date'
	attr_accessor :nome
	attr_accessor :cpf
	attr_accessor :id
	attr_accessor :dthratualizacao
	
	def initialize(h)
		@nome  	= h[:nome]||h["nome"]
		@cpf = (h[:cpf]||h["cpf"]).to_i
	
		@dthratualizacao = Time.now
		@id = (h[:id]||h["id"]).to_i if h[:id]||h["id"]
	end

	def to_s
		"Cliente : id :#{@id}, nome: #{@nome}, cpf : #{@cpf}"
	end

	def to_a
		v = []
		v << @id if @id
		v << @nome
		v << @cpf
		v << @dthratualizacao
	
	end

	

end
