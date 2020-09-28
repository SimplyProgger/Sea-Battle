# Console Sea-Battle by SimplyProgger

top_margin = [' ', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И' ,'К']
player_1_field = [['~' for i in range(10)] for j in range(10)]

for i in range(10):
	list_pred = player_1_field[i]
	new_list = [i] + list_pred
	player_1_field[i] = new_list
	
pred_list = player_1_field
player_1_field = [top_margin] + pred_list

for i in player_1_field:
	print(' '.join([str(j) for j in i]))