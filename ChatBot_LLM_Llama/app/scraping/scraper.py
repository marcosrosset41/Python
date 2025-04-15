import json
import time
from autoscraper import AutoScraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def carregar_sites(path_json=r"C:\Users\mvros\Documents\ChatBot_Comparador_de_preços-20250411T135948Z-002\ChatBot_LLM_Llama\app\ecommerce_config.json"):
    with open(path_json, "r", encoding="utf-8") as f:
        return json.load(f)


def buscar_produto(site, palavra_chave):
    print(f"\n🔍 Buscando por: {palavra_chave} em {site['nome']}")

    # Configurações do navegador (headless)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    navegador = webdriver.Chrome(options=options)

    # Abrir o site
    navegador.get(site["url_base"])
    time.sleep(2)

    # Buscar pela palavra-chave
    barra_busca = navegador.find_element(By.XPATH, site["xpath_busca"])
    barra_busca.send_keys(palavra_chave)
    barra_busca.send_keys(Keys.RETURN)
    time.sleep(10)

    # Carregar o modelo do AutoScraper
    scraper = AutoScraper()
    scraper.load(site["modelo_scraper"])

    # verificando o html retornado
    print("\n📄 Trecho do HTML:")
    print(navegador.page_source[:1000])
    # Buscar dados semelhantes àqueles treinados
    resultados = scraper.get_result_similar(html=navegador.page_source, grouped=True)
    navegador.quit()

    print("⚙️ Resultados brutos encontrados pelo modelo:", resultados)
    return resultados


def extrair_ranking(resultados):
    produtos = resultados.get("rule_redn", [])
    precos = resultados.get("rule_69tg", [])

    if not produtos or not precos:
        print("⚠️ Nenhum produto ou preço encontrado.")
        return []

    # Garantir mesmo tamanho entre listas
    pares = list(zip(produtos[:len(precos)], precos[:len(produtos)]))

    # Limpar e converter preços para float
    ranking = []
    for produto, preco in pares:
        try:
            preco_float = float(preco.replace("R$", "").replace(".", "").replace(",", ".").strip())
            ranking.append((produto, preco_float))
        except Exception as e:
            print(f"Erro ao converter preço '{preco}':", e)

    # Ordenar por menor preço
    ranking.sort(key=lambda x: x[1])
    return ranking


def test_scraper():
# Carregar sites e buscar resultados
    sites = carregar_sites()
    palavra_chave = "lenovo core i9"

    for site in sites:
        resultados = buscar_produto(site, palavra_chave)
        ranking = extrair_ranking(resultados)

        print(f"\n📊 Ranking de preços - {site['nome']}")
        if not ranking:
            print("⚠️ Nenhum resultado encontrado.")
        else:
            for i, (produto, preco) in enumerate(ranking, start=1):
                print(f"{i}. {produto} - R$ {preco:.2f}")

test_scraper()
