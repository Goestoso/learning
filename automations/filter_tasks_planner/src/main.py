"""Módulo das funções principais do app Filter Tasks Planner"""
from src import utils
import schedule, time, sys

def job():
    if utils.log_active:
        utils.logger.info("Iniciando execução do filtro das tarefas do planner...")
    utils.load_tasksplanner_json()
    if utils.option_new:
        utils.create_tasksnew_json()
    if utils.option_moved:
        utils.create_changedbucketes_json()
    if utils.log_active:
        utils.logger.info("Finalizando execução do filtro das tarefas do planner...")
        

def run_scheduler(config_path):
    utils.initialize(config_path)
    print("Iniciando execução das tarefas agendadas do Filter Tasks Planner...\n🔹 Pressione Ctrl + C para encerrar o programa.")
    if utils.log_active:
        utils.logger.info(f"Tarefas agendadas para rodarem a cada {utils.observe_schedule} segundos.")
    if not utils.option_new and not utils.option_moved:
        if utils.log_active:
            utils.logger.warning("Programa encerrado pois as opções 'tasks_new' e 'tasks_changed' estão desativadas.")
            print("⚠️ Execução das tarefas agendadas do Filter Tasks Planner finalizada pois nenhuma opção de filtro está ativada!\n")
            sys.exit(0)

    schedule.every(utils.observe_schedule).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
