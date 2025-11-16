import class_main, os, sys, socket, json, threading, time

#Seleção do menu
while True:
    os.system("clear")
    print("+-----------------------------------+")
    print("| Seja bem vindo!                   |")   
    print("+-----------------------------------+")  
    print("|[1]- Chat Local                    |")
    print("|[2]- Scan Subdomain                |")      
    print("|[3]- Scanport                      |")
    print("|[4]- Dirb                          |")
    print("|                                   |")
    print("|[99]- Sair                         |")    
    print("+-----------------------------------+")   
    opc_menu = int(input("Digite uma opção: "))

    if opc_menu == 1:
        while True:
            os.system("clear")
            print("+-----------------------------------+")
            print("| Mode: Chat local                  |")   
            print("+-----------------------------------+")  
            print("|[1]- Servidor/tcp                  |")
            print("|[2]- Cliente/tcp                   |")   
            print("|                                   |")
            print("|[99]- Voltar                       |")    
            print("+-----------------------------------+")   
            opc_chat = int(input("Digite uma opção: "))
            chatlocal = class_main.chatlocal
            if opc_chat == 1:
                chatlocal.servidor()
            elif opc_chat == 2:
                chatlocal.cliente()
            elif opc_chat == 99:
                break
            elif opc_chat not in ["1", "2", "99"]:
                print("\033[F", end="")  
                print(f"Esta opção não está disponível..")
                time.sleep(2)
    elif opc_menu == 2:
        while True:
            os.system("clear")
            print("+-----------------------------------+")
            print("| Mode: Scan Subdomain              |")   
            print("+-----------------------------------+")  
            print("|[1]- IPV4/IPV6                     |")
            print("|[2]- TakeOver                      |") 
            print("|[3]- ALL                           |")  
            print("|                                   |")
            print("|[99]- Voltar                       |")    
            print("+-----------------------------------+") 
            opc_sub = int(input("Digite uma opção: "))
            if opc_sub == 1:
                subdomain = class_main.subdomain
                subdomain.ipv4_ipv6()
            elif opc_sub == 2:
                takeover = class_main.subdomain
                takeover.takeover_sub()
            elif opc_sub == 3:
                all_sub = class_main.subdomain
                all_sub.all_sub()
            elif opc_sub == 99:
                break
            elif opc_sub not in ["1", "2", "3", "99"]:
                print("\033[F", end="")  
                print(f"Esta opção não está disponível..")
                time.sleep(2)
    



    elif opc_menu == 3:
        while True:
            os.system("clear")
            print("+-----------------------------------+")
            print("| Mode: ScanPort                    |")   
            print("+-----------------------------------+")  
            print("|[1]- ScanPort Full                 |")
            print("|[2]- Scanport Wordist              |")   
            print("|[3]- ScanPort SYN Scan             |")
            print("|                                   |")
            print("|[99]- Voltar                       |")    
            print("+-----------------------------------+") 
            opc_scan = int(input("Digite uma opção: "))
            scanport = class_main.scanport
            if opc_scan == 1:
                scanport = class_main.scanport
                scanport.scanport_full()
                input("Digite ENTER para voltar..")
            elif opc_scan == 2:
                scanport = class_main.scanport
                scanport.scanport_wordlist()
                input("Digite ENTER para voltar..")
            elif opc_scan == 3:
                synscan = class_main.scanport
                synscan.syn_scan()
            elif opc_scan == 99:
                break
            elif opc_scan not in ["1", "2", "3", "99"]:
                print("\033[F", end="")  
                print(f"Esta opção não está disponível..")
                time.sleep(2)
    elif opc_menu == 4:
        dirb = class_main.dirb
        dirb.dirb()
    elif opc_menu == 99:
        os.system("clear")
        exit()
    elif opc_menu not in ["1", "2", "3", "99"]:
        print("\033[F", end="")  
        print(f"Esta opção não está disponível..")
        time.sleep(2)
