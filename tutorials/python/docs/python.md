# Guia Rápido sobre Python

## 🐍 O que é Python?
Python é uma linguagem de programação de **alto nível**, **interpretada** e de **tipagem dinâmica**. Criada por Guido van Rossum, ela é amplamente utilizada para desenvolvimento web, ciência de dados, automação, inteligência artificial e muito mais. Sua sintaxe simples e legível a torna uma das linguagens mais populares do mundo.

## 🔧 Como instalar Python?
Para instalar o Python no seu computador:

1. Acesse o site oficial: [python.org](https://www.python.org/)
2. Baixe a versão mais recente compatível com seu sistema operacional.
3. Execute o instalador e siga as instruções (certifique-se de marcar a opção "Add Python to PATH").
4. Após a instalação, verifique se tudo está funcionando abrindo o terminal e digitando:
```sh
   python --version
```

## 💻 Como desenvolver em Python?
Para programar em Python, você pode usar diversas IDEs (Ambientes de Desenvolvimento Integrados), incluindo:
- **PyCharm** – Completo e ideal para projetos profissionais.
- **Visual Studio Code** – Leve, rápido e com suporte a extensões.
- **Jupyter Notebook** – Perfeito para ciência de dados e aprendizado de máquina.
- **IDLE** – Simples e já vem instalado com Python.
Também é possível escrever scripts Python em qualquer editor de texto e executá-los via terminal.

## ▶️ Como executar programas Python?
Depois de criar um arquivo `.py`, você pode executá-lo pelo terminal ou prompt de comando:
- Salve o código em um arquivo, por exemplo, `script.py`.
- Abra o terminal e navegue até a pasta onde o arquivo está salvo.
- Execute o comando:
```sh
   python script.py
```

Se quiser executar um código interativo, basta digitar `python` no terminal e começar a programar diretamente.

## 🛑 Como parar a execução programas Python?
Se um script Python estiver em execução (por exemplo, um loop infinito ou uma tarefa longa), você pode interrompê-lo no terminal pressionando `Ctrl + C
`.

> Isso envia um sinal de ***KeyboardInterrupt***, que faz o Python encerrar o processo atual.

---

# 📦 Guia Completo sobre o Pip

## 🔍 O que é o Pip?
O `pip` é o sistema de gerenciamento de pacotes padrão para Python. Ele permite instalar, atualizar e remover bibliotecas e módulos de terceiros, facilitando o desenvolvimento de aplicações.

A maioria das versões modernas do Python já vem com `pip` pré-instalado, tornando a instalação de pacotes extremamente simples.

## 🚀 Como verificar se o Pip está instalado?
Para verificar se o `pip` está instalado em seu sistema, abra o terminal ou prompt de comando e digite:

```sh
pip --version
```

Se o `pip` estiver instalado corretamente, você verá uma saída semelhante a:

```
pip 23.0.1 from /usr/local/lib/python3.10/site-packages/pip (python 3.10)
```

##  🔧 Como instalar ou atualizar o Pip?

### 📥 Instalar o Pip
Se você não tem `pip`, pode instalá-lo usando o seguinte comando no terminal ou prompt de comando:
```sh
python -m ensurepip --default-pip
```

Caso esteja usando uma versão antiga do Python, pode baixá-lo manualmente do [site oficial do Pip](https://pip.pypa.io/en/stable/installation/).

### ⏫ Atualizar o Pip
Para garantir que você está usando a versão mais recente do pip, execute:
```sh
pip install --upgrade pip
```

Isso atualizará `pip` para a versão mais recente disponível.

### 📦 Como instalar pacotes com Pip?
Para instalar um pacote com `pip`, basta usar:
```sh
pip install nome-do-pacote
```

Exemplo: Instalando o `requests`, uma biblioteca popular para fazer requisições HTTP:
```sh
pip install requests
```

Se quiser instalar uma versão específica do pacote:
```sh
pip install nome-do-pacote==versão
```

Exemplo:
```sh
pip install numpy==1.22.0
```


### 📜 Como listar pacotes instalados?
Para ver todos os pacotes instalados no seu ambiente, execute:
```sh
pip list
```


### 🗑️ Como remover um pacote?
Caso queira desinstalar um pacote:
```sh
pip uninstall nome-do-pacote
```

Exemplo:
```sh
pip uninstall pandas
```

### 📂 Como usar um arquivo `requirements.txt`?
O `requirements.txt` é um arquivo onde você pode listar todas as dependências de um projeto para instalação automática.
Crie um arquivo `requirements.txt` e adicione os pacotes:
```
requests==2.27.1
numpy==1.22.0
pandas==1.3.5
```

Depois, instale todas as dependências com:
```sh
pip install -r requirements.txt
```

Isso garantirá que todas as bibliotecas necessárias sejam instaladas de uma só vez.

### 🔍 Como buscar pacotes disponíveis no PyPI?
Para procurar pacotes no Python Package Index (PyPI), visite:

🔗 https://pypi.org

---

# 🌍 Guia Completo sobre Ambientes Virtuais no Python

## 🔍 O que são Ambientes Virtuais?
Os **ambientes virtuais** no Python permitem criar espaços isolados para projetos, garantindo que cada um tenha suas próprias dependências sem afetar o sistema principal. Isso ajuda a evitar conflitos entre pacotes e versões de bibliotecas.

A ferramenta mais utilizada para gerenciar ambientes virtuais em Python é o **venv**, que já vem integrado nas versões modernas da linguagem.

---

## 🚀 Como criar um ambiente virtual?

Para criar um ambiente virtual, abra o terminal e siga os passos:

1. **Escolha uma pasta para seu projeto** e navegue até ela:
```sh
   mkdir meu_projeto
   cd meu_projeto
```

2. Crie o ambiente virtual usando `venv`:
```sh
python -m venv venv
```

Isso criará uma pasta chamada `venv` dentro do projeto, contendo a versão do Python e os arquivos necessários para o isolamento.

## ▶️ Como ativar o ambiente virtual?
Depois de criado, é preciso ativá-lo antes de instalar pacotes ou rodar o código:

#### 🪟 Windows
```sh
venv\Scripts\activate
```

#### 🐧 Linux/macOS
```sh
source venv/bin/activate
```

Se a ativação for bem-sucedida, você verá o nome do ambiente virtual antes do cursor no terminal, indicando que está ativo:

```
(venv) $
```

### 📦 Como instalar pacotes no ambiente virtual?
Após ativar o ambiente, use pip para instalar pacotes:
```sh
pip install nome-do-pacote
```

Exemplo:
```sh
pip install requests pandas
```

Os pacotes serão instalados dentro do ambiente virtual, sem afetar o sistema principal.

Se precisar salvar todas as dependências instaladas, gere um arquivo `requirements.txt`:
```sh
pip freeze > requirements.txt
```

Esse arquivo pode ser compartilhado e usado para recriar o ambiente com:
```sh
pip install -r requirements.txt
```

### 🛑 Como desativar o ambiente virtual?
Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual com:
```sh
deactivate
```

Isso retorna ao ambiente padrão do sistema.

### ❌ Como excluir um ambiente virtual?
Se quiser apagar um ambiente virtual, basta excluir sua pasta:

> Linux/macOS:

```sh
rm -rf venv
```

> Windows (no cmd):

```sh
rmdir /s /q venv  # Windows (no cmd)
```

Isso remove todas as configurações e pacotes do ambiente virtual.

### 🛠️ Alternativa: Usando `virtualenv`
Além do venv, também existe o `virtualenv`, uma ferramenta mais poderosa para gerenciar ambientes virtuais. Para instalá-lo:
```sh
pip install virtualenv
```

E para criar um ambiente com `virtualenv`:
```sh
virtualenv meu_ambiente
```
