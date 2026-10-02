import argparse
from descargador.core import obtener_metadatos

def main():

    parser = argparse.ArgumentParser(description="Descarga audio de Youtube")
    parser.add_argument("url", help = "URL del video")
    args= parser.parse_args()

    metadatos=obtener_metadatos(args.url)
    print(type(metadatos))
    print(metadatos)

if __name__ == "__main__":
    main()
