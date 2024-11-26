list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

lenght_list=len(list_players)
lenght_list_mide=lenght_list//2

team_1=list_players[0:lenght_list_mide]
team_2=list_players[lenght_list_mide:]

print(team_1)
print(team_2