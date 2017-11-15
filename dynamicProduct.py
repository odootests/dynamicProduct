from openerp import models, fields, api

class Dynamic_product_template(models.Model):
	_name = 'product.template'
	_inherit = 'product.template'

	ring_spun_count = fields.Integer('Ring spun count')
	twist_count = fields.Integer('Twist Count')
	compact_state = fields.Selection([('Compact', 'Compact'),('', 'Not Compact')],'Compact')
	process = fields.Selection([('Carded', 'Carded'),('Combed', 'Combed'),('-', 'None')],'Process')
	trade_name = fields.Selection([('100% Cotton', '100% Cotton'),('Cotton Melange', 'Cotton Melange'),('Grey Mellange', 'Grey Mellange'),('CVC', 'CVC'),('PC', 'PC'),('Siro', 'Siro'), ('Inject', 'Inject'), ('Cotton Modal', 'Cotton Modal'), ('Cotton Tencel', 'Cotton Tencel'), ('Cotton Linen', 'Cotton Linen'), ('100% Viscose', '100% Viscose'), ('100% Modal', '100% Modal'), ('100% Tencel', '100% Tencel'), ('100% Polyester', '100% Polyester')],'Trade Name')
	slub = fields.Selection([('-', 'No Slub'),('Slub', 'Slub')],'Slub')
	cotton_percentage = fields.Integer('Cotton %')
	cotton_type = fields.Selection([('Organic', 'Organic'),('BCI', 'BCI'),('Conventional', 'Conventional')],'Cotton Type')

	dyed_cotton_percentage = fields.Integer('Dyed Cotton %')
	white_viscose_percentage = fields.Integer('White Viscose %')
	dyed_viscose_percentage = fields.Integer('Dyed Viscose %')
	polyester_percentage = fields.Integer('Polyester %')
	linen_percentage = fields.Integer('Linen %')
	tencel_percentage = fields.Integer('Tencel %')
	modal_percentage = fields.Integer('Modal %')

	contamination = fields.Selection([('Contamination Free', 'Free'),('', 'None')],'Contamination')
	popularity = fields.Selection([('Normal', 'Normal'),('Popular', 'Popular')],'Popularity')
	yarn_process = fields.Selection([('Ring', 'Ring'),('Open End', 'Open End'),('Vortex', 'Vortex')],'Yarn Process')

	@api.depends('ring_spun_count','twist_count','compact_state','process','trade_name','slub','cotton_percentage','cotton_type','dyed_cotton_percentage','linen_percentage','tencel_percentage','modal_percentage','contamination','popularity','yarn_process', 'dyed_cotton_percentage', 'white_viscose_percentage', 'dyed_viscose_percentage', 'polyester_percentage', 'linen_percentage', 'tencel_percentage', 'modal_percentage')

	def concatenate_custom_fields(self):
       
		if str(self.trade_name) == '100% Cotton' or str(self.trade_name) == '100% Viscose' or str(self.trade_name) == '100% Modal' or str(self.trade_name) == '100% Tencel' or str(self.trade_name) == '100% Polyester':
			self.combined_name = str(self.ring_spun_count) + '/' + str(self.twist_count) + ' ' + str(self.compact_state) + ' ' + str(self.process) + ' ' + str(self.trade_name) + ' ' + str(self.slub) + ' ' + str(self.contamination) + ' ' + str(self.yarn_process)
			self.name= self.combined_name
		else:
			if self.dyed_cotton_percentage:
				self.combined_name = str(self.ring_spun_count) + '/' + str(self.twist_count) + ' ' + str(self.compact_state) + ' ' + str(self.process) + ' ' + str(self.trade_name) + ' ' + str(self.slub) + ' (Cotton ' + str(self.cotton_percentage) + '%-' + str(self.cotton_type) + ' + Dyed Cotton ' + str(self.dyed_cotton_percentage) + '%' + ') ' + str(self.contamination) + ' ' + str(self.yarn_process)
				self.name= self.combined_name

			elif self.white_viscose_percentage:
				self.combined_name = str(self.ring_spun_count) + '/' + str(self.twist_count) + ' ' + str(self.compact_state) + ' ' + str(self.process) + ' ' + str(self.trade_name) + ' ' + str(self.slub) + ' (Cotton ' + str(self.cotton_percentage) + '%-' + str(self.cotton_type) + ' + White Viscose ' + str(self.white_viscose_percentage) + '%' + ') ' + str(self.contamination) + ' ' + str(self.yarn_process)
				self.name= self.combined_name

			elif self.dyed_viscose_percentage:
				self.combined_name = str(self.ring_spun_count) + '/' + str(self.twist_count) + ' ' + str(self.compact_state) + ' ' + str(self.process) + ' ' + str(self.trade_name) + ' ' + str(self.slub) + ' (Cotton ' + str(self.cotton_percentage) + '%-' + str(self.cotton_type) + ' + Dyed Viscose' + str(self.dyed_viscose_percentage) + '%' + ') ' + str(self.contamination) + ' ' + str(self.yarn_process)
				self.name= self.combined_name

			elif self.polyester_percentage:
				self.combined_name = str(self.ring_spun_count) + '/' + str(self.twist_count) + ' ' + str(self.compact_state) + ' ' + str(self.process) + ' ' + str(self.trade_name) + ' ' + str(self.slub) + ' (Cotton ' + str(self.cotton_percentage) + '%-' + str(self.cotton_type) + ' + Polyster ' + str(self.polyester_percentage) + '%' + ') ' + str(self.contamination) + ' ' + str(self.yarn_process)
				self.name= self.combined_name

			elif self.linen_percentage:
				self.combined_name = str(self.ring_spun_count) + '/' + str(self.twist_count) + ' ' + str(self.compact_state) + ' ' + str(self.process) + ' ' + str(self.trade_name) + ' ' + str(self.slub) + ' (Cotton ' + str(self.cotton_percentage) + '%-' + str(self.cotton_type) + ' + Linen ' + str(self.linen_percentage) + '%' + ') ' + str(self.contamination) + ' ' + str(self.yarn_process)
				self.name= self.combined_name

			elif self.tencel_percentage:
				self.combined_name = str(self.ring_spun_count) + '/' + str(self.twist_count) + ' ' + str(self.compact_state) + ' ' + str(self.process) + ' ' + str(self.trade_name) + ' ' + str(self.slub) + ' (Cotton ' + str(self.cotton_percentage) + '%-' + str(self.cotton_type) + ' + Tencel ' + str(self.tencel_percentage) + '%' + ') ' + str(self.contamination) + ' ' + str(self.yarn_process)
				self.name= self.combined_name

			elif self.modal_percentage:
				self.combined_name = str(self.ring_spun_count) + '/' + str(self.twist_count) + ' ' + str(self.compact_state) + ' ' + str(self.process) + ' ' + str(self.trade_name) + ' ' + str(self.slub) + ' (Cotton ' + str(self.cotton_percentage) + '%-' + str(self.cotton_type) + ' + Modal ' + str(self.modal_percentage) + '%' + ') ' + str(self.contamination) + ' ' + str(self.yarn_process)
				self.name= self.combined_name
		
			else:
				self.combined_name = str(self.ring_spun_count) + '/' + str(self.twist_count) + ' ' + str(self.compact_state) + ' ' + str(self.process) + ' ' + str(self.trade_name) + ' ' + str(self.slub) + ' (Cotton ' + str(self.cotton_percentage) + '%-' + str(self.cotton_type) + ') ' + str(self.contamination) + ' ' + str(self.yarn_process)
				self.name= " "	

	combined_name = fields.Char(compute=concatenate_custom_fields,store=True)
