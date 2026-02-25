import shutil
from pathlib import Path
import json
import time
from logger import setup_logger

logger = setup_logger()

def sort_file(base_folder, file_path):
    with open("config.json") as f:
        config = json.load(f)

    archivo = file_path.suffix
    
    if archivo in config["Extensiones"]:
        carpeta = config["Extensiones"][archivo]

        destino = Path(base_folder) / carpeta
        destino.mkdir(exist_ok=True)

        try:
            destino_archivo = destino / file_path.name

            if destino_archivo.exists():
                contador = 1
                while destino_archivo.exists():
                    nuevo_nombre = f"{file_path.stem} ({contador}){file_path.suffix}"
                    destino_archivo = destino / nuevo_nombre
                    contador += 1
            time.sleep(1)
            shutil.move(file_path, destino_archivo)
            logger.info(f"{file_path.name} movido a {carpeta}")

        except Exception as e:
            logger.error(f"Error al mover {file_path.name}: {e}")
    else:
        logger.error("Extensión no soportada")


