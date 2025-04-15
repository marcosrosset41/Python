from autoscraper import AutoScraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url = "https://www.kabum.com.br/busca/lenovo-core-i7"
exemplos = [
            'Mini PC Lenovo intel Core i7-7700 7º Geração, 16GB RAM DDR4, SSD 256GB M.2 Nvme, Windows 10 Pro', 
            "R$ 1.890,53",
            'Notebook Lenovo IdeaPad 1i Intel Core i7-1255U, 12GB RAM, SSD 512GB, Intel Iris Xe, 15.6", Windows 11, Cinza -...', 
            "R$ 3.499,00",
            "Mini PC Lenovo Intel Core I7-7700 7ª Geração, 16GB RAM DDR4, SSD 512GB M2, Wifi, Windows 10",
            "R$ 1.986,24",
            'Notebook Lenovo Ideapad 1i, Intel Core i7-1255u, 12GB, SSD 512GB, Tela 15.6", Linux, Cloud Grey - 82vys01000',
            "R$ 3.519,12",
            'Notebook Lenovo V14 G4 Iru Intel Core I7-1355u 16gb 512gb SSD WINDOWS 11 Pro 14" - 83gk0009br Preto',
            "R$ 4.751,12"
            ]

# Iniciar navegador com Selenium
options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(10)  # Aguardar carregar completamente

# Capturar HTML da página renderizada
html = driver.page_source
driver.quit()

# Treinar o modelo com HTML renderizado
scraper = AutoScraper()
resultado = scraper.build(html=html, wanted_list=exemplos)

print("\n✅ Resultado de exemplo extraído:", resultado)

# Salvar modelo treinado
scraper.save("C:/Users/mvros/Documents/ChatBot_Comparador_de_preços-20250411T135948Z-002/ChatBot_LLM_Llama/app/scraping/kabum_autoscraper.json")