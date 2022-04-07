palavras = ('Ambiguidade', 'Pragmatico', 'Impio', 'Tortuoso',
            'Defasado', 'Inificiencia', 'Parco', 'Macrocosmo',)
vg = ('A', 'E', 'I', 'O', 'U')
for p in palavras:
    print(f'\n\033[1;36mNa palavra {p} temos ', end='')
    for c in range(0, len(p)):
        if p[c].upper() in vg:
            print(f'\033[1;34m{p[c]}', end=' ')








print('\033[1;35m')
                                    # Resposta do Guanabara


palavra = ('aprender', 'programar', 'linguagem', 'python',
           'curso', 'gratis', 'estudar', 'praticr',
           'trabalhar', 'marcado', 'programador', 'futuro')
for p in palavra:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
