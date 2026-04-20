import sys
from utils import is_prime

def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <número>")
        sys.exit(1)

    try:
        numero = int(sys.argv[1])

        if is_prime(numero):
            print(f"O número '{numero}' é primo.")
        else:
            print(f"O número '{numero}' NON é primo.")

    except ValueError:
        print("Non é un número válido")
        sys.exit(1)

if __name__ == "__main__":
    main()
