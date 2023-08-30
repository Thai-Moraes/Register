# Estava tendo aula de Banco de Dados então pensei que seria divertido tentar fazer algo do tipo em Python, um sistema de planilha no Python.

import re
import fileinput
import string
def register():

    res = int(input('''- O que você deseja fazer?
    1. Cadastro no Sistema
    2. Login no Sistema
    3. Recuperar Senha de Cadastro
    '''))

    if res == 1:
        loop = True
        usuario = input("Usuario: ").strip()

        dados = open('cadastro.txt', 'r').read()

        while loop:
            if re.search(r'\b'+ re.escape(usuario) + r'\b', dados, re.MULTILINE):
                usuario = input("Usuario já cadastrado! Tente outro nome de usuario!\nUsuario: ")
            else:
                loop = False

        senha = input("Senha: ")
        chave = input("Chave de Segurança (nome de animal, ano importante etc. Necessária para caso perca sua conta): ")

        dados = open('cadastro.txt', 'a+').write(f"\n{usuario} - {senha} - {chave}")

    if res == 2:
        loop = True

        usuario = input("Usuario: ")
        senha = input("Senha: ")

        dados = open('cadastro.txt', 'r').read()

        if re.search(r'\b' + re.escape(f"{usuario} - {senha}") + r'\b', dados, re.MULTILINE):
            print("Você acessou o sistema!!\n")
        else:
            print("Senha ou Usuario incorretos! Tente Novamente!\n")

    if res == 3:
        usuario = input("Informe seu Usuario: ")
        chave = input("Informe a sua Chave de acesso: ")

        dados = open('cadastro.txt', 'r').read()

        for line in open('cadastro.txt', 'r').readlines():
            if usuario in line and chave in line:
                senhanova = input("Informe a sua nova senha: ")
                if line.strip().startswith(usuario):
                    line = usuario + " - " + senhanova + " - " + chave
            f = open("cadastro.txt", "w")
            f.write("" + line)
            f.close()
        if usuario not in line and chave not in line:
            print("Usuario ou Chave Incorretos!\n")

while True:
    register()
