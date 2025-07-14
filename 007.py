# Level 007

# --------------
# -- CONVERSOR --
# --------------


def conversor_days(days):
    
    """ Converts days to hours, minutes and seconds """
    
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    return hours, minutes, seconds

def main ():
    print("=== CONVERSOR DE DIAS ===")

    try: 
        # Solicita o nuḿero de dias ao usuário
        days = float(input("Digite o número de dias: "))

        # Calcula as conversões
        hours, minutes, seconds = conversor_days(days)

        # Exibe os resultados 
        print(f"\nYours {days} converted are: ")
        print(f"{hours:,.0f} hours")
        print(f"{minutes:,.0f} minutes")
        print(f"{seconds:,.0f} seconds")

    except ValueError:
        print("Error, please enter a valid number!")

if __name__ == "__main__":
    main()