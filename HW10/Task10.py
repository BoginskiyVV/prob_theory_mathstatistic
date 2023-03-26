# Урок 10. Дисперсионный анализ

from scipy.stats import f_oneway

'''
Провести дисперсионный анализ для определения того, есть ли различия среднего роста 
среди взрослых футболистов, хоккеистов и штангистов. Даны значения роста в трех 
группах случайно выбранных спортсменов:
Футболисты: 173, 175, 180, 178, 177, 185, 183, 182
Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180
Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170
'''

football_players = [173, 175, 180, 178, 177, 185, 183, 182]
hockey_players = [177, 179, 180, 188, 177, 172, 171, 184, 180]
weightlifters = [172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170]

print(f_oneway(football_players, hockey_players, weightlifters))
print('Средний рост одной группы спортсменов отличается от других, т.к. значение pvalue меньше 5%, 0 гипотеза отвергается')