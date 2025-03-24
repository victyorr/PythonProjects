import random

word_bank = ['lomba','gamer','raios','funde','quiz']

word = random.choice(word_bank)
guessed_word = ['_'] * len(word)

attempts = 10

print('Olá, você está no jogo: Wordle!')
print('\nA quantidade de tentativas que tem é: '+ str(attempts))
while attempts > 0:
    print('\nCurrent Word: ' + ' '.join(guessed_word))
    guess = input('Tente uma letra: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print('Boa tentativa!')
    else:
        attempts -= 1
        print('Errou a tentativa! Tentativas restante: '+ str(attempts))
    if '_' not in guessed_word:
        print('\nParabéns! Você acertou a palavra '+ word)
        break

if attempts == 0:
    print('\nVocê ficou sem tentativas! A palavra era:' + word)
