# Documentação do Projeto YouTube Transcription

## Descrição
Este projeto permite baixar vídeos do YouTube e transcrever seu áudio utilizando a API Whisper da OpenAI. O código foi desenvolvido em Python e utiliza as bibliotecas pytube, yt-dlp e openai.

## Dependências e Instalação

### Requisitos
- Python 3.10 ou superior
- FFmpeg instalado e configurado no PATH
- Chave de API da OpenAI

### Instalação
1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/youtube-transcription.git
cd youtube-transcription
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure o FFmpeg:
- Baixe o FFmpeg: https://ffmpeg.org/download.html
- Adicione ao PATH do sistema

## Estrutura do Código

### Arquivos Principais
- `transcriber.py`: Script principal que contém toda a lógica de download e transcrição
- `requirements.txt`: Lista de dependências do projeto

### Funções Principais
1. `download_video(url: str, output_path: str) -> str`
   - Baixa o vídeo do YouTube e converte para MP3
   - Parâmetros:
     - `url`: URL do vídeo do YouTube
     - `output_path`: Diretório de saída (padrão: 'downloads')
   - Retorna: Caminho do arquivo MP3 gerado

2. `transcribe_audio(file_path: str, api_key: str) -> str`
   - Transcreve o áudio usando a API Whisper da OpenAI
   - Parâmetros:
     - `file_path`: Caminho do arquivo de áudio
     - `api_key`: Chave da API OpenAI
   - Retorna: Texto transcrito

3. `main()`
   - Função principal que orquestra o fluxo do programa

## Erros Encontrados e Soluções

### 1. Erro: Client.__init__() got an unexpected keyword argument 'proxies'
- **Causa**: Atualização da biblioteca openai (versão 1.0.0+)
- **Solução**: 
  - Atualizar a biblioteca openai:
    ```bash
    pip install --upgrade openai
  ```
  - Ajustar a inicialização do cliente OpenAI:
    ```python
    client = OpenAI(api_key=api_key)
    ```

### 2. Erro: Formato de áudio incompatível
- **Causa**: Problemas na conversão do vídeo para áudio
- **Solução**: 
  - Verificar instalação do FFmpeg
  - Atualizar yt-dlp:
    ```bash
    pip install --upgrade yt-dlp
    ```

## Melhorias Futuras

1. Implementar interface gráfica
2. Adicionar suporte a múltiplos formatos de saída (SRT, VTT)
3. Implementar sistema de filas para processamento em lote
4. Adicionar suporte a outras APIs de transcrição
5. Implementar cache de transcrições

## Guia de Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas mudanças:
   ```bash
   git commit -m 'Adicionando nova funcionalidade'
   ```
4. Push para a branch:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request

## Licença
MIT License

## Contato
Para suporte ou dúvidas, entre em contato:
- Email: suporte@youtube-transcription.com
- Issues: https://github.com/seu-usuario/youtube-transcription/issues
