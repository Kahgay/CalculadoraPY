import time
from decimal import *
import sys
from termcolor import colored, cprint 


def calculando():
  time.sleep(1)
  for pontos in range(1, 5):
   palavra = 'Calculando'
   if pontos == 1:
     caractere = '.'
   elif pontos == 2:
     caractere = '..'
   elif pontos == 3:
     caractere = '...'
    
   print(palavra + caractere, end='\r')
   time.sleep(1)
  
  

class colors: 
  HEADER = '\033[95m' 
  OKBLUE = '\033[94m' 
  OKCYAN = '\033[96m' 
  OKGREEN = '\033[92m' 
  WARNING = '\033[93m' 
  FAIL = '\033[91m' 
  ENDC = '\033[0m' 
  BOLD = '\033[1m' 
  UNDERLINE = '\033[4m'
cprint('\n[AVISO] Esse projeto NÃO TEM 100% de certeza, estudem que é melhor, não use esse projeto pensando que vai gabaritar na prova, o projeto foi criado para ser algo muito menos sério do que vestibular, prova, simulado. Se estiver fazendo um agora, boa sorte!', 'yellow', attrs=['bold'], file=sys.stderr)
cprint('[!] A responsabilidade é toda sua, se ir mal em um simulado, prova, vestibular, a culpa não irá ser do projeto, estudem que é melhor :)\n\n', 'red', attrs=['bold'], file=sys.stderr)
cprint('[1] 2 números [ON] \n[2] 3 números [ON] \n[11] Potência [ON] \n[12] Raiz Quadrada e Cúbica [ON]\n[13] Descobrir o raio [ON]\n[14] Circunferência (Círculo) [ON]\n[exit] exit\n\n\n', 'white', attrs=['bold'], file=sys.stderr)

escolha = input('Selecione a opção: ')

while len(escolha) < 0 or escolha == "" or escolha != '1' and escolha != '2' and escolha != 'exit' and escolha != '11' and escolha != '12' and escolha != '13' and escolha != '14':
  print('Opção inválida')
  escolha = input('Selecione a opção: ')
  
if escolha == '1':

 calc = str(input('Escolha o número: ')).lower()

 while len(calc) < 0 or calc == "":
  print('Ei, coloque um número válido')
  calc = input('Escolha o número: ')

 sinal = str(input('Coloque o sinal ["+", "-", "*", "/"]: ')).lower()

 while len(sinal) < 0 or sinal != '+' and sinal != '-' and sinal != '*' and sinal != '/':
    print('Podem apenas os sinais ["+", "-", "*", "/"]')
    sinal = str(input('Coloque o sinal ["+", "-", "*", "/"]: ')).lower()
    
 calc2 = str(input('Escolha o segundo números: ')).lower()

 while len(calc2) < 0 or calc2 == "":
  print('Ei, coloque um número válido.')
  calc = input('Escolha o número: ')
  
 print(calc, sinal, calc2 + ' = ?')

 calculando()
 time.sleep(1)
 print('Pronto       ')
 
 try:
   if sinal == '+':
     total = Decimal(calc) + Decimal(calc2)
   elif sinal == '-':
     total = Decimal(calc) - Decimal(calc2)
   elif sinal == '*':
     total = Decimal(calc) * Decimal(calc2)
   elif sinal == '/':
     total = Decimal(calc) / Decimal(calc2)
 
   print(calc, sinal, calc2 + ' = ' + str(total))
 except InvalidOperation as err:
   print(colors.FAIL + 'Algo deu muito errado, o erro foi: ', err)
if escolha == '2':

 calc = str(input('Escolha o número: ')).lower()

 while len(calc) < 0 or calc == "":
  print('Ei, coloque um número válido')
  calc = input('Escolha o número: ')

 sinal = str(input('Coloque o sinal ["+", "-", "*", "/"]: ')).lower()

 while len(sinal) < 0 or sinal != '+' and sinal != '-' and sinal != '*' and sinal != '/':
    print('Podem apenas os sinais ["+", "-", "*", "/"]')
    sinal = str(input('Coloque o sinal ["+", "-", "*", "/"]: ')).lower()
    
 calc2 = str(input('Escolha o segundo número: ')).lower()

 while len(calc2) < 0 or calc2 == "":
  print('Ei, coloque um número válido.')
  calc = input('Escolha o número: ')
  
 sinal2 = str(input('Coloque o sinal ["+", "-", "*", "/"]: ')).lower()

 while len(sinal2) < 0 or sinal2 != '+' and sinal2 != '-' and sinal2 != '*' and sinal2 != '/':
    print('Podem apenas os sinais ["+", "-", "*", "/"]')
    sinal2 = str(input('Coloque o sinal ["+", "-", "*", "/"]: ')).lower()
 calc3 = str(input('Escolha o terceiro número: ')).lower()

 while len(calc3) < 0 or calc3 == "":
  print('Ei, coloque um número válido.')
  calc = input('Escolha o número: ')
  
 print(calc, sinal, calc2, sinal2, calc3 + ' = ?')

 calculando()
 time.sleep(1)
 print('Pronto       ')
 
 try:

   if sinal == '+' or sinal2 == '+':
     total = Decimal(calc) + Decimal(calc2) + Decimal(calc3)
   elif sinal == '-' or sinal2 == '-':
     total = Decimal(calc) - Decimal(calc2) - Decimal(calc3)
   elif sinal == '*' or sinal2 == '*':
     total = Decimal(calc) * Decimal(calc2) * Decimal(calc3)
   elif sinal == '/' or sinal2 == '/':
     total = Decimal(calc) / Decimal(calc2) / Decimal(calc3)
 # Possibilidades com "+"
   if sinal == '+':
     if sinal2 == '-':
       total = Decimal(calc) + Decimal(calc2) - Decimal(calc3)
     elif sinal2 == '*':
       total = Decimal(calc) + Decimal(calc2) * Decimal(calc3)
     elif sinal2 == '/':
       total = Decimal(calc) + Decimal(calc2) / Decimal(calc3)
 # Possibilidades com "-"
   if sinal == '-':
     if sinal2 == '+':
       total = Decimal(calc) - Decimal(calc2) + Decimal(calc3)
     elif sinal2 == '*':
       total = Decimal(calc) - Decimal(calc2) * Decimal(calc3)
     elif sinal2 == '/':
       total = Decimal(calc) - Decimal(calc2) / Decimal(calc3)
   # Possibilidades com "*"
   if sinal == '*':
     if sinal2 == '+':
        total = Decimal(calc) * Decimal(calc2) + Decimal(calc3)
     elif sinal2 == '-':
       total = Decimal(calc) * Decimal(calc2) - Decimal(calc3)
     elif sinal2 == '/':
       total = Decimal(calc) * Decimal(calc2) / Decimal(calc3)
    # Possibilidades com "/"
   if sinal == '/':
     if sinal2 == '+':
       total = Decimal(calc) / Decimal(calc2) + Decimal(calc3)
     elif sinal2 ==  '-':
       total = Decimal(calc) / Decimal(calc2) - Decimal(calc3)
     elif sinal2 == '*':
       total = Decimal(calc) / Decimal(calc2) * Decimal(calc3)
   print(calc, sinal, calc2, sinal2, calc3 + ' = ' + str(total))
 except ValueError as err:
   print(colors.FAIL + 'Algo deu muito errado, o erro foi: ', err)
if escolha == '11':
   potencianum = input('Escolha um número: ')
  
   while len(str(potencianum)) < 0:
    print('Coloque um número válido')
    potencianum = input('Escolha um número: ')
  
   potencia = input('Escolha o número da potência: ')
  
   while len(str(potencia)) < 0:
    print('Coloque um número válido')
    potencia = Decimal(input('Escolha o número da potência: '))
  
   print(str(potencianum) + '^(' + str(potencia) + ') = ?')
  
   calculando()
   time.sleep(1)
   print('Pronto       ')
 
   try:
     total = potencianum ** potencia
     print(str(potencianum) + '^(' + str(potencia) + ') =', str(total))
   except ValueError as err:
     print(colors.FAIL + 'Algo deu muito errado, o erro foi: ', err)

if escolha == '12':
  qouc = input('Raiz Quadrada ou Cúbica? [Quadrada/Cúbica]: ').lower()
  while len(qouc) < 0 or qouc != 'quadrada' and qouc != 'cúbica':
    print('Opção inválida, coloque Quadrada ou Cúbica')
    qouc = input('Raiz Quadrada ou Cúbica? [Quadrada/Cúbica]: ').lower()
    
  if qouc == 'quadrada':
     número = input('Escolha o número: ')
     while len(str(número)) < 0:
      print('Escola um número válido')
      número = input('Escolha o número: ')
     qouc = '²√'
     print(str(qouc) + str(número) + ' = ?')
    
     calculando()
     time.sleep(1)
     print('Pronto       ')

     try:
       total = número ** (1/2)
       print(str(qouc) + str(número) + ' =', str(total))
     except ValueError as err:
       print(colors.FAIL + 'Algo deu muito errado, o erro foi: ', err)
    
     
  elif qouc == 'cúbica':
     número = input('Escolha o número: ')
     while len(str(número)) < 0:
       print('Escola um número válido')
       número = input('Escolha o número: ')
     qouc = '³√'
     print(str(qouc) + str(número) + ' = ?')
    
     calculando()
     time.sleep(1)
     print('Pronto       ')

      
     try: 
       total = número ** (1/3)
       print(str(qouc) + str(número) + ' =', str(total))
     except ValueError as err:
       print(colors.FAIL + 'Algo deu muito errado, o erro foi: ', err)

if escolha == '13':
  circunferência = input('Coloque o valor da circunferência: ')
  while len(str(circunferência)) < 0:
    print('Número inválido, forneça um número')
    circunferência = input('Coloque o valor da circunferência: ')
  
  pi = input('Coloque o valor de π(pi): ')
  while len(pi) < 0:
    print('Número inválido, forneça um número')
    pi = input('Coloque o valor de π(pi): ')
  print('2 *', pi, '/', circunferência, '= ?')
  calculando()
  
  time.sleep(1)
  print('Pronto       ')
  
  pitotal = 2 * Decimal(pi)
  total = Decimal(circunferência) / Decimal(pitotal)
  
  print('2 *', pi, '/', circunferência, '=', total)
if escolha == '14':
  pi = input('Coloque o valor de π(pi): ')
  while len(pi) < 0:
    print('Forneça um número')
    pi = input('Coloque o valor de π(pi): ')
  raio = input('Coloque o valor do raio: ')
  while len(raio) < 0:
    print('Forneça um número')
    raio = input('Coloque o valor do raio: ')
  print('2 *', pi + ' *', raio, '= ?')
  calculando()
  time.sleep(1)
  print('Pronto       ')
  
  total = 2 * Decimal(pi) * Decimal(raio)
  
  print('2 *', pi + ' *', raio, '=', str(total))
