import json
import time
from autoscraper import AutoScraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def carregar_sites(path_json=r"C:\Users\mvros\Documents\ChatBot_Comparador_de_preços-20250411T135948Z-002\ChatBot_LLM_Llama\app\ecommerce_config.json"):
    with open(path_json, "r", encoding="utf-8") as f:
        return json.load(f)


def buscar_produto(site, palavra_chave):
    print(f"\n🔍 Buscando por: {palavra_chave} em {site['nome']}")

    # Configurações aprimoradas do navegador para evitar erro 403
    options = Options()
    # options.add_argument("--headless")  # Roda sem abrir o navegador
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("window-size=1920,1080")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    )

    navegador = webdriver.Chrome(options=options)

    # Abrir o site
    navegador.get(site["url_base"])

    # Buscar pela palavra-chave
    barra_busca = navegador.find_element(By.XPATH, site["xpath_busca"])
    barra_busca.send_keys(palavra_chave)
    barra_busca.send_keys(Keys.RETURN)

    # Esperar carregar os resultados
    WebDriverWait(navegador, 15).until(
    EC.presence_of_element_located((By.XPATH, "//body"))
)

    # Carregar o modelo do AutoScraper
    scraper = AutoScraper()
    scraper.load(site["modelo_scraper"])

    # Verificando o HTML retornado (útil pra debug, pode comentar se quiser)
    print("\n📄 Trecho do HTML:")
    print(navegador.page_source[:1000])

    # Buscar dados semelhantes àqueles treinados
    resultados = scraper.get_result_similar(html=navegador.page_source, grouped=True)
    navegador.quit()

    print("⚙️ Resultados brutos encontrados pelo modelo:", resultados)
    return resultados


def extrair_ranking(resultados, site):
    produtos = resultados.get(site["stack_id_produto"], [])
    precos = resultados.get(site["stack_id_preco"], [])

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
    palavra_chave = "lenovo core i7"

    for site in sites:
        resultados = buscar_produto(site, palavra_chave)
        ranking = extrair_ranking(resultados, site)

        print(f"\n📊 Ranking de preços - {site['nome']}")
        if not ranking:
            print("⚠️ Nenhum resultado encontrado.")
        else:
            for i, (produto, preco) in enumerate(ranking, start=1):
                print(f"{i}. {produto} - R$ {preco:.2f}")


# Descomente para testes locais
test_scraper()
