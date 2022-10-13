num1 = int(input("Digite um Numero:"));

if num1%2 == 0:
    print("Par");
else:
    print("Impar");

s = 0
for i in range(5):
    s += 3*i
print(s)