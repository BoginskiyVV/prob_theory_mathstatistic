# Урок 10. Дисперсионный анализ

import numpy as np
import scipy.stats as stats

'''
Провести дисперсионный анализ для определения того, есть ли различия среднего роста 
среди взрослых футболистов, хоккеистов и штангистов. Даны значения роста в трех 
группах случайно выбранных спортсменов:
Футболисты: 173, 175, 180, 178, 177, 185, 183, 182
Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180
Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170
'''

football_players = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey_players = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifters = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
