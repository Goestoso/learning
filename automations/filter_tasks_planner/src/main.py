"""Módulo das funções principais do app Filter Tasks Planner"""
from src import utils
import schedule, time

def job():
    if utils.log_active:
        utils.logger.info("Iniciando execução do filtro das tarefas do planner...")
    if utils.option_new or utils.option_moved:
        utils.load_tasksplanner_json()
        if utils.option_new:
            utils.create_tasksnew_json()
        if utils.option_moved:
            utils.create_changedbucketes_json()
    if utils.log_active:
        utils.logger.info("Finalizando execução do filtro das tarefas do planner...")

def run_scheduler(config_path):
    utils.initialize(config_path)
    if utils.log_active:
        utils.logger.info(f"Tarefas agendadas para rodarem a cada {utils.observe_schedule} segundos.")
    print("Iniciando execução das tarefas agendadas do Filter Tasks Planner...\n🔹 Pressione Ctrl + C para encerrar o programa.")

    schedule.every(utils.observe_schedule).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
