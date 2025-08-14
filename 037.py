# Level 037

#  -------------------------------------------
#  -- TEMPERATURE IN CELSIUS AND FAHRENHEIT --
#  -------------------------------------------

measure = input("This temperature will be measure in Celsius or Fahrnheit? [F/C]: ")
temperature = float(input("Insert the temperature: "))

if measure == "C":
    conversor = round((9 * temperature) / 5 + 32)
    print(f"The temperature of {temperature}  Degree Celsius corresponds to {conversor:.2f}  Degree Fahrnheit")
elif measure == "c":
    conversor = round((9 * temperature) / 5 + 32)
    print(f"The temperature of {temperature} Degree Celsius corresponds to {conversor:.2f} Degree Fahrnheit")
elif measure == "F":
    conversor_c = ((temperature - 32) * 5 / 9)
    print(f"The temperature of {temperature} Degree Fahrnheit corresponds to {conversor_c:.2f} Degree Celsius")
elif measure == "f":
    conversor_c = ((temperature - 32) * 5 / 9)
    print(f"The temperature of {temperature} Degree Fahrnheit corresponds to {conversor_c:.2f} Degree Celsius")
else:
    print("This is not a valid value, please choose between [F/C] and insert a valid number!")