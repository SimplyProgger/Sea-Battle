# Console Sea-Battle by SimplyProgger




class Player:

	def __init__(self):

		self.player_field = self.createField()



	def createField(self):
		top_margin = [' ', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И' ,'К']
		player_field = [['~' for i in range(10)] for j in range(10)]

		for i in range(10):
			list_pred = player_field[i]
			new_list = [i] + list_pred
			player_field[i] = new_list
			
		pred_list = player_field
		player_field = [top_margin] + pred_list

		return player_field





player1 = Player()
for i in player1.player_field:
	print(' '.join([str(j) for j in i]))