print('********************************')
print('        Jogo da Adivinhação     ')
print('********************************')

numero_secreto = 42
pontuacao = 1000
print('\nPontuação inicial: ', pontuacao)
dificuldade = int(input('Escolha uma dificuldade: \n1 - Fácil;\n2 - Médio\n3 - Difícil\n'))
#rodada = 1

#while(rodada <= total_de_tentativas):
if(dificuldade == 1):
    total_de_tentativas = 20
elif(dificuldade == 2):
    total_de_tentativas = 10
elif(dificuldade == 3):
    total_de_tentativas = 5
    
for rodada in range(1, total_de_tentativas+1):
    print('\nTentativa {} de {}'.format(rodada, total_de_tentativas))

    chute = int(input('\nDigite o seu número: \n'))
    print('\nVocê digitou: ', chute)
    diferenca = abs(numero_secreto - chute)

    if(numero_secreto == chute):
        print('\nvocê acertou!!')
        break
    elif(chute > numero_secreto):
        print('\nVoce errou! O chute foi maior que o numero secreto')
        pontuacao -= diferenca
        print('\nSua pontuação agora é: ', pontuacao)
    elif(chute < numero_secreto):
        print('\nVoce errou! O chute foi menor que o numero secreto')
        pontuacao -= diferenca
        print('\nSua pontuação agora é: ', pontuacao)
print('\nFim do jogo!')