def imprime_media(a:float , b:float) -> None:
    print(media(a, b))


# imprime_media(10, 20)

# x = float(input("x: "))
# y = float(input("y: "))

# imprime_media(x, y)

def media(a:float = 40, b:float = 50) -> float:
    return((a + b)/2)

# print(media(10))
# print(media(30, 64))

def media_arbitraria(*args):
    n = 0
    s = 0
    for i in args:
        s += i
        n += 1
    if n == 0:
        return 0 
    return s/n

# print(media_arbitraria(1, 2, 3, 4, 5, 6, 7))
