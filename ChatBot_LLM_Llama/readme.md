#  ChatBot WhatsApp com FastAPI, Twilio, LLaMA e Scraping

Este projeto é um chatbot experimental que permite ao usuário interagir via WhatsApp para buscar o melhor preço de produtos em e-commerces pré estabelecidos. Ele utiliza LLM local (LLaMA), scraping com Selenium + AutoScraper e integra com a API do Twilio para por fim ser interagível pelo watsapp.

---

##  Visão Geral

- O usuário envia uma mensagem pelo WhatsApp
- O chatbot extrai palavras-chave e caracteristicas do item na mensagem com um modelo LLaMA rodando localmente
- Com essas palavras-chave, ele busca preços em sites de e-commerce
- Retorna as ofertas encontradas diretamente pelo WhatsApp

---

## Bibliotecas Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) 
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) 
- [Selenium](https://www.selenium.dev/) 
- [AutoScraper](https://github.com/alirezamika/autoscraper) 
- [Twilio](https://www.twilio.com/) 
- [Ngrok](https://ngrok.com/)

---

## Como Rodar Localmente

### 1. Clonar o repositório
```bash
git clone https://github.com/marcosrosset41/Python/ChatBot_LLM_Llama.git
cd ChatBot_LLM_Llama
```

### 2. Criar ambiente virtual e instalar dependências
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente
Crie um arquivo `.env` na pasta `app/` com:
```env
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=seu_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
LOCAL_NGROK_URL=https://abcd1234.ngrok.io
```

### 4. Executar o projeto
```bash
# Terminal 1
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload

# Terminal 2 (Ngrok)
ngrok http 8000
```

### 5. Configurar Webhook no Twilio
Acesse https://console.twilio.com/
E configure o webhook do Sandbox para:
```
https://abcd1234.ngrok.io/twilio-webhook
```
sendo que esse link para o webhook é disponibilizado pelo ngrok ao exectutar
```
# Terminal 2 (Ngrok)
ngrok http 8000
```
---

## Estrutura do Projeto

```
chatbot-whatsapp/
├── app/
│   ├── main.py                  # API principal
│   ├── llm_llama.py             # LLM local com LLaMA
│   ├── twilio_webhook.py        # Integração com WhatsApp
│   ├── ecommerce_config.json    # URLs dos sites e XPaths das caixas de busca
│   ├── scraping/                # Lógica de scraping nos e-commerces
│   │   ├── kabum_autoscraper.py
│   │   ├── mercado_livre_autoscraper.py
│   │   └── scraper.py           # Utilitários de scraping
│   └── model/                   # Modelo local do LLaMA
│       └── llama-2-7b-chat.Q5_K_M.gguf
├── requirements.txt             # Dependências do projeto
├── .env                         # Variáveis de ambiente (chaves, tokens etc.)
├── start.bat                    # Script de inicialização (opcional)
└── docs/
    ├── diagram.png              # Diagrama do fluxo
    └── readme.md                # Documentação do projeto

```

---

## Possíveis adaptações
- Persistência em banco de dados
- Deploy completo via container, dispensando a maquina local como servidor
- Integração com mais marketplaces
- UI de gerenciamento

---

##  Autor
Marcos Vinicius Rosset - Estudante de Dados e IA

---

## Licença
Este projeto é de código aberto. Sinta-se à vontade para usar, modificar e distribuir.

