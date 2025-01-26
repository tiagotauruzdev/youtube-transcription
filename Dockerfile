# Imagem base com Python 3.10 e FFmpeg
FROM python:3.10-slim

# Instala o FFmpeg
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão do container (pode ser ajustado para o projeto)
CMD ["python", "transcriber.py"]
