# YouTube Transcription App

Aplicativo Python para transcrever vídeos do YouTube utilizando a API da OpenAI.

## Requisitos

- Python 3.8+
- Chave da API da OpenAI

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/MacOS: `source venv/bin/activate`
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da OpenAI:
   ```
   OPENAI_API_KEY=sua_chave_aqui
   ```

## Uso

Execute o aplicativo:
```bash
python main.py
```

Cole a URL do vídeo do YouTube quando solicitado. A transcrição será salva no arquivo `transcription.txt`.

## Licença

MIT
