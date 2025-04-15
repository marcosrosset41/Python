from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from app.llm_llama import extrair_palavras_chave
from app.scraping.scraper import buscar_melhor_preco



app = FastAPI()

@app.get("/")
def root():
    return {"status": "online"}

@app.post("/twilio-webhook")
async def receber_mensagem(Body: str = Form(...)):
    print("Requisição recebida!")
    print("Mensagem:", Body)

    if not Body:
        return {"erro": "Mensagem vazia"}

    try:
        palavras_chave = extrair_palavras_chave(texto=Body)
        resultado = buscar_melhor_preco(palavras_chave)
        return {"resposta": resultado}
    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": str(e)})

# Código para rodar o servidor diretamente com `python -m app.main`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
