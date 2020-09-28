# Console Sea-Battle by SimplyProgger




class Player:

	def __init__(self):

		self.player_field = self.createField()
		self.ship_4_cell = 1
		self.ship_3_cell = 2
		self.ship_2_cell = 3
		self.ship_1_cell = 4



	def createField(self):
		self.top_margin = [' ', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И' ,'К']
		player_field = [['~' for i in range(10)] for j in range(10)]

		for i in range(10):
			list_pred = player_field[i]
			new_list = [i] + list_pred
			player_field[i] = new_list
			
		pred_list = player_field
		player_field = [self.top_margin] + pred_list

		return player_field


	def buildField(self, ship, name, x, y, x1, y1):
		if ship != 0:
			margin_index = self.top_margin.index(x)
			margin_index1 = self.top_margin.index(x1)
			if name == 'ship_4_cell':
				if abs(y - y1) == 4 and abs(margin_index - margin_index1) == 0 or abs(y - y1) == 0 and abs(margin_index - margin_index1) == 4:
					if y1 > y:
						count = 0
						for _ in range(5):
							count = 0
							self.player_field[y + 1][margin_index] = '#'
							y += 1

					elif y > y1:
						count = 0
						for _ in range(5):
							count = 0
							self.player_field[y + 1][margin_index] = '#'
							y -= 1


				else:
					return 'Введены неверные координаты построения'



	def getTheNumberOfShips(self):
		
		output = [f'Всего 4 местных кораблей: {self.ship_4_cell}', f'Всего 3 местных кораблей: {self.ship_3_cell}',
			 f'Всего 2 местных кораблей: {self.ship_2_cell}', f'Всего 1 местных кораблей: {self.ship_1_cell}']


		return output




player1 = Player()
player1.buildField(player1.ship_4_cell, 'ship_4_cell', 'В', 5, 'В', 9)
for i in player1.getTheNumberOfShips():
	print(i)
for i in player1.player_field:
	print(' '.join([str(j) for j in i]))