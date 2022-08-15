print("Olá,Mundo!!!")

if True:
    print("Hello, world!")

b = eval(input("Operação: "))
print(b)

a = 0
while a<=10:
    print(a, end='/')
    a += 1

print()

# C#: for(x=0; x<10; x++)
# Rust: for x in (0..10)
for x in range(10,0,-1):
    print(x, end=',')

