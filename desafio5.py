tipos_usuario = ["admin", "funcionario", "visitante"]

nome_usuario = ""
idade_usuario = ""
tipo_usuario = ""
cargo = ""

print(f"Tipos usuário: {tipos_usuario}")


#entrada usuário 
nome = input("Digite seu nome completo: ")
idade = input("Informe sua idade: ")
usuario = input("Informe seu tipo de usuário: ")
cargo_usuario = input("Informe seu cargo na empresa: ")


#formatando e armazenando entradas
nome_usuario = nome.strip().title()
idade_usuario = int(idade.strip())
tipo_usuario = usuario.strip().lower()
cargo = cargo_usuario.strip().lower()


#acesso permissão
permitido_acesso = True

#condições
if tipo_usuario == "admin":
    permitido_acesso = True

elif tipo_usuario == "funcionario":
    if idade_usuario >= 18 and cargo == "pleno":
        permitido_acesso = True
    else:
        permitido_acesso = False

elif tipo_usuario == "visitante":
    permitido_acesso = False

else:
    print("Tipo usuário não reconhecido!")


if permitido_acesso == True:
    status_acesso = "permitido".upper()
else:
    status_acesso = "negado".upper()


#exibindo na tela
mensagem_final = f""" 
Usuário: {nome_usuario}
Idade: {idade_usuario}
Tipo: {tipo_usuario}
Status de acesso: {status_acesso}
"""

print(mensagem_final)