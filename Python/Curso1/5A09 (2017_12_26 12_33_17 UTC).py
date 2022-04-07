frase = 'OI como voce vai otario'
print(frase)    #Vai escrever a frase
print(frase[3]) #Vai escrever a letra 'c' que e o 3° caractere e quarta letra
print(frase[1:7])   #Vai comesar do 1° caractere ater o 7°, cendo que não vai escrever o cetimo
print(frase[4:])    #Vai do 4° ate o fim
print(frase[:9])    #Vai do inicio ate 9°
print(frase[2:16:2])    #Vai do 2° ate 16° pulando de 2 em 2
print(frase[4::5])  #Vai do 4° ate o fim pulando 2 em 2
print(frase[::2])   #Vai do inicio ate o fim pulando 2

frase1 = """   Bom dia, amigo
Que a paz seja contigo
Eu vim somente dizer
Que eu te amo tanto
Que vou morrer
Amigo... adeus   """   #Aspas tripula(3) para escrever textos em mais linas

print(frase1.count('o'))    #Vai contar quantas letras 'o' tem
print(frase1.upper())   # Vai deixa a frase maiuscula
print(frase1.lower())   #Vai deixa minuscula
print(len(frase1))  #Vai dise o tamanho da frase
print(frase1.strip())   #Remove os espaços indegeijados
frase.strip()
print(len(frase1.strip()))  #Vai dise o tamanho da frase tirando os espaços do inicio e fim
print(frase1.replace('amigo', 'colega'))    #Troca a palavra 'amigo' por 'colega'
print('morrer' in frase1)    # Vai dize se tem a palafra 'morrer' em frase1
print(frase1.find('adeus'))  #Vai dise em que posiçao esta a palavra 'adeus'
print(frase1.strip().replace('OI', 'Ola').split())
print(frase1.split())    #Vai dividir todas as palafras da frase em uma lista
frase1.split()
print('-'.join(frase1)) # Vai vai juntar a palavra denovo e colocar '-' nolugar dos espaços


print(frase1.strip(), ' \n esta frase tem ', len(frase1), 'Letras')

nome1 = input('Digite Seu Nome:')
nome1 = nome1.upper()
print(nome1.strip())
print(nome1.lower().strip())
nomes1 = nome1.split()
nomesj1 = ''.join(nomes1)
print('Seu Nome Ten ', len(nomesj1), 'Letras')
primeiron = nomes1[0]
print('Seu Primeiro Nome Ten ', len(primeiron), 'Letras')

nomess = 'SANTO' in nome1.strip()
print('Voce é da Familha santo {}'.format(nomess))

cd = str(input('Nome De sua Cidade:')).strip()
cd = cd.upper()
print(cd[:5] == 'SANTO')

numero = int(input('Dijite Um Numero de 1 a 9999:'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Unidade: {} \n Dezena: {} \n Centena: {} \n Milhar: {}'.format(u, d, c, m))

fraz1 = str(input('Sua Frase Favorita')).strip().upper()
fraz = fraz1.split()
fraz = ''.join(fraz)
print('A sua frase tem {} letras A, A primeira letra aparese no {} Carictere é a utima no {} Carictere '.format(fraz.count('A'), fraz.find('A') + 1, fraz.rfind('A') + 1))

noms = str(input('Seu Nome Completo')).strip().lower()
nomsd = noms.split()
print('{}'.format(noms.title()))
print('Primeiro Nome: {}'.format(nomsd[0].title()))
print('Utimo Nome: {}'.format(nomsd[len(nomsd)-1].title()))

