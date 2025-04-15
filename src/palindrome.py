mport string

def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

if _name_ == "_main_":
    while True:
        try:
            frase = input("Ingrese una palabra o frase: ")
            if is_palindrome(frase):
                print(f'"{frase}" es un palíndromo')
            else:
                print(f'"{frase}" no es un palíndromo')
        except KeyboardInterrupt:
            print("\nSaliendo...")
            break