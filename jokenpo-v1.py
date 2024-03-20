#Jokenpô
import os, time, random
print('''\033[1;31m
      
 _____                                          _____ 
( ___ )----------------------------------------( ___ )
 |   |                                          |   | 
 |   |      _       _                     //\   |   | 
 |   |     | | ___ | | _____ _ __  _ __  |/_\|  |   | 
 |   |  _  | |/ _ \| |/ / _ \ '_ \| '_ \ / _ \  |   | 
 |   | | |_| | (_) |   <  __/ | | | |_) | (_) | |   | 
 |   |  \___/ \___/|_|\_\___|_| |_| .__/ \___/  |   | 
 |   |                            |_|           |   | 
 |___|                                          |___| 
(_____)----------------------------------------(_____)\033[m''')

time.sleep(3)
os.system('cls')
print('''


 ________      ___    ___             ________ ___  ___  ___  ___  ________  ________     
|\   __  \    |\  \  /  /|___        |\  _____\\  \|\  \|\  \|\  \|\   __  \|\   __  \    
\ \  \|\ /_   \ \  \/  / /\__\       \ \  \__/\ \  \\\  \ \  \\\  \ \  \|\  \ \  \|\  \   
 \ \   __  \   \ \    / /\|__|        \ \   __\\ \  \\\  \ \   __  \ \  \\\  \ \   _  _\  
  \ \  \|\  \   \/  /  /     ___       \ \  \_| \ \  \\\  \ \  \ \  \ \  \\\  \ \  \\  \| 
   \ \_______\__/  / /      |\__\       \ \__\   \ \_______\ \__\ \__\ \_______\ \__\\ _\ 
    \|_______|\___/ /       \|__|        \|__|    \|_______|\|__|\|__|\|_______|\|__|\|__|
             \|___|/                                                                      

''')
time.sleep(2)
os.system('cls')
#Classificando os itens.
itens = ['pedra', 'papel', 'tesoura']
#Aleatorizando a escolha do robô.
robo = random.randint(0, 2)
#Descrição do Jogo

print('''
      



      
      
      \033[1;31;40mJokenpô: o duelo clássico de pedra, papel e tesoura. Escolha seu elemento e desafie o robô.
       Pedra esmaga tesoura, papel embrulha pedra, e tesoura corta papel. Rápido, simples e divertido!\033[m
      
      
      
      ''')
print(' ')
print('                                                            \033[1;31;40mPor favor, aguarde 10 segundos.\033[m')
time.sleep(10)
os.system('cls')

#Escolha
print('''Você tem 3 alternativas para ganhar do robô, escolha entre essas 3.
      
      [0] \033[32mPedra\033[m
      [1] \033[34mPapel\033[m
      [2] \033[33mTesoura\033[m      
      
      ''')
#Jogada
jogador = int(input('Digite o número que deseja jogar: '))
print('Processando.')
time.sleep(0.5)
os.system('cls')
print('Processando..')
time.sleep(0.5)
os.system('cls')
print('Processando...')
time.sleep(0.5)
os.system('cls')
print('Processando.')
time.sleep(0.5)
os.system('cls')
print('Processando..')
time.sleep(0.5)
os.system('cls')
print('Processando...')
time.sleep(0.5)
os.system('cls')
print(f'O jogador jogou: {itens[jogador]}')
print(f'O robô jogou: {itens[robo]}')
#Resultados
if robo > 2 and jogador > 3 and robo < 0 and jogador < 0:
    print('Por favor, digite um número de \033[1;34m0 a 2.\033[m')
if robo == 0:
    if jogador == 0:
        print('Vocês empataram!')
        print(' ')
        print('''
              





    ______                      __     
   / ____/___ ___  ____  ____ _/ /____ 
  / __/ / __ `__ \/ __ \/ __ `/ __/ _ \
 / /___/ / / / / / /_/ / /_/ / /_/  __/
/_____/_/ /_/ /_/ .___/\__,_/\__/\___/ 
               /_/                     
              
              
              
              
              
              
              ''')
    elif jogador == 1:
        print('Você ganhou!')
        print(' ')
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    elif jogador == 2:
        print('Você perdeu!')
        print(' ')
    else:
        print('Jogada inválida.')
if robo == 1:
    if jogador == 0:
        print('Você perdeu!')
        print(' ')
    elif jogador == 1:
        print('Vocês empataram!')
        print(' ')
        print('''
              



    ______                      __     
   / ____/___ ___  ____  ____ _/ /____ 
  / __/ / __ `__ \/ __ \/ __ `/ __/ _ \
 / /___/ / / / / / /_/ / /_/ / /_/  __/
/_____/_/ /_/ /_/ .___/\__,_/\__/\___/ 
               /_/                     
              
              
              
              
              
              
              ''')
    elif jogador == 2:
        print('Você ganhou!')
        print(' ')
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    else:
        print('Jogada inválida.')
if robo == 2:
    if jogador == 0:
        print('Você ganhou!')
        print(' ')
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif jogador == 1:
        print('Você perdeu!')
        print(' ')
    elif jogador == 2:
        print('Vocês empataram!')
        print(' ')
        print('''
              




    ______                      __     
   / ____/___ ___  ____  ____ _/ /____ 
  / __/ / __ `__ \/ __ \/ __ `/ __/ _ \
 / /___/ / / / / / /_/ / /_/ / /_/  __/
/_____/_/ /_/ /_/ .___/\__,_/\__/\___/ 
               /_/                     
              
              
              
              
              ''')
    else:
        print('Jogada inválida.')
