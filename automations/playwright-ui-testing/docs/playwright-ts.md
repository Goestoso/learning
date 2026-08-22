# Guia Rápido sobre Playwright com TypeScript

## 📚 Pré-requisitos

Antes de estudar este guia, é recomendável possuir conhecimentos básicos de:

- JavaScript;
- TypeScript;
- Node.js;
- npm e npx;
- utilização do terminal.

Em JavaScript e TypeScript, é especialmente útil conhecer:

- variáveis e tipos de dados;
- condicionais e loops;
- funções tradicionais e arrow functions;
- arrays e objetos;
- classes;
- `import` e `export`;
- Promises;
- `async` e `await`.

> Não é necessário dominar todos esses assuntos para começar. Entretanto, compreender os fundamentos facilitará a leitura, a criação e a manutenção dos testes.

## 🎭 O que é Playwright?
Playwright é uma ferramenta de código aberto desenvolvida pela Microsoft para automação de navegadores web.

Seu framework de testes, chamado **Playwright Test**, é utilizado principalmente para realizar testes de ponta a ponta — end-to-end ou E2E — em aplicações web modernas.

Ele oferece recursos como:

- execução de testes;
- assertions;
- isolamento entre testes;
- execução paralela;
- geração de relatórios;
- depuração;
- captura de screenshots, vídeos e traces;
- suporte a Chromium, Firefox e WebKit.

Além dos testes E2E, sua biblioteca de automação também pode ser utilizada para automatizar tarefas e interações em navegadores.

## 🔧 Como instalar Playwright?
Para instalar o Playwright em um projeto Node.js novo ou existente, abra o terminal no diretório desejado e execute:

```
npm init playwright@latest
```

Durante a instalação, serão apresentadas algumas opções:

1. Escolher entre TypeScript e JavaScript;
2. Definir o diretório dos testes;
3. Adicionar ou não um workflow do GitHub Actions;
4. Instalar os navegadores utilizados pelo Playwright.

Para este guia, selecione **TypeScript**.

A estrutura inicial será semelhante a:

```
meu-projeto/
├── tests/
│   └── example.spec.ts
├── node_modules/
├── package.json
├── package-lock.json
└── playwright.config.ts
```

## ▶️ Como executar testes com Playwirght?
Para executar todos os testes:

```
npx playwright test
```

Por padrão, os testes são executados em modo **headless**, sem exibir a janela do navegador.

> ***Executar mostrando o navegador***

```
npx playwright test --headed
```

> ***Executar pela interface visual***

```
npx playwright test --ui
```

O modo UI permite acompanhar os testes, visualizar cada etapa, consultar erros e utilizar ferramentas de depuração.

> ***Executar um arquivo específico***

```
npx playwright test tests/example.spec.ts
```

> ***Executar em um navegador específico***

```
npx playwright test --project=chromium
```

Outras possibilidades:

```
npx playwright test --project=firefox
```

```
npx playwright test --project=webkit
```

> ***Executar em modo de depuração***

```
npx playwright test --debug
```

Esse comando abre o navegador e o Playwright Inspector, permitindo executar o teste passo a passo.

> ***Abrir o relatório dos testes***

```
npx playwright show-report
```

> ***Executar casos de testes específicos***

```
npx playwright test -g "deve realizar login"
```

Também é possível usar o nome do arquivo e `-g` juntos:

```
npx playwright test tests/login.spec.ts -g "login válido"
```

- 💡 O `-g` é ideal para uma execução temporária porque não exige alterar o código.

## 🧪 Como criar o primeiro teste?

Dentro do diretório `tests`, crie um arquivo chamado:

- *primeiro-teste.spec.ts*

Adicione o seguinte código:

```
import { test, expect } from "@playwright/test";

test("deve abrir a página Example", async ({ page }) => {
  await page.goto("https://example.com");

  await expect(page).toHaveTitle(/Example/);
});
```

Execute o teste:

```
npx playwright test tests/primeiro-teste.spec.ts
```

Nesse código:

- `test()` declara o teste;
- `async` indica que o teste executará operações assíncronas;
- `{ page }` fornece uma página isolada do navegador;
- `page.goto()` acessa uma URL;
- `expect()` realiza uma verificação;
- `toHaveTitle()` verifica o título da página;
- `await` aguarda a conclusão de cada operação.

## 🎥 Como gerar testes automaticamente?

O Playwright possui uma ferramenta chamada Codegen, que registra interações realizadas no navegador e sugere o código correspondente:

```
npx playwright codegen https://example.com
```

Ao clicar, preencher campos e navegar pela página, o Codegen gera comandos Playwright automaticamente.
