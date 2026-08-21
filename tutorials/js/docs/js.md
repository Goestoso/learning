# Guia Rápido sobre JavaScript

## 👨‍💻 O que é JavaScript (JS)?
JavaScript é uma linguagem de programação de **alto nível** usada para criar **interatividade**, **animações** e **comportamento dinâmico** em **páginas da web**.

## 🧱 O que é TypeScript (TS)?
TypeScript é uma linguagem de programação de **código aberto** criada pela Microsoft. 

Ela funciona como um **superconjunto do JavaScript**, adicionando **tipagem estática opcional**, **interfaces**, **tipos personalizados**, **generics**, **detecção antecipada de erros** e melhor integração com editores de código.

No final, **o código é convertido em JavaScript puro** para rodar nos navegadores ou no **Node.js**.

## 🌐 O que é Node.js?
É um **ambiente de execução** que roda código JavaScript fora do navegador. Ele usa o motor V8 do Google para transformar o JavaScript em uma ferramenta potente para criar servidores, sites e programas de computador.

## 🔧 Como instalar Node.js?
Para instalar o `Node.js` no seu computador:

1. Acesse o site oficial: [nodejs.org](https://nodejs.org/en/download)
2. Baixe a versão mais recente compátível (recomenda-se a versão **LTS - Long Term Support**) com seu sistema operacional.
3. Execute o instalador e siga a instruções.
4. Após a instalação, verifique se tudo está funcionando abrindo o terminal e digitando:
```sh
   node --version
```
## 💻 Como desenvolver em JS?
Para programar em JS, você pode usar diversas IDEs (Ambientes de Desenvolvimento Integrados), incluindo:
- **Visual Studio Code** – Leve, rápido e com suporte a extensões.
- **WebStorm** – Robusto e com ferramentas avançadas nativas, tendo foco total em JavaScript e TypeScript, **porém é pago**.
- **Sublime Text** - Ultrarápido, interface limpa e ideal para computadores mais fracos.

## ▶️ Como executar programas JavaScript?
Depois de instalar o **Node.js**, crie um arquivo `app.js` (ou `app.ts` se quiser usar **TS**):
```
console.log("Hello World");
```

Abra o terminal no diretório do arquivo e execute:

```
node app.js
```

A saída será: 

```
Hello World
```

## 🛑 Como parar a execução do código JS?
Se um código JS estiver em execução (por exemplo, um loop infinito ou uma tarefa longa), você pode interrompê-lo no terminal pressionando `Ctrl + C`.

---

# 📦 Guia Completo sobre o npm

## 🔍 O que é o npm?
O `npm` (**Node Package Manager**) é o gerenciador de pacotes padrão do **Node.js**. 

Ele serve para baixar, instalar, atualizar e remover códigos prontos (bibliotecas e ferramentas) criados por outros desenvolvedores. 

Ele funciona com um grande site de códigos e um programa no terminal.

Normalmente, ele é instalado automaticamente junto com o Node.js.

## 🚀 Como verificar se o npm está instalado?
Para verificar se o `npm` está instalado em seu sistema, abra o terminal ou prompt de comando e digite:

```sh
npm --version
```

Se o `npm` estiver instalado corretamente, você verá uma saída semelhante a:

```
11.17.0
```

## ⏫ Atualizar o npm

Para atualizar o npm para a versão estável mais recente:

```
npm install -g npm@latest
```

Depois, verifique a versão instalada:

```
npm --version
```

No Windows, pode ser necessário fechar e abrir novamente o terminal. Caso a atualização não seja aplicada, outra opção é atualizar o próprio Node.js.

## 🏗️ Como criar um projeto com npm?

Entre no diretório em que o projeto será criado:

```
mkdir meu-projeto
cd meu-projeto
```

Inicialize o projeto:

```
npm init
```

O npm fará algumas perguntas e criará o arquivo `package.json`.

Para aceitar automaticamente as configurações padrão:

```
npm init -y
```

## 📦 Como instalar pacotes com npm?

Para instalar um pacote no projeto:

```
npm install nome-do-pacote
```

Exemplo: instalando o `axios`, uma biblioteca utilizada para realizar requisições HTTP:

```
npm install axios
```

O pacote será registrado em `dependencies` no `package.json`:

```
{
  "dependencies": {
    "axios": "^1.0.0"
  }
}
```

A versão apresentada é apenas um exemplo. O npm registrará a versão realmente instalada.

## 🛠️ Como instalar uma dependência de desenvolvimento?

Dependências utilizadas apenas durante o desenvolvimento devem ser instaladas com `--save-dev` ou `-D`:

```
npm install --save-dev nome-do-pacote
```

Forma abreviada:

```
npm install -D nome-do-pacote
```

Exemplo:

```
npm install -D typescript
```

Esses pacotes são registrados em `devDependencies`:

```
{
  "devDependencies": {
    "typescript": "^5.0.0"
  }
}
```

## 🎯 Como instalar uma versão específica?

Utilize `@` seguido da versão:

```
npm install nome-do-pacote@versão
```

Exemplo:

```
npm install lodash@4.17.21
```

Para solicitar a versão mais recente:

```
npm install nome-do-pacote@latest
```

## 📂 Como instalar as dependências de um projeto existente?

Quando o projeto já possui um `package.json`, execute:

```
npm install
```

O npm lerá o `package.json` e instalará as dependências dentro do diretório `node_modules`.

## 📜 Como listar os pacotes instalados?

Para listar as dependências principais do projeto:

```
npm list --depth=0
```

Para listar pacotes instalados globalmente:

```
npm list -g --depth=0
```

## 🔍 Como verificar pacotes desatualizados?

Execute:

```
npm outdated
```

## 🔄 Como atualizar os pacotes do projeto?

Para atualizar as dependências respeitando os intervalos de versões definidos no package.json:

```
npm update
```

Esse comando atualiza os pacotes do projeto. Ele é diferente do comando utilizado para atualizar o próprio npm.

## 🗑️ Como remover um pacote?

Para remover um pacote do projeto:

```
npm uninstall nome-do-pacote
```

Exemplo:

```
npm uninstall axios
```

O pacote também será removido do `package.json`.

Para remover um pacote global:

```
npm uninstall -g nome-do-pacote
```

## 🌍 Como instalar um pacote globalmente?

Pacotes que fornecem ferramentas de linha de comando podem ser instalados globalmente com `-g`:

```
npm install -g nome-do-pacote
```

Bibliotecas utilizadas pelo código do projeto normalmente devem ser instaladas localmente, sem `-g`.