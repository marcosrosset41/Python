from autoscraper import AutoScraper

url = "https://www.kabum.com.br/busca/lenovo-core-i9"
exemplos = ['Notebook Lenovo Legion 5 16irx9 Intel Core i9-14900hx 32gb 1TB SSD RTX 4070 WINDOWS 11 16" - 83ew0004br...', "R$ 14.079,12"]

scraper = AutoScraper()
scraper.build(url, exemplos)
scraper.save("app/scraping/kabum_autoscraper")
