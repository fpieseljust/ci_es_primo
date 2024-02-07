import math


def es_primo(numero):
    if numero < 2:    
        return False
    else:
        for n in range(2, math.floor(math.sqrt(numero) + 1)):
            if numero % n == 0:
                return False
    return True

if __name__=='__main__':
    for i in range(2,100):
        print(f'{i} -> {es_primo(i)}')