from autoscraper import AutoScraper
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

palavras_chave = "lenovo core i9"

def buscar_melhor_preco(palavras_chave):
    with open(r'C:\Users\mvros\Documents\ChatBot_Comparador_de_preços-20250411T135948Z-002\ChatBot_LLM_Lhama\app\ecommerce_config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)

    resultados = []

    for site in config:
        navegador = None
        try:
            url = site["url_base"]
            xpath = site["xpath_busca"]
            modelo_scraper = site["modelo_scraper"]

            navegador = webdriver.Chrome()
            navegador.get(url)

            # Espera até o campo de busca estar visível
            campo_busca = WebDriverWait(navegador, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            campo_busca.clear()
            campo_busca.send_keys(palavras_chave)
            campo_busca.send_keys(Keys.RETURN)

            # Espera a página de resultados carregar
            time.sleep(5)

            # Carrega o modelo treinado do AutoScraper
            scraper = AutoScraper()
            scraper.load(modelo_scraper)

            resultados_parciais = scraper.get_result_similar(navegador.page_source, grouped=True)

            # Filtra resultados agrupados com preço (R$)
            ofertas = []
            for key, values in resultados_parciais.items():
                if any("R$" in v for v in values):
                    ofertas.append(values)

            resultados.append({site["nome"]: ofertas})

        except Exception as e:
            resultados.append({site["nome"]: f"Erro: {str(e)}"})

        finally:
            if navegador:
                try:
                    navegador.quit()
                except:
                    pass

    return resultados


resultados = buscar_melhor_preco(palavras_chave)
for r in resultados:
    print(json.dumps(r, indent=2, ensure_ascii=False))
