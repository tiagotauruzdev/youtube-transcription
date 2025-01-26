import os
from pytube import YouTube
import openai
import yt_dlp
from tqdm import tqdm

def download_video(url: str, output_path: str = "downloads") -> str:
    """Baixa o vídeo do YouTube usando yt-dlp e retorna o caminho do arquivo"""
    from yt_dlp import YoutubeDL
    
    # Configurações do yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'ffmpeg_location': r'C:\ffmpeg\bin',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'retries': 3,
        'quiet': True,
        'no_warnings': True,
        'extract_flat': False,
        'force_generic_extractor': True,
        'nocheckcertificate': True,
        'source_address': '0.0.0.0',
        'socket_timeout': 30,
        'extractor_args': {
            'youtube': {
                'skip': ['dash', 'hls']
            }
        },
        'compat_opts': {
            'no-youtube-unavailable-videos': True,
            'no-youtube-channel-redirect': True
        },
        'progress_hooks': [lambda d: progress_hook(d)]
    }
    
    # Cria diretório de downloads se não existir
    os.makedirs(output_path, exist_ok=True)
    
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info_dict).replace('.webm', '.mp3')

def progress_hook(d):
    """Função de callback para mostrar progresso"""
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes')
        downloaded_bytes = d.get('downloaded_bytes')
        if total_bytes and downloaded_bytes:
            with tqdm(total=total_bytes, unit='B', unit_scale=True, desc='Baixando') as pbar:
                pbar.update(downloaded_bytes - pbar.n)

def transcribe_audio(file_path: str, api_key: str) -> tuple:
    """Transcreve o áudio usando a API Whisper da OpenAI e retorna texto e segmentos temporizados"""
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        
        file_size = os.path.getsize(file_path)
        with tqdm(total=file_size, unit='B', unit_scale=True, desc='Transcrevendo') as pbar:
            with open(file_path, "rb") as audio_file:
                transcription = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    response_format="verbose_json",
                    timestamp_granularities=["segment"]
                )
                pbar.update(file_size)
        
        # Extrai texto completo e segmentos temporizados
        full_text = transcription.text
        segments = [{
            'start': segment.start,
            'end': segment.end,
            'text': segment.text
        } for segment in transcription.segments]
        return full_text, segments
    except Exception as e:
        raise Exception(f"Erro na transcrição: {str(e)}")

def create_subtitles(segments, output_path):
    """Cria arquivo de legendas .srt a partir dos segmentos temporizados"""
    srt_content = ""
    for i, segment in enumerate(segments, start=1):
        start_time = segment['start']
        end_time = segment['end']
        text = segment['text']
        
        # Converte segundos para formato SRT (HH:MM:SS,ms)
        def format_time(seconds):
            hours = int(seconds // 3600)
            minutes = int((seconds % 3600) // 60)
            seconds = seconds % 60
            return f"{hours:02}:{minutes:02}:{seconds:06.3f}".replace('.', ',')
        
        srt_content += f"{i}\n"
        srt_content += f"{format_time(start_time)} --> {format_time(end_time)}\n"
        srt_content += f"{text}\n\n"
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(srt_content)

def main():
    # Chave da API
    api_key = "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"
    
    print("YouTube Transcription App")
    url = input("Cole a URL do vídeo do YouTube: ")
    
    try:
        print("Baixando vídeo...")
        audio_file = download_video(url)
        
        print("Transcrevendo áudio...")
        transcription, segments = transcribe_audio(audio_file, api_key)
        
        print("\nTranscrição completa:")
        print(transcription)
        
        # Salvar transcrição em arquivo
        base_name = os.path.splitext(audio_file)[0]
        txt_file = base_name + ".txt"
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(transcription)
            
        # Salvar legendas
        srt_file = base_name + ".srt"
        create_subtitles(segments, srt_file)
        
        print(f"\nTranscrição salva em: {txt_file}")
        print(f"Legendas salvas em: {srt_file}")
        
    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    main()
