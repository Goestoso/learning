# 📘 Guia Rápido sobre Jupyter Notebooks

## 🧠 O que é o Jupyter Notebook?

O **Jupyter Notebook** é um ambiente interativo usado principalmente para **ciência de dados**, **análise exploratória**, **machine learning** e **visualização de dados**. Ele permite escrever e executar código em blocos (células), mesclando **código Python**, **texto explicativo em Markdown**, **gráficos** e **tabelas** no mesmo documento.

🔍 *Jupyter* vem de **Ju**lia, **Pyt**hon e **R**, as três linguagens suportadas inicialmente.

---

## 🎯 Para que serve o Jupyter Notebook?

- Ensino e aprendizado de programação
- Documentação de experimentos com código e resultados
- Testes interativos com dados
- Relatórios técnicos e científicos
- Prototipação rápida de ideias

---

## 🚀 Como instalar o Jupyter Notebook?

### ✅ Requisitos:
Você precisa ter o **Python** e o **pip** instalados. Veja como instalar no [guia de Python](https://pypi.org/project/notebook/).

### 📦 Instalar com pip:
```sh
pip install notebook
```

### 💡 Alternativas:
Você também pode instalar o Jupyter como parte do pacote **Anaconda** (recomendado para ciência de **dados**):
🔗 anaconda.com

## ▶️ Como iniciar um Jupyter Notebook?
Depois de instalado, abra o terminal e execute:

```sh
jupyter notebook
```
O navegador será aberto automaticamente com a interface web do Jupyter.

## ✍️ Como criar um novo notebook?
Na interface web do Jupyter:

1. Clique em New > Python 3 (ipykernel)

2. Um novo notebook será criado com células de código.

3. Escreva seu código e pressione `Shift + Enter` para executar.

## 📝 Como usar Jupyter no VSCode?

### 1. **Instale a extensão Jupyter**

-  Abra o VSCode.

- Vá até a aba de extensões (ícone de quadrado ou `Ctrl+Shift+X`).

- Busque por **Jupyter** (extensão oficial da Microsoft).

- Clique em **Instalar**.

> A extensão Python será instalada automaticamente se ainda não estiver.

### 2. Abra ou crie um notebook
Você pode:

- Criar um novo notebook: `File > New File` → escolha `Jupyter Notebook (.ipynb)`.

- Ou abrir um arquivo `.ipynb` existente.

### 3. Executar células
- Clique no botão ▶️ ao lado de cada célula.

- Ou use ``Shift + Enter` para executar.

### 4. Ambiente de execução (kernel)
- A primeira vez que abrir um notebook, o VSCode perguntará qual **kernel (ambiente Python)** usar.

- Se você estiver usando um **ambiente virtual**, certifique-se de ativá-lo no terminal antes ou selecione manualmente.

## 🧩 Estrutura de um Notebook
- **Células de Código**: Onde você escreve código Python.

- **Células Markdown**: Para adicionar explicações, títulos e formatação.

- **Saídas**: Mostram o resultado do código abaixo da célula.

Exemplo de Markdown:

```
# Título
## Subtítulo
**Texto em negrito**
*Texto em itálico*
```

## 🖼️ Exemplo de notebook

```
# Célula de código
import pandas as pd

df = pd.read_csv("dados.csv")
df.head()
```
```
### Análise inicial dos dados
A função `head()` mostra as primeiras linhas do DataFrame.
```

## 📁 Como salvar e compartilhar notebooks?
Arquivos Jupyter têm a extensão `.ipynb`

- Você pode:

- Salvar clicando em **File** > **Save** and **Checkpoint**

- Exportar como *PDF*, *HTML* ou *Markdown* em **File** > **Download as**

- Subir para repositórios como o **GitHub** para compartilhar

## 💡 Dicas úteis
Atalhos:

- `Shift + Enter` → Executa célula

- `Esc + B` → Nova célula abaixo

- `Esc + M` → Transforma célula em Markdown

- `Esc + D + D` → Deleta célula

- Comandos mágicos:

```
%time                 # Tempo de execução de uma linha
%matplotlib inline    # Exibe gráficos no próprio notebook
```

## 🌐 Alternativas e interfaces modernas 

- [JupyterLab](https://jupyterlab.readthedocs.io/en/latest/) – interface mais moderna e poderosa

- [Google Colab](https://colab.research.google.com) – versão online gratuita com GPU

## 🛑 Como encerrar o Jupyter?
No terminal onde o notebook foi iniciado, pressione `Ctrl + C` e confirme com `y` para interromper o servidor.