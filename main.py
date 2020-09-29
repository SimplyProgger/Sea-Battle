# Console Sea-Battle by SimplyProgger
from termcolor import colored



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
				if abs(y - y1) == 3 and abs(margin_index - margin_index1) == 0 or abs(y - y1) == 0 and abs(margin_index - margin_index1) == 3:
					if y1 > y:
						count = 0
						for _ in range(5):
							count = 0
							self.player_field[y + 1][margin_index] = colored('#', 'green')
							y += 1

					elif y > y1:
						count = 0
						for _ in range(5):
							count = 0
							self.player_field[y + 1][margin_index] = colored('#', 'green')
							y -= 1


					elif margin_index1 > margin_index:
						print('!')
						for i in range(margin_index, margin_index1 + 1):
							self.player_field[y + 1][i] = colored('#', 'green')

					elif margin_index > margin_index1:
						for i in range(margin_index1, margin_index + 1):
							self.player_field[y + 1][i] = colored('#', 'green')

			elif name == 'ship_3_cell':
				if abs(y - y1) == 2 and abs(margin_index - margin_index1) == 0 or abs(y - y1) == 0 and abs(margin_index - margin_index1) == 2:
					if y1 > y:
						count = 0
						for _ in range(3):
							count = 0
							self.player_field[y + 1][margin_index] = colored('#', 'green')
							y += 1

					elif y > y1:
						count = 0
						for _ in range(3):
							count = 0
							self.player_field[y + 1][margin_index] = colored('#', 'green')
							y -= 1


					elif margin_index1 > margin_index:
						for i in range(margin_index, margin_index1 + 1):
							self.player_field[y + 1][i] = colored('#', 'green')

					elif margin_index > margin_index1:
						for i in range(margin_index1, margin_index + 1):
							self.player_field[y + 1][i] = colored('#', 'green')


				else:
					return 'Введены неверные координаты построения'


			elif name == 'ship_2_cell':
				if abs(y - y1) + 1 == 2 and abs(margin_index - margin_index1 - 1) == 1 or abs(y - y1 + 1) == 1 and abs(margin_index - margin_index1) + 1 == 2:
					if y1 > y:
						count = 0
						for _ in range(2):
							count = 0
							self.player_field[y + 1][margin_index] = colored('#', 'green')
							y += 1

					elif y > y1:
						count = 0
						for _ in range(2):
							count = 0
							self.player_field[y + 1][margin_index] = colored('#', 'green')
							y -= 1


					elif margin_index1 > margin_index:
						for i in range(margin_index, margin_index1 + 1):
							self.player_field[y + 1][i] = colored('#', 'green')

					elif margin_index > margin_index1:
						for i in range(margin_index1, margin_index + 1):
							self.player_field[y + 1][i] = colored('#', 'green')


				else:
					return 'Введены неверные координаты построения'


			elif name == 'ship_1_cell':
				self.player_field[y + 1][margin_index] = colored('#', 'green')




	def getTheNumberOfShips(self):
		
		output = [f'Всего 4 местных кораблей: {self.ship_4_cell}', f'Всего 3 местных кораблей: {self.ship_3_cell}',
			 f'Всего 2 местных кораблей: {self.ship_2_cell}', f'Всего 1 местных кораблей: {self.ship_1_cell}']


		return output




player1 = Player()
player1.buildField(player1.ship_4_cell, 'ship_4_cell', 'А', 0, 'А', 3)
player1.buildField(player1.ship_3_cell, 'ship_3_cell', 'К', 0, 'К', 2)
player1.buildField(player1.ship_3_cell, 'ship_3_cell', 'А', 9, 'В', 9)
player1.buildField(player1.ship_2_cell, 'ship_2_cell', 'Г', 4, 'Г', 5)
player1.buildField(player1.ship_2_cell, 'ship_2_cell', 'Е', 7, 'Ж', 7)
player1.buildField(player1.ship_2_cell, 'ship_1_cell', 'И', 7, 'И', 7)
for i in player1.player_field:
	print(' '.join([str(j) for j in i]))