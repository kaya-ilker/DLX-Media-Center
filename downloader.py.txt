import yt_dlp
import os

def download_engine(url, quality_choice, save_path):
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'noplaylist': True
    }

    if "En Yüksek" in quality_choice:
        ydl_opts['format'] = 'bestvideo+bestaudio/best'
    elif "Sadece Ses" in quality_choice:
        codec = 'mp3' if "MP3" in quality_choice else 'flac'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': codec,
            'preferredquality': '320',
        }]
    else:
        # 1080p, 720p gibi seçimler için
        height = quality_choice.split("p")[0] if "p" in quality_choice else "1080"
        ydl_opts['format'] = f'bestvideo[height<={height}]+bestaudio/best'

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])