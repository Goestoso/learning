"""Módulo executável do app Filter Tasks Planner"""
from src import main
from src import utils
from pathlib import Path
import sys

if getattr(sys, 'frozen', False):
    base_path = Path(sys.executable).parent
else:
    base_path = Path(__file__).resolve().parent

config_path = base_path / 'settings' / 'mainsettings.yml'

if __name__ == "__main__":
    try:
        main.run_scheduler(config_path)
    except KeyboardInterrupt:
        if utils.log_active:
            utils.cleanup_json_data()
            utils.logger.warning("Programa encerrado pelo usuário com Ctrl+C.")
        print("🔹 Execução das tarefas agendadas do Filter Tasks Planner finalizada!\n")