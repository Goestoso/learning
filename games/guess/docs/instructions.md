# 🎮 Guess - Jogo de Adivinhação de Palavras

**Guess** é um jogo simples de adivinhação de palavras, inspirado na tradicional forca, desenvolvido em Python.

---

## 🚀 Como Jogar

### 🧾 Regras do Jogo:

- O jogo escolhe uma palavra secreta aleatória.
- Você deve tentar adivinhar a palavra:
  - Letra por letra **ou**
  - A palavra inteira de uma vez.

### 🎯 Objetivo:
Adivinhar corretamente a palavra antes de acabar suas tentativas.

---

## 🕹️ Jogabilidade

Ao rodar o jogo, você verá um menu com 3 opções:

1. **▶ Start** - Inicia uma nova partida.
2. **❓ Help** - Exibe as instruções detalhadas.
3. **↩ Exit** - Sai do jogo.

---

## 📜 Instruções (exibidas ao escolher a opção 3)

- A palavra secreta será exibida como: `_ _ _ _`
- Você pode tentar:
  - Uma **letra** por vez
  - A **palavra inteira** diretamente
- Se acertar uma letra, ela será revelada nas posições corretas.
- Se errar, perderá uma tentativa.
- Você tem **6 tentativas** no total.

---

## 🔄 Opções pós-jogo

Após o fim da partida será mostrada a pergunta "Would you like to try again?", da qual você poderá escolher:

- **Yes**: Jogar novamente com uma nova palavra.
- **No**: Voltar ao menu principal.

---

## ✅ Condições de Vitória:

- Acertar todas as letras da palavra.
- Adivinhar corretamente a palavra inteira.

## ❌ Condições de Derrota:

- Utilizar todas as 6 tentativas sem descobrir a palavra.

---

## 🧠 Dicas

- Evite repetir letras já testadas.
- Palavras inteiras também podem ser chutadas, mas errar consome tentativa.
- Não são aceitos números ou caracteres especiais.

---

## 📁 Estrutura atual do projeto

```
/artificial-guess
|
├── assets 
|    └── lamp.ico   # icon do jogo
├── data 
|    └── words.txt   # palavras que deverão ser advinhadas
├── docs
|     └── instructions.txt  
└── guess  # executável do jogo

```

> O arquivo `words.txt` deve conter uma lista de palavras, uma por linha, que serão usadas como palavras secretas.

## 🐍 Como executar

Basta clicar no programa `guess.exe` ou  executar via terminal o seguinte comando:

```
guess.exe
```

> Certifique-se de que os arquivos `words.txt` e `lamp.ico` estão no caminho correto (`/data/words.txt` e `/assets/lamp.ico`).
