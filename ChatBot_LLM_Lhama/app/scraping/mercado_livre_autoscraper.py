from autoscraper import AutoScraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url = "https://lista.mercadolivre.com.br/lenovo-core-i9"
exemplos = [
    "Notebook Lenovo LOQ-e 15iax9e Intel Core i5-12450hx 16gb 512gb Ssd Rtx 3050 Windows 11 15.6 - 83me0007br Luna Grey",
    "4.999",
    "Notebook Lenovo Ideapad 1i Intel Core I3 - 1215U, 4GB RAM, 256GB SSD,...",
    "2.499"
    "Pc Completo Fácil Intel Core I9 10900f 16gb Ssd 960gb 19''",
    "4.199",
    "Cpu Lenovo M93p Intel Core I5 8gb Ssd 240gb Wifi Office",
    "818",
    "Workstation Lenovo P360 Core I9 12900k, 64 Gb Ram",
    "9.900"
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
scraper.save("C:/Users/mvros/Documents/ChatBot_Comparador_de_preços-20250411T135948Z-002/ChatBot_LLM_Llama/app/scraping/mercado_livre_autoscraper.json")
