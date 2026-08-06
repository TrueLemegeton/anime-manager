import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / 'anime.json'

if not DATA_FILE.exists():
    DATA_FILE.write_text('[]', encoding='utf-8')  # Create an empty JSON array if the file doesn't exist


def load_anime() -> list[dict]:
    """Load the list of anime from a JSON file."""
    with open(DATA_FILE, mode='r', encoding='utf-8') as file:
        anime_list = json.load(file)
    return anime_list


def save_anime(anime_list: list[dict]) -> None:
    """Save the list of anime to a JSON file."""
    with open(DATA_FILE, mode='w', encoding='utf-8') as file:
        json.dump(anime_list, file, ensure_ascii=False, indent=2)