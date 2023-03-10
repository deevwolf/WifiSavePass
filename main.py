#Script By Wolf
#Script Feito Para Pegar Senhas Salvas Do Computador, útil caso Seu Windows Esteja Conectado Em Uma Rede Wi-fi Que Você Não Sabe o Password.


#importações
import colorama,time,os
import webbrowser as wb
from colorama import Fore
def script():
    os.system("cls")
    print(Fore.GREEN + """     __          ___  __ _        _____              
     \ \        / (_)/ _(_)      |  __ \             
      \ \  /\  / / _| |_ _ ______| |__) |_ _ ___ ___ 
       \ \/  \/ / | |  _| |______|  ___/ _` / __/ __|
        \  /\  /  | | | | |      | |  | (_| \__ \__ \

         \/  \/   |_|_| |_|      |_|   \__,_|___/___/ """)
    print(Fore.BLUE +"                                               @WolfOFCC")  
    print("")
    print(Fore.GREEN + "Escolha Uma Opção Abaixo: ")
    print(Fore.WHITE + "################################################################")
    print(Fore.WHITE + "[" + Fore.GREEN + "01" + Fore.WHITE + "]" + " - " + "Listar Redes Wi-fi Conectadas" )
    print(Fore.WHITE + "[" + Fore.GREEN + "02" + Fore.WHITE + "]" + " - " + "Pegar A Senha De Uma Rede Wi-fi " )
    print(Fore.WHITE + "[" + Fore.RED + "99" + Fore.WHITE + "]" + " - " + "Meu Github" )
    print(Fore.WHITE + "################################################################")
    menu_opcao = input(Fore.GREEN + ">> ")
    if menu_opcao == '99':
        print(Fore.GREEN + "OK ! Estou Redirecionando Você Para o Meu GitHub.")
        time.sleep(2)
        wb.open('https://github.com/deevwolf')
        time.sleep(2)
        script()
    elif menu_opcao == '01':
        print(Fore.WHITE + "[" + Fore.YELLOW + "i" + Fore.WHITE + "]" + " - " + "Sempre Use Esse Script Como 'Executar Como Administrador'" )
        time.sleep(1)
        print(Fore.WHITE + "[" + Fore.GREEN + "✅" + Fore.WHITE + " ]" + " - " + "Redes De Wi-fi Conectadas Abaixo: " )
        os.system("netsh wlan show profile")
        print(Fore.WHITE + "[" + Fore.YELLOW + "i" + Fore.WHITE + "]" + " - " + "Anote o Nome Da Rede Wi-fi Desejada Que Estará Depois Do" + Fore.CYAN + " 'All User Profile :'" + Fore.WHITE + "Pois Irá Precisa-lo Na Etapa 2")
        lista_wifi = input(Fore.GREEN + "Pressione  Qualquer Tecla Para Voltar Ao Menu ... ")
        script()
    elif menu_opcao == '02':
        print(Fore.WHITE + "[" + Fore.YELLOW + "i" + Fore.WHITE + "]" + " - " + "Sempre Use Esse Script Como 'Executar Como Administrador'" )
        time.sleep(1)
        print(Fore.WHITE + "[" + Fore.YELLOW + "i" + Fore.WHITE + "]" + " - " + "Um Arquivo .xml Será Criado No Local" + Fore.BLUE + " C:\ " + Fore.WHITE + "Abra O Arquivo Que Terá O Nome Da Rede Wi-fi Desejada  Usando Algum Edito De Texto " )
        print(Fore.WHITE + "[" + Fore.YELLOW + "i" + Fore.WHITE + "]" + " - " + "A Senha Estará Aproximadamente Na Linha " + Fore.BLUE + "22" + Fore.WHITE + "Ao Lado Do keyMaterial" )
        os.system("netsh wlan export profile folder=C:\ key=clear")
        print(Fore.WHITE + "[" + Fore.GREEN + "✔" + Fore.WHITE + "]" + " - " + "A Senha Foi Salva Com Sucesso! Verifique Seu Disco Local C ")
        time.sleep(5)
        script()
    else:
        print(Fore.WHITE + "[" + Fore.RED + "!" + Fore.WHITE + "]" + " - " + "Opção Inválida!" + Fore.BLUE + "" + Fore.WHITE + "" )
        time.sleep(1)
        script()

script()
