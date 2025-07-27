# Level 022

# ------------------------
# -- Movies: Age Rating --
# ------------------------

"""
Here in Brazil we have a law that protects children and adolescents from certain types 
of content, this is divided according to age group and that is what this code is about.

The comments after define your classification is about why you or you child cannot watch that movie, in Brazil We take 
care with the content We expose our childrens and I decide do a code about it because could be funny and educational ;)
"""

idade = int(input("Please, insert your age (use just int numbers) and discover your age range based on Brazilian Classification: "))

if idade <= 9:
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("According to the Brazilian indicative classification, your range for films is: FREE CLASSIFICATION")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("This rating does not expose the child to potentially harmful content.")
    print("--------------------------------------------------------------------------------------------------------------------------")
elif idade <=10:
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("According to the Brazilian indicative classification, your range for films is: FORBIDDENG TO LESS THAN 10 YEARS")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("The film may contain violent content or language inappropriate for children, even if to a lesser extent.")
    print("--------------------------------------------------------------------------------------------------------------------------")
elif idade <=11:
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("According to the Brazilian indicative classification, your range for films is: FORBIDDENG TO LESS THAN 12 YEARS")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("Scenes may contain physical aggression, drug use and sexual insinuation.")
    print("--------------------------------------------------------------------------------------------------------------------------")
elif idade <=13:
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("According to the Brazilian indicative classification, your range for films is: FORBIDDENG TO LESS THAN 14 YEARS")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("More violent content and/or more pronounced sexual language")
    print("--------------------------------------------------------------------------------------------------------------------------")
elif idade <=15:
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("According to the Brazilian indicative classification, your range for films is: FORBIDDENG TO LESS THAN 16 YEARS")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("More violent content or content with more intense visual content, with scenes of torture, suicide, rape or full nudity")
    print("--------------------------------------------------------------------------------------------------------------------------")
elif idade <=17:
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("According to the Brazilian indicative classification, your range for films is: FORBIDDENG TO LESS THAN 18 YEARS")
    print("--------------------------------------------------------------------------------------------------------------------------") 
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("Extreme violent and sexual content. With scenes of sex, incest, or repeated acts of torture, mutilation, or sexual abuse")
    print("--------------------------------------------------------------------------------------------------------------------------")
elif idade >=18:
    print("If you have more than 18, you can watch what you want ;) ")