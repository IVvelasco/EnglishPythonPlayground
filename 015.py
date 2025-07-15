# Level 015
# -----------------------------------------------
# -- Mode, Mean and Median using NUMPY e SCIPY --
# -----------------------------------------------

import numpy as np
from scipy import stats

def main():
        # Collect multiple values from the user
    print("Type your dates separate by commas (ex: 31,32,30,29):")
    numbers = input("Declare here the data you want to analyze:: ")
    
    # Convert the string into numbers
    try:
        # Take one by one, remove espaces and convert float
        data_list = [float(i.strip()) for i in numbers.split (',')]
        data = np.array(data_list)
    except Exception:
        print("Erro: check if the insert data is in the right format.")
        return
    
    # MEAN
    mean = np.mean(data)
    
    # STANDARD DEVIATION
    standard_deviation = np.std(data)
    
    # MEDIAN
    median = np.median(data)
    
    # MODE
    mode_result = stats.mode(data, keepdims=True)
    mode = mode_result.mode[0]
    
    # OUTPUT
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print(f"DATA PROCESSED: {data_list}")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print(f"MEAN: {mean:.2f}")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print(f"MEDIAN: {median:.2f}")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print(f"MODE: {mode:.2f}")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print(f"STANDARD DEVIATION: {standard_deviation:.2f}")
    print("----------------------------------------------------------------------------------------------------------------------------------------")

# Chamar a função principal
if __name__ == "__main__":
    main()