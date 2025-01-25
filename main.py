import os
from pytube import YouTube
from openai import OpenAI
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

def download_audio(url):
    """Baixa o áudio de um vídeo do YouTube"""
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    return audio.download()

def transcribe_audio(file_path):
    """Transcreve o áudio usando a API da OpenAI"""
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    with open(file_path, 'rb') as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcription.text

def main():
    print("YouTube Transcription App")
    url = input("Cole a URL do vídeo do YouTube: ")
    
    try:
        print("Baixando áudio...")
        audio_path = download_audio(url)
        
        print("Transcrevendo áudio...")
        transcription = transcribe_audio(audio_path)
        
        print("\nTranscrição completa:")
        print(transcription)
        
        # Salvar transcrição em arquivo
        output_file = "transcription.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(transcription)
        print(f"\nTranscrição salva em {output_file}")
        
    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    main()
