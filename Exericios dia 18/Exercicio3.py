# 3. Crie uma função que verifique se um número é primo.

def é_primo(x):
    if(x <= 1):
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
num = float(input("Digite um número: "))
if é_primo(num):
    print("O número é primo")
else:
    print("O número não é primo")