# Onix - Teste de Carga Simples

Onix é um script simples em Python para realizar testes de carga básicos em um servidor web. Ele utiliza `threading` para disparar múltiplas requisições HTTP GET simultaneamente, ajudando a verificar como o servidor se comporta sob um estresse moderado.

Onix is a simple Python script for performing basic load tests on a web server. It uses `threading` to fire multiple simultaneous HTTP GET requests, helping to check how the server behaves under moderate stress.

---

## Funcionalidades | Features

* **Simulação de Múltiplos Usuários / Multi-User Simulation:**
    Cria threads para simular vários usuários acessando uma URL ao mesmo tempo.
    Creates threads to simulate multiple users accessing a URL at the same time.
* **Configuração Fácil / Easy Setup:**
    Basta alterar duas variáveis no início do script para definir o alvo e a intensidade do teste.
    Just change two variables at the beginning of the script to set the target and the intensity of the test.
* **Feedback em Tempo Real / Real-Time Feedback:**
    Exibe o status de cada requisição (iniciada, concluída ou falha) diretamente no terminal.
    Displays the status of each request (initiated, completed, or failed) directly in the terminal.

## Requisitos | Requirements

* Python 3
* Biblioteca `requests`

## Como Usar | How to Use

1.  **Baixe o Script / Download the Script**
    Faça o download do arquivo `teste_de_carga.py`.
    Download the `teste_de_carga.py` file.

2.  **Instale as Dependências / Install Dependencies**
    Se você não tiver a biblioteca `requests` instalada, execute o comando abaixo no seu terminal:
    If you don't have the `requests` library installed, run the command below in your terminal:
    ```bash
    pip install requests
    ```

3.  **Configure o Alvo / Configure the Target**
    Abra o arquivo `teste_de_carga.py` e edite as seguintes variáveis para o seu teste:
    Open the `teste_de_carga.py` file and edit the following variables for your test:
    ```python
    # **********************************************
    url = "[https://seusite.com](https://seusite.com)"
    numero_de_requisicoes_simultaneas = 50
    # **********************************************
    ```

4.  **Execute o Script / Run the Script**
    Rode o script pelo terminal:
    Run the script from the terminal:
    ```bash
    python teste_de_carga.py
    ```

## Aviso | Disclaimer

Use este script com responsabilidade. Realizar testes de carga em servidores sem a devida permissão pode ser considerado um ataque (DoS) e violar os termos de serviço do provedor de hospedagem. Utilize apenas em servidores que você possui ou tem autorização explícita para testar.

Use this script responsibly. Performing load tests on servers without proper permission can be considered a DoS attack and may violate the hosting provider's terms of service. Only use it on servers that you own or have explicit authorization to test.
