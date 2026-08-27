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

## ⏱️ Como configurar timeouts?

Um **timeout** define por quanto tempo o Playwright deve aguardar uma operação terminar antes de considerá-la uma falha.

Todos os valores são informados em **milissegundos**. Por exemplo:

- `1_000` representa 1 segundo;
- `5_000` representa 5 segundos;
- `30_000` representa 30 segundos.

O Playwright possui diferentes tipos de timeout porque cada um controla um escopo específico da execução.

> ***Global timeout***

O `globalTimeout` limita a duração da **execução completa da suíte**, considerando todos os arquivos, projetos, testes e tentativas de repetição.

Seu valor padrão é `0`, que significa que não existe um limite global. Esse timeout é especialmente útil em ambientes de integração contínua — CI — para impedir que uma execução inteira permaneça ativa indefinidamente.

Ele é configurado no arquivo `playwright.config.ts`:

```
import { defineConfig } from "@playwright/test";

export default defineConfig({
  globalTimeout: 60 * 60 * 1_000, // 1 hora para toda a execução
});
```

Quando esse tempo é atingido, o Playwright interrompe a execução da suíte, mesmo que ainda existam testes pendentes.

> ***Test timeout***

O `timeout` limita a duração de **cada teste individualmente**. Seu valor padrão é `30_000`, ou seja, 30 segundos.

Esse tempo inclui a função do teste, as fixtures utilizadas e os hooks associados, como `beforeEach`. Ele não representa uma espera específica por um elemento: é o orçamento total de tempo disponível para o teste.

Para definir o valor padrão de todos os testes:

```
import { defineConfig } from "@playwright/test";

export default defineConfig({
  timeout: 60_000, // 1 minuto para cada teste
});
```

Também é possível alterar o timeout de um teste específico:

```
import { test } from "@playwright/test";

test("deve concluir uma operação demorada", async ({ page }) => {
  test.setTimeout(90_000);

  await page.goto("https://example.com");
});
```

Para aumentar o timeout com base no valor já configurado, utilize `testInfo`:

```
test("deve concluir uma operação demorada", async ({ page }, testInfo) => {
  testInfo.setTimeout(testInfo.timeout + 30_000);

  await page.goto("https://example.com");
});
```

> O timeout de uma operação individual não aumenta o timeout total do teste. Por exemplo, uma ação configurada para aguardar 60 segundos ainda será interrompida se o test timeout restante for de apenas 20 segundos.

> ***Action timeout***

O `actionTimeout` limita cada **ação executada pelo Playwright**, como `click()`, `fill()`, `check()` e `press()`.

Seu valor padrão é `0`, que significa que não existe um limite separado para ações. Mesmo assim, a ação continua limitada pelo timeout total do teste.

Para definir um valor padrão para todas as ações:

```
import { defineConfig } from "@playwright/test";

export default defineConfig({
  use: {
    actionTimeout: 10_000, // 10 segundos para cada ação
  },
});
```

Também é possível definir o timeout somente para uma ação:

```
await page.getByRole("button", { name: "Enviar" }).click({
  timeout: 5_000,
});
```

Ou definir o timeout padrão das ações realizadas por uma página:

```
page.setDefaultTimeout(10_000);
```

O auto-waiting continua funcionando normalmente: antes de executar a ação, o Playwright espera o elemento satisfazer as condições necessárias, como estar visível, estável e habilitado, até o timeout aplicável terminar.

> ***Expect timeout***

O timeout de `expect` controla por quanto tempo as **assertions assíncronas** podem tentar novamente antes de falhar. Seu valor padrão é `5_000`, ou seja, 5 segundos.

Assertions baseadas em locators, como `toBeVisible()` e `toHaveText()`, consultam novamente a página até que a condição seja satisfeita ou o timeout termine.

Para definir o valor padrão das assertions:

```
import { defineConfig } from "@playwright/test";

export default defineConfig({
  expect: {
    timeout: 10_000, // 10 segundos para assertions assíncronas
  },
});
```

Também é possível configurar uma assertion específica:

```
await expect(page.getByText("Operação concluída")).toBeVisible({
  timeout: 15_000,
});
```

Assertions genéricas sobre valores já obtidos não possuem auto-retry:

```
const status = "concluído";

expect(status).toBe("concluído");
```

Nesse exemplo, a comparação acontece imediatamente porque `status` é apenas um valor JavaScript, e não um locator consultado novamente pelo Playwright.

> ***Navigation timeout***

O `navigationTimeout` limita operações de **navegação**, como `page.goto()`, `page.reload()`, `page.goBack()` e `page.goForward()`.

Seu valor padrão é `0`, que significa que não existe um limite separado para navegações. A operação ainda permanece limitada pelo timeout total do teste.

Para definir um valor padrão para todas as navegações:

```
import { defineConfig } from "@playwright/test";

export default defineConfig({
  use: {
    navigationTimeout: 30_000, // 30 segundos para cada navegação
  },
});
```

Também é possível configurar uma navegação específica:

```
await page.goto("https://example.com", {
  timeout: 15_000,
});
```

Ou definir o timeout padrão de navegação de uma página:

```
page.setDefaultNavigationTimeout(30_000);
```

Quando `navigationTimeout` e `actionTimeout` estão configurados, o timeout de navegação tem prioridade para operações de navegação.

> ***Configuração completa***

Os cinco timeouts podem ser visualizados juntos no `playwright.config.ts`:

```
import { defineConfig } from "@playwright/test";

export default defineConfig({
  globalTimeout: 60 * 60 * 1_000,
  timeout: 60_000,

  expect: {
    timeout: 10_000,
  },

  use: {
    actionTimeout: 10_000,
    navigationTimeout: 30_000,
  },
});
```

Resumo dos escopos:

- `globalTimeout`: limita toda a execução da suíte;
- `timeout`: limita cada teste;
- `actionTimeout`: limita cada ação;
- `expect.timeout`: limita assertions assíncronas com retry;
- `navigationTimeout`: limita cada navegação.

Quando houver uma configuração específica na própria operação, ela terá prioridade sobre o valor padrão correspondente. Entretanto, os limites do teste e da execução global continuam válidos.

> 💡 Aumentar timeouts indiscriminadamente pode esconder lentidão ou problemas de sincronização. Prefira locators estáveis, assertions com auto-retry e esperas baseadas em condições reais da interface.
