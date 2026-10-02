import yt_dlp


def obtener_metadatos(url: str) -> dict:
    ydl_opts = {
            'js_runtimes': {'node':{}}  # Le dice a yt-dlp que use Node.js
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return ydl.sanitize_info(info)

def obtener_audio(url: str, carpetaDestino: str) -> str:
    ruta = {}
    def mi_hook(d):
        if d['status'] == 'finished':
            ruta['path'] = d.get('info_dict', {}).get('_filename') or d.get('filename')
        
    ydl_opts = {
        'js_runtimes': {'node':{}},  # Le dice a yt-dlp que use Node.js
        'progress_hooks':  ['mi_hook'],
        'outtmpl': '/home/ronald/Projects/python/appmusic/downloads/%(title)s.%(ext)s',
        'format': 'm4a/bestaudio/best',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
    return ruta.get('path') 


