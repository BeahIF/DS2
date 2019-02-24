class Quarto
		require 'date'
	attr_accessor :quant_pessoas

	attr_accessor :id
	attr_accessor :dthratualizacao
	
	def initialize(h)
		@quant_pessoas  	= h[:quant_pessoas]||h["quant_pessoas"]

		@dthratualizacao = Time.now
		@id = (h[:id]||h["id"]).to_i if h[:id]||h["id"]
	end


	def to_s
		"Quarto : id #{@id}: data da ultima atualizacao : #{@dthratualizacao}, numero de pessoas: #{@quant_pessoas}"
	end

	def to_a
		v = []
		v << @id if @id
		v << @quant_pessoas
		v << @dthratualizacao
	
	end

	

end
