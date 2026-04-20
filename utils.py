'''
def fizz_buzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return n
'''

def mayor_de_tres(a, b, c):
    """
    Recibe tres números y devuelve el mayor.
    """
    return max(a, b, c)
