def fib(n):
    """n までのフィボナッチ級数を表示する"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b =  b, a+b
        print()



def fib2(n):
    """n までのフィボナッチ級数から成るリストを返す"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2()
