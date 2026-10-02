import argparse
from descargador.core import obtener_metadatos
from descargador.core import obtener_audio

def main():

    parser = argparse.ArgumentParser(description="Descarga audio de Youtube")
    parser.add_argument("url", help = "URL del video")
    parser.add_argument("carpetaDestino", help = "Direccion de la carpeta donde se va a descargar")
    args= parser.parse_args()

    metadatos=obtener_metadatos(args.url)
    for clave in ('title', 'upload_date', 'tags'):
        print(f"{clave}: {metadatos.get(clave)}")

    audio=obtener_audio(args.url, args.carpetaDestino) 
    print(audio)

if __name__ == "__main__":
    main()
