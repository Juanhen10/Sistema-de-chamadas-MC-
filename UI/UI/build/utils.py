# Direcionando o caminho para imagem

from pathlib import Path

BASE_DIR = Path(__file__).parent
IMAGEM_DIR = BASE_DIR / "assets" / "frame0"



print(IMAGEM_DIR)