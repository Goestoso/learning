from src import main
from pathlib import Path

config_path = Path(__file__).resolve().parent / 'settings' / 'mainsettings.yml'

if __name__ == "__main__":
    main(config_path)