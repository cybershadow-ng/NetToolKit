from scapy.all import IP, TCP, sr, L3RawSocket, conf, RandShort #type:ignore
import socket, os, sys, getpass, json, threading
import dns.resolver #type:ignore

class chatlocal:
	def servidor():
		os.system("clear")
		print("+-------------------------------------------------+")
		print(f"| IP LOCAL: [0.0.0.0] [127.0.0.1] [localhost]     |")
		print("+-------------------------------------------------+\n")
		ip = input("Digite seu IP: ")
		port = int(input("Digite a porta: "))

		os.system("clear")
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((ip, port))
		s.listen(1)
		print("Esperando cliente..")
		con, client = s.accept()

		os.system("clear")
		print("+-----------------------------------+")
		print(f"|     [+]Conectado ao {client[0]}     |")
		print("+-----------------------------------+\n")
		con.send("Digite a senha: ".encode())
		senha = con.recv(1024)

		if senha.decode() == "admin":
			while True:
				msg = input("Host: ")
				con.send(msg.encode())
				dados = con.recv(1024)
				print(f"{client[0]}: {dados.decode()}")
		else:
			print("Senha incorreta, conexão encerrada!")	

	def cliente():
		os.system("clear")
		ip = input("Digite o IP: ")
		port = int(input("Digite a Porta: "))
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		os.system("clear")
		try:
			s.connect((ip,port))
			msg = s.recv(1024).decode()
			senha = getpass.getpass(msg)
			s.send(senha.encode())
			os.system("clear")
			print("+-------------------------------------+")
			print(f"|   [+]Conectado ao {ip}      |")
			print("+-------------------------------------+")
			while True:
				print(f"\nAdmin: {s.recv(1024).decode()}")
				msg = input(">> ")
				msg = msg + "\n"
				s.send(msg.encode())
		except ConnectionRefusedError:
			input("Este servidor não esta aberto!")




class subdomain:
	def ipv4_ipv6():
		os.system("clear")
		def ipv4():
			try:
				dados = socket.getaddrinfo(ip_ipv4, None, socket.AF_INET)
				print(f"\n{dominio_montado} - {dados[0][4][0]}")
				return dados[0][4][0]
			except socket.gaierror:
				None
		def ipv6():
			try:
				dados = socket.getaddrinfo(ip_ipv6, None, socket.AF_INET6)
				print(f"\t{dominio_montado} - {dados[0][4][0]}")
				return dados[0][4][0]
			except socket.gaierror:
				None
		def host_ipv4():
			try:
				dados_host = socket.getaddrinfo(dominio_montado, None, socket.AF_INET)
				return dados_host[0][4][0]
			except socket.gaierror:
				None
		def host_ipv6():
			try:
				dados_host = socket.getaddrinfo(dominio_montado, None, socket.AF_INET6)
				return dados_host[0][4][0]
			except socket.gaierror:
				None
		dominio = input("Digite seu domínio: ")
		consultado = []
		logs = {}
		os.system("clear")
		print("+-----------------------------------+")
		print(f"| Domain: {dominio}                |")   
		print("+-----------------------------------+")
		with open("wordlist_subdomain.txt") as wordlist:
			for i in wordlist.readlines():
				i = i.replace("\n", "")
				dominio_montado = f"{i}.{dominio}"
				if dominio_montado not in consultado:
					ip_ipv4 = host_ipv4()
					ip_ipv6 = host_ipv6()
					addr4 = ipv4()
					addr6 = ipv6()
					consultado.append(dominio_montado)
					logs[dominio_montado] = (addr4, addr6)
		with open(f"{dominio}_subdomain_logs", "w") as f:
			logs_json = json.dumps(logs)
			f.write(logs_json)
	
	
	
	
	def takeover_sub():
		def takeover():
			try:
				dados = dns.resolver.resolve(dominio_montado, "CNAME")
				cname = str(dados[0].target)
				print(f"{dominio_montado} --> {cname}")
				return cname
			except (socket.gaierror, dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.DNSException):
				return None
		os.system("clear")
		dominio = input("Digite seu domínio: ")
		consultado = []
		logs = {}
		os.system("clear")
		print("+-----------------------------------+")
		print(f"| Domain: {dominio}                |")   
		print("+-----------------------------------+\n")
		with open("wordlist_subdomain.txt") as wordlist:
			for i in wordlist.readlines():
				i = i.replace("\n", "")
				dominio_montado = f"{i}.{dominio}"
				if dominio_montado not in consultado:
					cname_resultado = takeover()
					consultado.append(dominio_montado)
					logs[dominio_montado] = (cname_resultado)
					
		with open(f"{dominio}_cname.logs", "w") as f:
			logs_json = json.dumps(logs)
			f.write(logs_json)
			input("\nDigite ENTER para retornar..")
	
	
	
	def all_sub():
		os.system("clear")
		def ipv4():
			try:
				dados = socket.getaddrinfo(ip_ipv4, None, socket.AF_INET)
				print(f"\n[IPV4] {dominio_montado} - {dados[0][4][0]}")
				return dados[0][4][0]
			except socket.gaierror:
				None
		def ipv6():
			try:
				dados = socket.getaddrinfo(ip_ipv6, None, socket.AF_INET6)
				print(f"[IPV6] {dominio_montado} - {dados[0][4][0]}")
				return dados[0][4][0]
			except socket.gaierror:
				None
		def takeover():
			try:
				dados = dns.resolver.resolve(dominio_montado, "CNAME")
				cname = str(dados[0].target)
				print(f"[TAKEOVER] {dominio_montado} --> {cname}")
				return cname
			except (socket.gaierror, dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.DNSException):
				return None
		def host_ipv4():
			try:
				dados_host = socket.getaddrinfo(dominio_montado, None, socket.AF_INET)
				return dados_host[0][4][0]
			except socket.gaierror:
				None
		def host_ipv6():
			try:
				dados_host = socket.getaddrinfo(dominio_montado, None, socket.AF_INET6)
				return dados_host[0][4][0]
			except socket.gaierror:
				None
		
		
		dominio = input("Digite seu domínio: ")
		consultado = []
		logs = {}
		os.system("clear")
		print("+-----------------------------------+")
		print(f"| Domain: {dominio}                |")   
		print("+-----------------------------------+")
		with open("wordlist_subdomain.txt") as wordlist:
			for i in wordlist.readlines():
				i = i.replace("\n", "")
				dominio_montado = f"{i}.{dominio}"
				if dominio_montado not in consultado:
					ip_ipv4 = host_ipv4()
					ip_ipv6 = host_ipv6()
					addr4 = ipv4()
					addr6 = ipv6()
					cname_resultado = takeover()
					consultado.append(dominio_montado)
					logs[dominio_montado] = (addr4, addr6, cname_resultado)
		with open(f"{dominio}_subdomain_logs", "w") as f:
			logs_json = json.dumps(logs)
			f.write(logs_json)
			input("\nDigite ENTER para retornar..")
	



class scanport:
	def scanport_full():
			import socket, os
			os.system("clear")
			dominio = input("Digite o domínio: ")
			os.system("clear")
			print("+-----------------------------------+")
			print(f"| Domain: {dominio}                |")   
			print("+-----------------------------------+")
			for port in range(55356):
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.settimeout(0.1)
				print(port)
				if s.connect_ex((dominio, port)) == 0:
					print(f"{port}/tcp encontrada!")
				else:
					None
	
	
	
	def scanport_wordlist():
		os.system("clear")
		dominio = input("Digite o domínio: ")
		os.system("clear")
		print("+-----------------------------------+")
		print(f"| Domain: {dominio}                |")   
		print("+-----------------------------------+")
		with open("wordlist_ports.txt") as wordlist:
			for port in wordlist.readlines():
				port = int(port)
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.settimeout(0.1)
				if s.connect_ex((dominio, port)) == 0:
					print(f"{port}/tcp encontrada!")
				else:
					None
	
	
	def syn_scan():
		os.system("clear")
		host = input("Digite o domínio: ") 
		os.system("clear")
		print("+-----------------------------------+")
		print(f"| Domain: {host}                |")   
		print("+-----------------------------------+")
		conf.L3socket = L3RawSocket
		conf.verb = 0

		for port in range(65536):
			pacote_ip = IP(dst=host)
			pacote_tcp = TCP(
				dport = port, #A porta destino
				sport = RandShort(), #Porta aleátoria não aberta para se comunicar
				flags = "S", #SYN
				seq = 1000,
				options = [("MSS", 1460),("NOP", None),("WScale", 7)]
			)

			pkg, unpkg = sr(pacote_ip/pacote_tcp, timeout=0.1) 

			if pkg:
				for snd, rcv in pkg:
					if rcv.haslayer(TCP):
						if rcv[TCP].flags == 0x012:
							print(f"{port}/tcp aberta!")