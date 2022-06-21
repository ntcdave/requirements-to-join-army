print('Consulte os requisitos para entrar no Army\n')

name = (str(input("what's your name?: ")))
age = (int(input('How old are you?: ')))
weight = (float(input('how much do you weight?: ')))
height = (float(input('How tall are you?: ')))

''' requires to join it '''
if age >= 18 and weight >= 60.0 and height >= 1.70:
    print('Well, you are able to join the army')
else:
    print("\nSorry, you don't have the requirements to join the brazilian army, maybe another time? :) ")
