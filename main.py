a=int(input('Ievadi kvadrāta malas garumu centimetros: '))
print(str(int((a+5)**2/a**2*100-100))+'%') if a>5 else print('Invalid input')