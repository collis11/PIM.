import json
import hashlib
import os
import statistics

USUARIOS_FILE = 'usuarios.json'
PROGRESSO_FILE = 'progresso.json'

if not os.path.exists(USUARIOS_FILE):
    with open(USUARIOS_FILE, 'w') as f:
        json.dump({}, f)
if not os.path.exists(PROGRESSO_FILE):
    with open(PROGRESSO_FILE, 'w') as f:
        json.dump({}, f)

def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

while True:
    print("""
1- Cadastrar
2- Login
3- Sair
""")
    
    escolha = int(input("Escolha uma opçao: "))

    if escolha == 1:
        with open(USUARIOS_FILE, "r") as f:
            usuarios = json.load(f)

        nome = str(input("Digite um nome de usuario: ")).strip()
        if nome in usuarios:
            print("O nome inserido ja esta sendo utilizado.")
            continue
        else:
            while True:
                senha = str(input("Digite uma senha forte : ")).strip()

                if len(senha) < 8:
                    print("A senha deve ter no mínimo 8 caracteres.")
                    continue

                tem_maiuscula = False
                tem_minuscula = False
                tem_numero = False
                tem_simbolo = False
                simbolos = "!@#$%^&*()_+-=[]{},.<>?/|\\"

                for caractere in senha:
                    if 'A' <= caractere <= 'Z':
                        tem_maiuscula = True
                    elif 'a' <= caractere <= 'z':
                        tem_minuscula = True
                    elif '0' <= caractere <= '9':
                        tem_numero = True
                    elif caractere in simbolos:
                        tem_simbolo = True

                if tem_maiuscula and tem_minuscula and tem_numero and tem_simbolo:
                    break
                else:
                    print("Senha fraca! Use letras maiúsculas, minúsculas, números e símbolos.")

            senha_crip = hashlib.sha256(senha.encode()).hexdigest()
            usuarios[nome] = senha_crip
            salvar_dados(USUARIOS_FILE, usuarios)
            print("Usuario cadastrado.")

    elif escolha == 2:
        with open(USUARIOS_FILE, "r") as f:
            usuarios = json.load(f)
        nome = str(input("Usuario: "))
        senha = str(input("Senha: "))
        senha_crip = hashlib.sha256(senha.encode()).hexdigest()

        if nome in usuarios and usuarios[nome] == senha_crip:
            print(f"Bem-vindo(a), {nome}.")
            print("")

            while True:
                print("""1- Acessar aulas
2- Registrar notas
3- Relatorio
4- Logout
""")
                escolha2 = int(input("Escolha: "))
                if escolha2 == 1:
                    while True:
                        print("""Aulas Disponiveis:
1- O que e logica computacional?
2- Introducao ao python
3- Boas praticas de seguranca
4- Sair
""")
                        escolha3 = int(input("Escolha uma aula: "))
                        if escolha3 == 1:
                            print("-=-"*10)
                            print("""A lógica computacional discute o uso de raciocínio em alguma atividade e é o estudo normativo, filosófico do raciocínio válido. 
Um jeito de organizar ideias para problemas ou atender demandas. O modo de pensar da logica computacional é uma forma estruturada, desenhando um encadeamento de etapas sequencial e com condições e não 
servem só para programar,  muito usual para resolver quaisquer tipos de problemas do dia a dia. 
A lógica é importante pois quando você esta programando um site é preciso fazer um manual de instruções bem minucioso para que o destinatária consiga usar o seu produto, caso você falhe nessa sequência, 
o resultado pode não ir tão bem.""")
                        elif escolha3 == 2:
                            print("-=-"*10)
                            print("""      O Python é uma linguagem de programação  para back-end(código que conecta a internet com o banco de dados) amplamente usada em aplicações da Web, desenvolvimento de software, ciência de dados e 
machine learning (ML). 
 As pessoas usam o Python para a manutenção do controle de erros no código, construção automática do software, desenvolvimento de prototipos de software e muitas mais outras funcionalidades. 
Esta linguagem é usada como Panda, Scipy e Numpy, fazendo dela a linguagem preferida para análise de dados, machine learning e inteligência aritificial.
Para começar a estudar Python primeiramente instale o Python no site https://python.org, tem como você usar editores como IDLE do Python, VS Code e PyCharm. Comece com scripts simples e vá aumentando o 
nível de dificuldade deles, tente sempre pratica-los para fixar na mente.""")
                        elif escolha3 == 3:
                            print("-=-"*10)
                            print("""Usar antivírus corporativo, segurança de ponta com baixo custo
Usar Firewall UTM, proteção em tempo real contra hackers 
Fazer backup em nuvem, recupera rapidamente em caso de perca de arquivos 
Crie senhas longas,  que não tenham seu nome, coloque letras maiúsculas e minúsculas e use símbolos como por exemplo: @#$ ...
Use autentificação de dois fatores, é melhor usar o google em vez de SMS 
Sempre desconfie de E-mails e links, nunca clique em links de desconhecidos ou E-mails pois podem conter virús dentro deles""")
                        if escolha3 == 4:
                            break
                if escolha2 == 2:
                    with open(PROGRESSO_FILE, "r") as f:
                        progresso = json.load(f)
                    try:
                        nota = float(input("Digite sua nota (0 a 10): "))
                        if nota < 0 or nota > 10:
                            print("Digite um numero de 0 a 10!")
                            continue
                    except ValueError:
                        print("Digite um numero valido!")
                        continue

                    if nome not in progresso:
                        progresso[nome] = []
                    progresso[nome].append(nota)

                    salvar_dados(PROGRESSO_FILE, progresso)
                    print("Notas registradas!")

                if escolha2 == 3:
                    with open(PROGRESSO_FILE, "r") as f:
                        progresso = json.load(f)

                    print("---Relatorio---")
                    print("")
                    todas_notas = []
                    for i, notas in progresso.items():
                        print(f"{i}: notas = {notas}")
                        todas_notas.extend(notas)
                            
                        if todas_notas:
                            media = statistics.mean(todas_notas)
                            print(f"Média geral: {media:.2f}")
                            print("")
                        else:
                            print("Nenhuma nota registrada.")

                elif escolha2 == 4:
                    print("Logout efetuado.")
                    break
        else:
            print("Usuário ou senha incorretos.")

    elif escolha == 3:
        print("Saindo...")
        break
    else:
        print("Opção inválida.")