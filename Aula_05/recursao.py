def contagem_regressiva(i: int) -> None:
    print(i)
    if i > 0:
        contagem_regressiva(i - 1)
        
# contagem_regressiva(10)

def fatorial(n: int):
    if n <= 0:
        return
    if n == 1:
        return 1
    return n * fatorial(n -1)

print(fatorial(6))