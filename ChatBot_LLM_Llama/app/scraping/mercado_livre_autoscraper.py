from autoscraper import AutoScraper

url = "https://lista.mercadolivre.com.br/lenovo-core-i9"
exemplos = ["Notebook Lenovo LOQ-e 15iax9e Intel Core i5-12450hx 16gb 512gb Ssd Rtx 3050 Windows 11 15.6 - 83me0007br Luna Grey", "4.999"]

scraper = AutoScraper()
resultado = scraper.build(url, exemplos)
print(resultado)
scraper.save("C:/Users/mvros/Documents/ChatBot_Comparador_de_preços-20250411T135948Z-002/ChatBot_LLM_Lhama/app/scraping/mercado_livre_autoscraper")
