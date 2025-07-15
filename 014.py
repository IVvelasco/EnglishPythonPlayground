# Level 014
# ---------------------------
# -- Mode, Mean and Median --
# ---------------------------

import numpy as np

"""
CLIMATE DATA TAKEN DIRECTLY FROM THE MINISTRY OF AGRICULTURE, LIVESTOCK, AND SUPPLY - MAPA
National Institute of Meteorology - INMET
General Coordination of Applied Meteorology, Development, and Research - CGMADP
Center for Weather Analysis and Forecasting - CAPRE
Porto Alegre, February 25, 2025
CLIMATE BULLETIN
JANUARY 2025 BALANCE SHEET FOR PORTO ALEGRE.
"""


temp_max = np.array([31, 32, 30, 29, 30, 31, 32, 30, 29, 30, 31, 33, 35, 35, 34, 33, 35, 34, 35, 34, 33, 34, 34, 33, 32, 30, 31, 32, 33, 32, 31])
temp_min = np.array([23, 22, 21, 20, 19, 18, 17, 19, 20, 19, 20, 21, 22, 23, 22, 21, 22, 21, 20, 21, 22, 21, 20, 19, 20, 21, 22, 21, 22, 21, 21])

# CALCULATION OF THE MEDIAN
median0 = np.mean(temp_max)
median1 = np.mean(temp_min)

# CALCULATION OF STANDARD DEVIATION 
standart_deviation0 = np.std(temp_max)
standart_deviation1 = np.std(temp_min)

# OUTPUT

print("----------------------------------------------------------------------------------------------------------------------------------------")
print(f"DATA WORKED ON MAXIMUM TEMPERATURE: {temp_max}")
print("----------------------------------------------------------------------------------------------------------------------------------------")
print(f"MEDIAN: {median0:.2f}")
print("----------------------------------------------------------------------------------------------------------------------------------------")
print(f"STANDART DEVIATION: {standart_deviation0:.2f}")
print("----------------------------------------------------------------------------------------------------------------------------------------")
print("")

print("")
print("----------------------------------------------------------------------------------------------------------------------------------------")
print(f"DADOS TRABALHADOS SOBRE A TEMPERATURA MÍNIMA: {temp_min}")  
print("----------------------------------------------------------------------------------------------------------------------------------------")
print(f"MÉDIA: {median1:.2f}")
print("----------------------------------------------------------------------------------------------------------------------------------------")
print(f"DESVIO PADRÃO: {standart_deviation1 :.2f}")
print("----------------------------------------------------------------------------------------------------------------------------------------")