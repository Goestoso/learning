# 🧾 Filter Tasks Planner Solution (Power Automate)

**Nome da Solução**: `Filter Tasks Planner` 

**Versão**: `1.6.2`  

**Última atualização**: `25/07/2025`  

---

## 📌 Resumo da Solução

A solução **Filter Tasks Planner** foi desenvolvida para facilitar o acompanhamento de tarefas no Microsoft Planner, exportando e processando automaticamente informações com base em buckets, status e alterações. Essa solução é composta por automações no Power Automate.

> Este guia tem como objetivo orientar os usuários na **importação**, **configuração** e **execução** correta da solução.

---

## 📥 Como Importar uma Solução no Power Automate

1. Acesse o Power Automate: https://make.powerautomate.com
2. No menu lateral, clique em "**Soluções**".
3. Clique em "**Importar solução**".
4. Faça upload do arquivo `.zip` da solução.
5. Siga as instruções da interface para mapear as conexões utilizadas (Planner, File System, etc).
6. Clique em **Importar** e aguarde a finalização.

---

## ⚙️ Configurar o Ambiente

Para que as automações funcionem corretamente, siga os passos abaixo:

- Crie as conexões necessárias no Power Automate (Planner, File System, Gateway).

- Instale e configure o **On-premises data gateway** (veja próximo tópico).

- Verifique os caminhos e credenciais do File System.

- Mantenha o Power Automate com permissões adequadas para acessar os recursos locais.

- Configure `FilterTasksPlanner.exe` com base no repositório/documentação técnica.

---

## 🔌 On-premises Data Gateway

O **Data Gateway** é necessário para permitir que o Power Automate acesse arquivos locais (como o JSON exportado pelo Power Automate Desktop).

**Passos para configurar**:

1. Baixe o instalador: https://aka.ms/gatewayinstall
2. Execute o instalador e conecte à sua conta Microsoft 365.
3. Escolha "Modo padrão" e defina um nome de gateway.
4. Após instalado, vá ao Power Automate > **Gateways** > Adicione seu gateway ao ambiente.
5. Use esse gateway ao configurar a conexão File System.

---

## 📂 Conexão File System do Power Automate
A conexão File System permite que os fluxos interajam com arquivos locais ou em rede.

**Como configurar**:

1. Vá em "**Dados**" > "**Conexões**" > **Nova conexão**.
2. Busque por "File System" e selecione.
3. Insira as credenciais do Windows com acesso à pasta monitorada.
4. Escolha o gateway configurado anteriormente.
5. Teste a conexão e certifique-se que o fluxo consegue ler/escrever arquivos.

---

## 🔄 Automações Incluídas na Solução

> Para mais detalhes, acesse a discussão sobre o desenvolvimento dessa solução: [Filter Tasks Planner - Criar solução com as automações do Power Automate](https://github.com/Goestoso/learning/issues/27)

### 🆕 Update Created Tasks Planner Data

- **Objetivo**: atualizar a descrição da tarefa que acabou de ser criada no Planner com o bucket atual dela e adicionar a nova linha com as informações dessa tarefa na base `.xlsx` armazenada no `OneDrive`.
- **Frequência**: A cada 10 minutos (ou conforme agendado).
- **Saída**: não se aplica.
- **Observação**: É necessário que o arquivo do Excel localizado no **OneDrive** esteja com a tabela do plano extraído do Planner. Não se esqueça de adicionar a coluna `ID do Bucket`, pois ela será crucial para a monitoração das tarefas que mudaram de bucket.

### ☑️ Update Completed Tasks Planner Data

- **Objetivo**: atualizar a descrição da tarefa que acabou de ser concluída no Planner com o bucket atual dela e atualizar a linha com as informações dessa tarefa na base `.xlsx` armazenada no `OneDrive`.
- **Frequência**: A cada 10 minutos (ou conforme agendado).
- **Saída**: não se aplica.
- **Observação**: É necessário que o arquivo do Excel localizado no **OneDrive** esteja com a tabela do plano extraído do Planner. Não se esqueça de adicionar a coluna `ID do Bucket`, pois ela será crucial para a monitoração das tarefas que mudaram de bucket.

### ☁️ Update Local Tasks Planner Data when it is modified in OneDrive

- **Objetivo**: atualizar o arquivo local `Tasks Planner.xlsx` com as informações da base `.xlsx` armazenada no `OneDrive`.
- **Frequência**: A cada 10 minutos (ou conforme agendado).
- **Saída**: carrega o conteúdo do arquivo aramzenado no OneDrive no excel `Tasks Planner.xlsx` localizado na máquina com o Gateway.
- **Observação**: É necessário que o diretório do arquivo `Tasks Planner.xlsx` esteja acessível via File System.

### 📝 List all tasks planner and create json file

- **Objetivo**: Exportar tarefas do Planner a cada X minutos e salvá-las em formato JSON.
- **Frequência**: A cada 10 minutos (ou conforme agendado).
- **Saída**: Arquivo `tasksplanner.json` localizado na máquina com o Gateway.
- **Observação**: É necessário que o diretório do arquivo `tasksplanner.json` esteja acessível via File System.

### ↔️ Get tasks with changed buckets

- **Objetivo**: Lê o conteúdo do arquivo `changedbuckets.json` gerado pelo programa `FilterTasksPlanner.exe` quando for identificado que tarefas mudaram de bucket no Planner. Caso alguma tarefa tenha mudado de bucket, a descrição da tarefa é atualizada com o bucket atual dela.
- **Frequência**: A cada 10 minutos (ou conforme agendado).
- **Saída**: não se aplica.
- **Observação**: É necessário que o diretório do arquivo `changedbuckets.json` esteja acessível via File System.

### 🆔 Update Tasks's Bucket ID

- **Objetivo**: atualizar a coluna `ID do Bucket` da base excel no OneDrive com os valores dos ids dos buckets do Planner. 
- **Frequência**: A cada 10 minutos (ou conforme agendado).
- **Saída**: não se aplica.
- **Observação**: Essa automação deve ser executada após exportar o plano do Planner, armazenar no OneDrive e criar a coluna `ID do Bucket`.

## ✅ Checklist Final

[] Solução importada com sucesso no Power Automate

[] Conexões (Planner e File System) configuradas

[] Gateway instalado e funcional

[] `FilterTasksPlanner.exe` em execução

[] Teste completo realizado

## 🕑 Histórico de alterações do documento

- `25/07/2025`: criação do documento.
