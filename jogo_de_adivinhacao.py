#Cenário: Um jogo de adivinhação55

import random

#Início do game informando as regras
print("\nOlá jogador! Está pronto para jogar?")
print("Você terá 3 chances para adivinhar o número sorteado entre 1 e 100.")
print("A cada tentativa o jogo dará uma dica se o número é maior ou menor que o número aleatório.")
print("Se você acertar, você ganha; caso não acerte, o jogo acaba e o número será revelado.\nBoa sorte!")

#Função para o jogo de adivinhação
def jogar_adivinhacao():
    # Escolher um número aleatório entre 1 e 100
    numero = random.randint(1, 100)

    #Inicializando contador e somador
    tentativas = 3
    tentativas_feitas = 0

    #Loop de tentativas
    while tentativas > tentativas_feitas:
        jogador = int(input("Digite um número entre 1 e 100: "))
        tentativas_feitas += 1

        #Verificar se o número escolhido é o correto
        if jogador == numero:
            print("Parabéns! Você acertou!")
            print("O número secreto é:", numero)
            break  # Finalizar em caso de acerto

        #Dicas e tentativas 
        else:
            if jogador < numero:
                print("O número secreto é maior. Tente novamente.")
            else:
                print("O número secreto é menor. Tente novamente.")

    #Verifica se o jogador não acertou após 3 tentativas
    if jogador != numero:
        print("Você não acertou o número. O número secreto era", numero)

#Função para perguntar se o jogador quer jogar novamente
def jogar_novamente():
    while True:
        jogar_adivinhacao()  # Chama a função que contém a lógica do jogo
        
        # Pergunta ao jogador se deseja jogar novamente
        resposta = input("\nDeseja jogar novamente? (s para sim, qualquer outra tecla para não): ").lower()
        
        if resposta != 's':
            print("\nObrigado por jogar! Até a próxima!")
            break  # Sai do loop e finaliza o programa
        else:
            print("\nOba! Vamos nessa!")
            print("\nCarregando...")
            print("\nTudo pronto!")

#Chama a função para iniciar o jogo
jogar_novamente()