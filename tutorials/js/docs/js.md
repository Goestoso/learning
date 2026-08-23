# Guia Rápido sobre JavaScript

## 👨‍💻 O que é JavaScript (JS)?
JavaScript é uma linguagem de programação de **alto nível** usada para criar **interatividade**, **animações** e **comportamento dinâmico** em **páginas da web**.

## 🧱 O que é TypeScript (TS)?
TypeScript é uma linguagem de programação de **código aberto** criada pela Microsoft. 

Ela funciona como um **superconjunto do JavaScript**, adicionando **tipagem estática com inferência de tipos** e **anotações explícitas opcionais**, **interfaces**, **tipos personalizados**, **generics**, **detecção antecipada de erros** e melhor integração com editores de código.

No final, **o código é convertido em JavaScript puro** para rodar nos navegadores ou no **Node.js**.

## 🌐 O que é Node.js?
Node.js é um **ambiente de execução** que permite executar JavaScript fora do navegador. Ele utiliza o motor V8 e pode ser usado para criar servidores, APIs, automações e ferramentas de linha de comando.

## 🔧 Como instalar Node.js?
Para instalar o `Node.js` no seu computador:

1. Acesse o site oficial: [nodejs.org](https://nodejs.org/en/download)
2. Baixe a versão mais recente compatível (recomenda-se a versão **LTS - Long Term Support**) com seu sistema operacional.
3. Execute o instalador e siga as instruções.
4. Após a instalação, verifique se tudo está funcionando abrindo o terminal e digitando:
```sh
   node --version
```
## 💻 Como desenvolver em JS?
Para programar em JavaScript, você pode utilizar diferentes editores de código e IDEs:
- **Visual Studio Code** – Leve, rápido e com suporte a extensões.
- **WebStorm** – Robusto e com ferramentas avançadas nativas, tendo foco total em JavaScript e TypeScript, sendo gratuito para uso não comercial e pago para uso comercial.
- **Sublime Text** - Ultrarápido, interface limpa e ideal para computadores mais fracos.

## ▶️ Como executar programas JavaScript?
Depois de instalar o **Node.js**, crie um arquivo `app.js`:
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

## 🧱 Como instalar, executar e verificar TypeScript?

### Instalar o TypeScript

Primeiro, crie ou acesse o diretório do projeto:

```sh
mkdir meu-projeto-typescript
cd meu-projeto-typescript
```

Inicialize o projeto npm:

```sh
npm init -y
```

Instale o TypeScript como dependência de desenvolvimento:

```sh
npm install -D typescript
```

### Verificar a instalação

Execute:

```sh
npx tsc --version
```

O `tsc` é o compilador do TypeScript.

### Criar um arquivo TypeScript

Crie um arquivo chamado `app.ts`:

```ts
const nome: string = "Gabriel";
const idade: number = 22;

console.log(`${nome} tem ${idade} anos.`);
```

A extensão `.ts` identifica um arquivo TypeScript.

### Verificar os tipos sem gerar JavaScript

Para verificar se o arquivo contém erros de tipagem:

```sh
npx tsc app.ts --noEmit
```

A opção `--noEmit` instrui o TypeScript a verificar o código sem gerar um arquivo JavaScript.

Por exemplo:

```ts
const idade: number = "vinte e dois";
```

A verificação apresentará um erro porque uma `string` não pode ser atribuída a uma variável do tipo `number`.

### Compilar TypeScript para JavaScript

Para converter o arquivo `app.ts` em JavaScript:

```sh
npx tsc app.ts
```

Esse comando criará:

```text
app.js
```

Agora, execute o JavaScript gerado:

```sh
node app.js
```

A saída será:

```text
Gabriel tem 22 anos.
```

O fluxo tradicional é:

```text
app.ts → verificação e compilação → app.js → execução pelo Node.js
```

### Criar o arquivo de configuração do TypeScript

Para criar o `tsconfig.json`:

```sh
npx tsc --init
```

O `tsconfig.json` centraliza as configurações do TypeScript, como:

* nível de rigor da tipagem;
* versão do JavaScript gerado;
* sistema de módulos;
* diretórios de entrada e saída;
* regras de compilação.

Depois de criar o `tsconfig.json`, é possível verificar todo o projeto:

```sh
npx tsc --noEmit
```

Ou compilar todo o projeto:

```sh
npx tsc
```

### Executar TypeScript diretamente com Node.js

Versões modernas do Node.js conseguem executar parte da sintaxe TypeScript diretamente:

```sh
node app.ts
```

Entretanto, essa execução apenas remove as anotações de tipos compatíveis e não realiza a verificação estática.

Para verificar os tipos, continue utilizando:

```sh
npx tsc --noEmit
```

Alguns recursos TypeScript que exigem geração adicional de JavaScript podem não funcionar na execução direta. Para maior compatibilidade, prefira compilar com `tsc`.

Assim, cada comando possui uma responsabilidade:

| Comando               | Finalidade                                        |
| --------------------- | ------------------------------------------------- |
| `npx tsc --noEmit`    | Verifica os tipos sem gerar arquivos              |
| `npx tsc`             | Verifica e compila TypeScript                     |
| `node app.js`         | Executa o JavaScript compilado                    |
| `node app.ts`         | Executa diretamente sintaxe TypeScript compatível |

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
Se o npm estiver instalado corretamente, o terminal mostrará a versão instalada.
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

## ⚡ O que é npx?

O `npx` permite executar comandos disponibilizados por pacotes npm sem precisar instalar essas ferramentas globalmente.

Quando o comando é executado, o `npx`:

1. Procura o pacote nas dependências locais do projeto;
2. Executa a versão encontrada em `node_modules`;
3. Caso o pacote não esteja instalado, pode solicitar autorização para baixá-lo temporariamente para o cache do npm.

Exemplo com Playwright:

```sh
npx playwright test
```

Nesse caso, o `npx` procura e executa o Playwright instalado no projeto.

Outros exemplos:

```sh
npx playwright test --ui
```

```sh
npx tsc --noEmit
```

```sh
npx eslint .
```

### Qual é a diferença entre npm e npx?

| Comando         | Finalidade                                     |
| --------------- | ---------------------------------------------- |
| `npm install`   | Instala um pacote                              |
| `npm uninstall` | Remove um pacote                               |
| `npm update`    | Atualiza os pacotes                            |
| `npm run`       | Executa scripts do `package.json`              |
| `npx`           | Executa uma ferramenta fornecida por um pacote |

Por exemplo:

```sh
npm install -D @playwright/test
```

Esse comando instala o Playwright como dependência de desenvolvimento.

Depois:

```sh
npx playwright test
```

Esse comando executa a ferramenta instalada.

> ⚠️ Caso o pacote não esteja instalado, confira atentamente o nome antes de permitir que o npx faça o download. Um erro de digitação pode resultar na execução de um pacote diferente do desejado.


