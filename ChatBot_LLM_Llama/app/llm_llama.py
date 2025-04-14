from llama_cpp import Llama

llm = Llama(model_path=r"C:\Users\mvros\Documents\ChatBot_Comparador_de_preços-20250411T135948Z-002\ChatBot_Comparador_de_preços\app\model\llama-2-7b.Q3_K_M.gguf")

texto = "notebook lenovo core i9"

def extrair_palavras_chave(texto):
    prompt = f"Extraia as palavras-chave para buscar um produto no e-commerce: {texto}\nPalavras-chave:"
    output = llm(prompt, max_tokens=20, stop=["\n"])

    print("Saída do modelo:", output)

    # Acessa o texto de forma segura:
    if isinstance(output, dict):
        if "choices" in output:
            return output["choices"][0]["text"].strip()
        elif "content" in output:
            return output["content"].strip()
    
    raise ValueError("Formato de resposta inesperado do modelo.")

resultado = extrair_palavras_chave(texto)
print("Palavras-chave extraídas:", resultado)
