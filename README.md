# NetToolKit 🛠️

Uma ferramenta multifuncional desenvolvida em **Python**, incluindo:

- **Chat TCP local** — converse com outros dispositivos na sua rede.  
- **Scanner de subdomínios** — descubra subdomínios de um domínio alvo.  
- **Scanner de portas** — verifique portas abertas de forma rápida.  
- **Scanner Dirb** — encontre diretórios e arquivos ocultos em servidores web.  

> ⚠️ **Atenção:** Este projeto foi testado apenas em Linux.

---

## 🚀 Requisitos

- Linux (qualquer distribuição moderna)  
- Python 3.x  
- pip3  

Este projeto depende das seguintes bibliotecas:

- `dnspython`  
- `scapy`  
- `requests`  

---

## 🐍 Configurando o ambiente virtual

Para evitar conflitos de dependências, é recomendado criar um **ambiente virtual**:

```bash
# Criar o ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate
