import math
ang = float(input('\033[1;30;46m Digite o Angulo'))
s = math.sin(math.radians(ang))
print('\033[1;33;46m O ângulo de {} tem o seno de {:.2f}'.format(ang, s))
c = math.cos(math.radians(ang))
print('\033[1;33;46m O ângulo de {} tem o Cosseno de {:.2f}'.format(ang, c))
t = math.tan(math.radians(ang))
print('\033[1;33;46m O ângulo de {} tem a Tangent de {:.2f}'.format(ang, t))
