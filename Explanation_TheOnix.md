# Explicação do Script de Carga "Onix"
## Explanation of the 'Onix' Load Script

Este arquivo explica como funciona o script Python "Onix", uma ferramenta simples para realizar testes de carga em um servidor web. Ele simula múltiplos acessos simultâneos a uma URL específica para verificar seu desempenho.

This file explains how the "Onix" Python script works, a simple tool for performing load tests on a web server. It simulates multiple simultaneous requests to a specific URL to check its performance.

O código-fonte está no arquivo `teste_de_carga.py`.
The source code is in the `teste_de_carga.py` file.

---

## Como funciona | How it works

1.  **Configuração do Alvo / Target Configuration**
    No início do script, o usuário define duas variáveis principais: a `url` que será o alvo do teste e o `numero_de_requisicoes_simultaneas`, que determina quantos "usuários" virtuais acessarão o site ao mesmo tempo.
    At the beginning of the script, the user defines two main variables: the target `url` for the test and the `numero_de_requisicoes_simultaneas`, which determines how many virtual "users" will access the site at the same time.

2.  **Requisição HTTP / HTTP Request**
    A função `fazer_requisicao` é o coração de cada acesso. Ela utiliza a biblioteca `requests` para enviar uma requisição `GET` para a URL alvo e imprime na tela se a requisição foi bem-sucedida (com o status code, ex: 200 para OK) ou se falhou.
    The `fazer_requisicao` function is the core of each request. It uses the `requests` library to send a `GET` request to the target URL and prints to the console whether the request was successful (with the status code, e.g., 200 for OK) or if it failed.

3.  **Simultaneidade com Threads / Concurrency with Threads**
    Para simular acessos simultâneos, o script usa a biblioteca `threading`. Em vez de fazer uma requisição de cada vez, ele cria um "thread" (uma linha de execução separada) para cada uma das requisições.
    To simulate simultaneous access, the script uses the `threading` library. Instead of making one request at a time, it creates a "thread" (a separate line of execution) for each request.

4.  **Execução e Sincronização / Execution and Synchronization**
    Um laço `for` cria e inicia todos os threads quase que instantaneamente. Depois de iniciar todos eles, um segundo laço com `t.join()` garante que o script principal espere até que a última requisição seja concluída antes de exibir a mensagem final.
    A `for` loop creates and starts all the threads almost instantly. After starting them all, a second loop with `t.join()` ensures that the main script waits until the very last request is completed before printing the final message.

---

## Código comentado | Commented code

```python
# Importa as bibliotecas necessárias
# Imports the necessary libraries
import requests
import threading

# *************** The ONIX ***************
# ASCII art para dar identidade ao script
# ASCII art to give the script an identity
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
# Variáveis de configuração que o usuário deve alterar
# Configuration variables that the user should change
url = "https://"
numero_de_requisicoes_simultaneas = 10
# **********************************************

# Função que será executada por cada thread
# Function that will be executed by each thread
def fazer_requisicao(numero):
    try:
        # Informa que a requisição começou
        # Informs that the request has started
        print(f"[Requisição {numero}] Iniciada...")
        
        # Envia a requisição GET para a URL alvo
        # Sends the GET request to the target URL
        resposta = requests.get(url)
        
        # Informa que a requisição terminou e mostra o status
        # Informs that the request has finished and shows the status
        print(f"[Requisição {numero}] Concluída! Status: {resposta.status_code}")
    except Exception as e:
        # Em caso de erro, informa a falha
        # In case of an error, reports the failure
        print(f"[Requisição {numero}] FALHOU! Erro: {e}")

# Imprime o cabeçalho do script
# Prints the script header
print(onix_art)
print(">>> Script de Teste de Carga - Onix <<<")
print(f"Alvo: {url}")
print(f"Simulando {numero_de_requisicoes_simultaneas} usuários simultâneos.")
print("=" * 50)

# Lista para armazenar todos os threads criados
# List to store all the created threads
threads = []

# Loop para criar e iniciar os threads
# Loop to create and start the threads
for i in range(numero_de_requisicoes_simultaneas):
    # Cria o thread, definindo a função alvo e seus argumentos
    # Creates the thread, setting the target function and its arguments
    t = threading.Thread(target=fazer_requisicao, args=(i+1,))  
    threads.append(t)
    
    # Inicia a execução do thread
    # Starts the thread's execution
    t.start()  

# Loop para esperar que todos os threads terminem
# Loop to wait for all threads to finish
for t in threads:
    # O método .join() pausa o script principal até que o thread 't' finalize
    # The .join() method pauses the main script until the 't' thread finishes
    t.join()

print("=" * 50)
print("Teste Onix concluído.")
