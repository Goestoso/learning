# 🧠 Filter Tasks Planner

Sistema automatizado para identificar novas tarefas e mudanças de bucket em tarefas existentes a partir de um arquivo JSON do Microsoft Planner. O sistema compara os dados com uma planilha Excel de referência e gera arquivos de saída com os resultados.

---

## 📂 Estrutura do App

```
filter_tasks_planner/
├── settings/
│ └── mainsettings.yml
├── data/
│ ├── tasksplanner.json # Arquivo JSON exportado do Planner
│ ├── Tasks Planner.xlsx # Planilha de referência
│ ├── tasksnew.json # Tarefas novas detectadas
│ └── changedbuckets.json # Tarefas que mudaram de bucket
├── log/
│ └── FilterTasksPlanner.log # Arquivo de log da execução
├── src/
│ ├── main.py # Função principal com agendamento
│ └── utils.py # Funções auxiliares e lógica do app
└── FilterTasksPlanner.py # Arquivo executável principal
```

---

## ⚙️ Configuração (YAML)

O arquivo de configuração `settings/mainsettings.yml` define os caminhos, opções e agendamento da execução:

```yaml
app:
  name: Filter Tasks Planner
  version: 1.0.0

observe:
  schedule: 300  # em segundos
  file: C:/caminho/para/tasksplanner.json

data:
  tasks_excel: C:/caminho/para/Tasks Planner.xlsx
  tasks_moved: C:/caminho/para/changedbuckets.json
  tasks_new: C:/caminho/para/tasksnew.json

options:
  tasks_new: true
  tasks_moved: true

log:
  active: true
  path: C:/caminho/para/diretorio/do/projeto

```

> ⚠️ O campo `log.path` pode ser tanto um diretório quanto um arquivo completo. Se for um diretório, o sistema criará automaticamente um arquivo chamado `FilterTasksPlanner.log` dentro dele.

---

## ▶️ Execução

O programa é executado em linha de comando:

```
C:\Caminho\do\programa>FilterTasksPlanner.exe
```
Após **iniciar** a execução, se as configurações estiverem corretas, a seguinte mensagem será mostrada no terminal:

```
Iniciando execução das tarefas agendadas do Filter Tasks Planner...
🔹 Pressione Ctrl + C para encerrar o programa.
```

Após **finalizar** a execução, a seguinte mensagem será mostrada no terminal:

```
🔹 Execução das tarefas agendadas do Filter Tasks Planner finalizada!

```

> Durante a execução do programa, caso o log esteja ativado, um arquivo `.log` será gerado. Podendo ser registrado as seguintes _flags_:

- `INFO`: informação relacionada a alguma ação executada pelo programa. 
- `WARNING`: avisos sobre alterações no funcionamento da aplicação e sobre qualquer movimentação das tarefas.
- `ERROR`: erros identificados durante a execução ou inicialização.

> ⚠️ Erros de inicialização sempre serão gravados num arquivo de log temporário localizado em `\temp\FilterTasksPlanner_init.log` independentemente do log estar ativado ou não.

---

## 💡 Funcionalidades

- 📥 Detecta tarefas novas que não estão na planilha de referência.

- ⚠️ Atente-se às tarefas duplicadas pois elas podem indevidamente afetar o resultado dos filtros.

- 2️⃣ Detecta tarefas duplicadas que estão na planilha de referência.

- ⚠️ Atente-se às tarefas novas pois elas indicam que a planilha de referência está defasada.

- 🔁 Detecta mudanças de bucket em tarefas já existentes.

- 🧾 Gera logs informativos e detalhados no arquivo especificado em `appsettings.json`.

- 🔁 Executa automaticamente de forma contínua usando agendamento.

- 🛑 Pode ser encerrado usando as teclas `Ctrl + C`.

---

## 🕑 Histórico de alterações do documento

- `22/07/2025`: criação do documento.
