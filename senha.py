print(f'Agora vamos criar sua senha.')

while True:
    senha = input(f"Digite a nova senha:\n")
    quant = len(senha)
    if quant < 14: 
        print("Número de caracteres menor que 14, favor verificar.")
        continue
    elif senha.lower() == senha:
        print("A senha não tem letras maiúsculas, por favor verifique a senha.")
        continue
    elif not senha.isalpha() == False:
        print('A senha não contém número, favor ferificar a senha.')
        continue
    elif not senha.isalnum() == False:
        print('A senha não contém caracteres especiais, favor verificar a senha.')
        continue
    else:
        break


print('Senha válida!')
