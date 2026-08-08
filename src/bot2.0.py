from selenium import webdriver
import openpyxl
import time
from urllib.parse import quote
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Navegador abrindo...")
navegador = webdriver.Chrome()

navegador.maximize_window()

print("whatsapp abrindo...")
navegador.get("https://web.whatsapp.com")

print("Conectar com seu whatsapp em 1 minuto!")
time.sleep(60)
print("Whatsapp conectado com sucesso!")

arquivo = openpyxl.load_workbook("clientes_teste.xlsx")
aba = arquivo.active

for linha in aba.iter_rows(min_row=2, values_only=True):
    nome = linha[0]
    telefone = str(linha[1])
    vencimento = linha[2]

    print(f"Enviando mensagem para {nome} - {telefone}")

      # Criar mensagem
    mensagem = (
        f"Olá {nome}! "
        f"Seu boleto vence no dia {vencimento.strftime('%d/%m/%Y')}. "
        f"Favor realizar o pagamento pelo link: "
        f"https://www.link_do_pagamento.com"
    )

    #Criar url da conversa
    url = f"https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}"

    navegador.get(url)

    # Esperar a conversa carregar
    time.sleep(8)

    # Enviar
    botao_enviar = WebDriverWait(navegador, 30).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//button[@aria-label="Enviar"]')
    )
)

    botao_enviar.click()
    print(f"Mensagem enviada para {nome}")

    # Esperar antes do próximo cliente
    time.sleep(5)

print("Todos os clientes foram processados!")