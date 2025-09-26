import requests
import threading

# *************** The ONIX ***************
onix_art = r"""
___           ___                       ___      
     /\  \         /\  \                     /|  |     
    /::\  \        \:\  \       ___         |:|  |     
   /:/\:\  \        \:\  \     /\__\        |:|  |     
  /:/  \:\  \   _____\:\  \   /:/__/      __|:|__|     
 /:/__/ \:\__\ /::::::::\__\ /::\  \     /::::\__\_____
 \:\  \ /:/  / \:\~~\~~\/__/ \/\:\  \__  ~~~~\::::/___/
  \:\  /:/  /   \:\  \        ~~\:\/\__\     |:|~~|    
   \:\/:/  /     \:\  \          \::/  /     |:|  |    
    \::/  /       \:\__\         /:/  /      |:|__|    
     \/__/         \/__/         \/__/       |/__/     
"""
# **********************************************
url = "https://"
numero_de_requisicoes_simultaneas = 10
# **********************************************

def fazer_requisicao(numero):
    try:
        print(f"[Requisição {numero}] Iniciada...")
        resposta = requests.get(url)
        print(f"[Requisição {numero}] Concluída! Status: {resposta.status_code}")
    except Exception as e:
        print(f"[Requisição {numero}] FALHOU! Erro: {e}")

print(onix_art)
print(">>> Script de Teste de Carga - Onix <<<")
print(f"Alvo: {url}")
print(f"Simulando {numero_de_requisicoes_simultaneas} usuários simultâneos.")
print("=" * 50)

threads = []
for i in range(numero_de_requisicoes_simultaneas):
    t = threading.Thread(target=fazer_requisicao, args=(i+1,))  
    threads.append(t)
    t.start()  

for t in threads:
    t.join()

print("=" * 50)
print("Teste Onix concluído.")