<h1>Treinamentos básicos e manuais de apoio 📋🤓</h1> 

→ Espaço dedicado para auxiliar na lógica da programação e estrutura de linguagens como o Python, JS e Java, além de oferecer suporte sobre a ferrramenta de versionamento Git, discorrendo sobre o que ele é e como ele funciona.

<div style="display: flex; justify-content: center; gap: 20px;">
<figure style="margin-right: 20px;">
  <img align="center" alt="Goes-Python" height="100" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg"  >
   <figcaption><b>Aproveite  os arquivos <code>.py</code> para estudar sobre o Python!</b></figcaption>
</figure>
</div> 

🆕 Atualmente desenvolvendo a branch [games](https://github.com/Goestoso/learning/edit/games)!
<br>
<br>
🆕 Elaborando códigos em `Python` para auxiliar na aprendizagem!
<br>
<br>
🗞️ Em breve tópicos sobre a lógica de programação e a estrutrua das linguagens Python, JS e Java...

<h2>😼 Git</h2>

<h3>O que é o Git?</h3>

- O Git é um sistema de controle de versão distribuído, ou seja, isso significa que cada clone local de um projeto é um repositório completo de ___controle de versão___.
- Esses repositórios locais funcionam de forma independente, facilitando o trabalho offline ou remoto.

> Diagrama geral do Git:

```
            master 
              |
              v
  Commit A --> Commit B --> Commit C
               |              |
               |              |
               |             dev
               |              |
               |              v
               |--> Commit D --> Commit E
               |
              feature
               |
               v
             Commit F --> Commit G

```

🌳 O Git segue uma ___estrutura de árvore___ para organizar os arquivos e diretórios em um repositório.

- `master` é a ramificação, `branch` base (raiz) do projeto.
- `branch` é a referência móvel para os `commits` e sempre aponta para o `commit` mais recente.
- Os `commits` são os controles de versões desenvolvidos.
- Cada `commit` contém informações sobre as alterações feitas nos arquivos (os `blobs`) e também aponta para o `commit` anterior (o nó pai).
- Dessa forma, os `commits` permitem reverter facilmente as alterações para as versões anteriores, alcançando até o `commit` mais antigo.
- `dev` e `feature` são `branches` filhas criadas a partir da `master` que possuem seus respectivos `commits`.
- Nas `branches` filhas você pode fazer todas as alterações necessárias sem afetar o código existente na branch principal `master`.

> Os ponteiros dos commits:
```
        +--------------------+
        |     Repositório    |
        +--------------------+
                |
                v
        +--------------------+
        |       HEAD         | 
        +--------------------+
                |
                v
        +--------------------+
        |     master         |
        | (current branch)   |
        +--------------------+
                |
                v
        +--------------------+
        |    Commit C        |
        +--------------------+
                |
                v
        +--------------------+
        |    Commit B        |
        +--------------------+
                |
                v
        +--------------------+
        |    Commit A        |
        +--------------------+

```

- `HEAD` é um ponteiro que sempre aponta para o `commit` mais recente na `branch` atual (`master` neste caso).

<h3>Como o Git funciona?</h3>

- O Git rastreia as alterações em arquivos e mantém um histórico completo de todas as modificações.
- Ele permite que você volte para versões anteriores do código, compare alterações e colabore com outras pessoas.

> Instalação e Configuração do Git:
- 🔗 <a href="https://git-scm.com/download/win" target="_blank">Download page ⬇️</a>
```
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@exemplo.com"
```
> Estrutura de um repositório Git:
```
Repositório Git
|
+-- .git/                # Diretório Git interno
|   +-- branches/        # Informações de branches
|   +-- hooks/           # Scripts de gancho
|   +-- info/            # Informações adicionais
|   +-- objects/         # Objetos de armazenamento de dados
|   +-- refs/            # Referências (branches e tags)
|       +-- heads/       # Branches locais
|       |   +-- master   # Branch master
|       |   +-- dev      # Branch dev
|       +-- remotes/     # Branches remotas
|           +-- origin/  # Repositório remoto
|               +-- master
|
+-- Working Directory    # Diretório de trabalho
|   +-- file1.txt        # Arquivo rastreado
|   +-- file2.txt        # Outro arquivo rastreado
|
+-- Staging Area         # Área de preparação para commits
|   +-- file1.txt        # Arquivo preparado para commit
|
+-- Commits
|   +-- Commit A         # Primeiro commit
|   +-- Commit B         # Segundo commit
|   +-- Commit C         # Terceiro commit
|
+-- Branches
|   +-- master           # Branch principal
|   +-- dev              # Branch de desenvolvimento
|   +-- feature          # Branch de funcionalidades

```

<h4>O fluxo de trabalho básico do Git</h4> 

- ___Início:___ Iniciar um repositório local.
```
git init
```
- ___Clonar:___ Criar uma cópia local de um repositório remoto.
```
git clone <URL_do_repositório>
```
- ___Status:___ Verificar o status do repositório.
```
git status
```
- ___Adicionar e modificar arquivos:___ Fazer alterações nos arquivos do projeto.
> Para adicionar todos os arquivos modificados e excluídos:
```
git add .
```
> Para adicionar arquivos específicos:
```
git add <nome_do_arquivo>
```
- ___Commit:___ Salvar as alterações em um ponto específico no histórico (cada `commit` tem um código _hash_ único para identificá-lo).
> Criar um commit:
```
git commit -m "Sua mensagem de commit"
```
> Checkout de um Commit Específico (muda o estado do repositório para um commit específico sem criar uma nova branch):
```
git checkout <commit_hash>
```
> Resetar o Repositório para um Commit Específico:
```
git reset --hard <commit_hash>
```
> Resetar o Índice do Commit para um Commit Específico (sem resetar o repositório):
```
git reset --soft <commit_hash>
```
> Criar uma Nova Branch a Partir de um Commit Específico:
```
git checkout -b nome_da_branch <commit_hash>
```
> Verificar Diferenças Entre Commits Específicos:
```
git diff <commit1_hash> <commit2_hash>
```
> Verificar Diferenças Entre Um Commit Especifico e o Estado Atual:
```
git diff <commit_hash>
```
> Verificar Diferenças Entre o Último Commit e o Estado Atual:
```
git diff HEAD
```
- ___Log:___ Ver o histórico de `commits` da `branch` atual.
> Visualizar todo o histórico de commits:
```
git log
```
> Exibir o log com formato simplificado (uma linha por commit):
```
git log --oneline
```
> Log com gráfico mostrando branches e merges:
```
git log --graph --oneline --all
```
> Mostrar Detalhes de um Commit Específico:
```
git show <commit_hash>
```
> Visualizar o Histórico de um Arquivo Específico:
```
git log -- <caminho_do_arquivo>
```
```
git log --follow -- <caminho_do_arquivo>
```
> Blame - Ver Quem Mudou Cada Linha de um Arquivo:
```
git blame <caminho_do_arquivo>
```
> Pesquisar por Mensagens de Commit:
```
git log --grep="texto_da_busca"
```
```
git log --oneline --grep="correção de bug"
```
> Log com Limitação de Tempo:
```
git log --since="2 weeks ago"
```
> Histórico de todos os movimentos do HEAD (cada estado é marcado no formato HEAD@{_n_})
```
git reflog
```
- ___Branches:___ Criar ramificações para desenvolver recursos separadamente.
> Para listar todas as ramificações (branches):
```
git branch
```
> Para criar uma nova branch:
```
git branch <nome_da_branch>
```
> Para mudar para uma branch específica:
```
git checkout <nome_da_branch>
```
> Para criar uma nova branch e mudar para essa nova branch:
```
git checkout -b <nome_da_branch>
```
> Para deletar uma branch:
```
git branch -d nome_da_branch
```
> Para renomear uma branch:
```
git branch -m nome_antigo nome_novo
```
- ___Merge:___ Integrar as alterações de uma ramificação em outra.
> Primeiro, vá para a branch de destino (por exemplo, a branch principal):
```
git checkout main
```
> Em seguida, faça o merge da outra branch (por exemplo, uma feature branch):
```
git merge <nome_da_outra_branch>
```
- ___Push:___ Enviar as alterações para um repositório remoto (como o GitHub).
```
git push origin <nome_da_branch>
```
- ___Pull:___ Obter as alterações do repositório remoto para o local.
```
git pull origin <nome_da_branch>
```

<h4>🔀 Merge ❌ Rebase 🔃</h4>

→ O `merge` e o `rebase` são duas estratégias distintas no Git para integrar mudanças entre branches. 

> Merge é Preferível Quando:
- ___Preservar o Contexto Original___: Você deseja manter um registro claro de onde e quando as branches foram mescladas.
- ___Colaboração Intensa___: Várias pessoas estão trabalhando na mesma área do código e podem beneficiar da visibilidade clara dos commits de merge.
> Rebase é Preferível Quando:
- ___Manter um Histórico Linear e Limpo___: Você prefere um histórico de commits mais organizado e fácil de seguir.
- ___Integração Contínua___: Você está trabalhando em uma feature isolada e deseja rebasear suas mudanças na branch principal antes de finalizar.

⚠️ Tanto o merge quanto o rebase podem gerar ___conflitos no Git___.

<h5>🛑 Conflitos</h5>

> O que são conflitos?
- Conflitos ocorrem quando o Git não consegue determinar automaticamente como combinar as alterações de duas ou mais versões diferentes de um mesmo arquivo.
- Isso pode acontecer, por exemplo, quando duas `branches` modificam a mesma parte de um arquivo de maneiras que não podem ser automaticamente mescladas.
> Como eles acontecem?
- ___Merge Conflitos___: Durante um merge, o Git tenta combinar as alterações de duas `branches`, se houver mudanças conflitantes no mesmo arquivo e nas mesmas linhas, o Git não pode determinar automaticamente como mesclá-las.
- ___Rebase Conflitos___: Durante um rebase, cada commit da branch sendo rebaseada é aplicado sequencialmente sobre a base branch, se um `commit` altera o mesmo local do código que outro `commit` na `base branch`, pode ocorrer um conflito.
> Como resolver conflitos?
- ___Identificar os Conflitos___: Quando um conflito ocorre, o Git marca o arquivo conflitante com marcações especiais que indicam as versões em conflito.
```
<<<<<<< HEAD
Código da branch atual (HEAD)
=======
Código da branch sendo mesclada/rebaseada
>>>>>>> branch_origem
```
- Essas marcações indicam onde começa e termina cada seção conflitante. Você verá isso diretamente nos arquivos afetados quando executar um git merge ou git rebase e encontrar conflitos.
- ___Resolver os Conflitos___: Para resolver um conflito, você deve editar os arquivos conflitantes manualmente para remover as marcações do Git e decidir como as alterações devem ser combinadas.
- ___Concluir a Mesclagem ou Rebase___:
> Para Merge:
- Adicione os arquivos alterados (resolvidos) ao índice do Git usando git add arquivo_conflitante.
- Continue o merge com `git merge --continue` ou `git commit` (se o merge estiver sendo feito diretamente na linha de comando).
> Para Rebase:
- Continue o rebase com `git rebase --continue` após resolver cada conflito.
- Às vezes, pode ser necessário usar `git rebase --skip` ou `git rebase --abort` se ocorrerem problemas durante o processo de rebase.
> Editor Vim:
- `Vim` é um editor de texto altamente configurável e poderoso, amplamente utilizado no desenvolvimento de software, administração de sistemas e muitos outros contextos onde a edição de texto eficiente é necessária (_prompt_: `vim nome_do_arquivo`).
- Às vezes, o editor `Vim` é aberto no terminal para editar uma mensagem de `commit`; digite `i` para entrar no _modo de inserção_ (descrever o seu `commit`), pressione `Esc` para sair do _modo de inserção_, digite `:w` e pressione `Enter` para salvar as alterações e `:q` (`:q!` sai sem salvar) e pressione `Enter` para sair (`:wq` + `Enter` faz alterações, salva e fecha o editor em um único comando). 

<h5>🔀 Merge</h5>

```
git checkout branch_destino
git merge branch_origem
```

> O que é Merge?
- O `merge` no Git combina as alterações de uma `branch` para outra, criando um novo `commit` que representa a junção das duas linhas de desenvolvimento.
- Ele preserva o histórico de commits original de cada branch.
- O histórico de `commits` mostra claramente onde e como as `branches` foram mescladas, mantendo uma ___visão cronológica do desenvolvimento___.

> Para que Serve o Merge?
- ___Integração de Trabalho Paralelo___: Permite que várias pessoas trabalhem em diferentes funcionalidades ou correções simultaneamente e, em seguida, combinem suas alterações de volta à branch principal.
- ___Preservação do Histórico___: Mantém o histórico de commits original de cada branch, o que pode ser útil para auditoria e depuração de problemas.

<h5>🔃 Rebase</h5>

```
git checkout branch_origem
git rebase branch_destino
```

> O que é Rebase?
- O rebase é outra forma de integrar mudanças, mas em vez de criar um novo `commit` de merge, ele ___reescreve o histórico de `commits` da branch_origem sobre a branch_destino___.
- Isso resulta em uma ___linha de tempo linear e mais limpa___, sem `commits` de merge extras.

> Para que Serve o Rebase?
- ___Manter um Histórico Linear___: Ajuda a manter um histórico de commits limpo e linear, facilitando a revisão de código e a identificação de mudanças específicas.
- ___Facilitar a Revisão de Código___: Reduz a poluição do histórico com commits de merge, tornando mais claro quem fez o que e quando.

> Iniciar um rebase interativo navegando pelos 3 últimos commits:
```
git rebase -i HEAD~3
```
> Iniciar um rebase interativo navegando para um commit específico:
```
git rebase -i <commit_hash>
```
> Opções do rebase interativo:

- `pick` ou `p`: Manter o commit como está

```
pick 1a2b3c4 Mensagem do commit
```

- `reword` ou `r`: Usar o commit, mas permite editar a mensagem do commit.

```
reword 1a2b3c4 Mensagem antiga do commit
```

- `edit` ou `e`: Usar o commit, mas parar para fazer alterações manuais.

```
edit 1a2b3c4 Mensagem do commit
```
- `squash` ou `s`: Mesclar este commit com o commit anterior e permitir editar a mensagem combinada.

```
squash 1a2b3c4 Mensagem do commit
```

- `fixup` ou `f`: Mesclar este commit com o commit anterior sem editar a mensagem.

```
fixup 1a2b3c4 Mensagem do commit
```

- `exec` ou `x`: Executar um comando shell.

```
exec echo "Este é um comando shell"
```

- `drop` ou `d`: Remover o commit da história.

```
drop 1a2b3c4 Mensagem do commit
```

<h4>👨‍💻 Colaboração remota</h4>

☁️  Um repositório remoto em Git é um ambiente importante para colaborar com outros desenvolvedores e trabalhar em projetos hospedados em plataformas como GitHub.

- Adicionar um Repositório Remoto:
```
git remote add origin https://github.com/usuario/repositorio.git
```
> `origin` é o nome padrão dado ao repositório remoto; você pode escolher qualquer nome, mas `origin` é amplamente utilizado por _convenção_.

- Fetch e Push URLs: Ao adicionar um repositório remoto, você verá que há dois tipos de URLs associados, o fetch e o push.
> `fetch`: Usada para obter (fetch) dados do repositório remoto, quando você executa ___git fetch___ ou ___git pull___, o Git usa esta URL para baixar `commits`, `branches` e `tags` do repositório remoto para o seu repositório local.
> <br>
> `push`: Usada para enviar (push) seus `commits` do repositório local para o repositório remoto, quando você executa ___git push___, o Git usa esta URL para transferir seus `commits` para o repositório remoto.
- Listar as URLs de `fetch` e `push` configuradas para seu repositório remoto:
```
git remote -v
```
- Renomear as referências de `fetch` e `push` (conhecidas como referências `remote`):
```
git remote rename learning origin
```
- Alterar a refrência de `fetch`:
```
git remote set-url origin [NEW_FETCH_URL]
```
- Alterar a referência de `push`:
```
git remote set-url --push origin [NEW_PUSH_URL]
```

- Branch Remota: Uma branch remota é uma branch que existe no repositório remoto (como GitHub) e é usada para compartilhar mudanças com outros colaboradores e manter o código sincronizado entre diferentes desenvolvedores.
> Ver Branches Remotas: ```git branch -r```
> <br>
> Sincronizar Branches Locais com Branches Remotas: ```git fetch```
> <br>
> Para criar uma cópia local de uma branch remota: ```git checkout -b nome_da_branch_local origin/nome_da_branch_remota```
> <br>
> Verificar todas as branches (locais e remotas): ```git branch -a```
> <br>
> Deletar uma branch remota: ```git push origin --delete nome_da_branch```

<h5>🔖 Tags</h5>

→ `Tags` no Git são referências que _apontam para pontos específicos na história_ do repositório, normalmente usadas para __marcar versões ou releases significativos__ de um projeto. 
- Elas são particularmente úteis para ___versionamento de software___ e para ___criar marcos importantes___ no desenvolvimento.
- Existem dois tipos principais de tags: tags leves (`lightweight tags`) e tags anotadas (`annotated tags`).

> `lightweight tags`: são basicamente ___um ponteiro para um `commit` específico___, não contêm metadados adicionais (como nome do autor, data, mensagem) e são criadas rapidamente e usadas quando não há necessidade de informações adicionais além do `commit` apontado.
<br>

> `annotated tags`: contêm metadados adicionais, como o nome do autor, data e uma mensagem, são armazenadas como objetos completos no banco de dados do Git e são preferíveis ___para marcar releases___, pois fornecem informações extras sobre a `tag`.

- Criar uma Tag Leve:

```
git tag nome_da_tag
```
> Exemplo:
```
git tag v1.0.0
```
- Criar uma Tag Anotada:
```
git tag -a nome_da_tag -m "mensagem da tag"
```
> Exemplo:
```
git tag -a v1.0.0 -m "Versão 1.0.0 - Primeira release estável"
```
- Listar Tags:
> Para listar todas as tags no repositório:
```
git tag
```
> Para listar tags com informações detalhadas (se são anotadas):
```
git show nome_da_tag
```
- Compartilhar Tags com o Repositório Remoto:
> Enviar uma Tag Específica
```
git push origin nome_da_tag
```
> Enviar Todas as Tags de Uma Vez
```
git push origin --tags
```
- Usar Tags:
> Checkout de uma Tag (para criar uma nova branch a partir de uma tag)
```
git checkout -b nome_da_nova_branch nome_da_tag
```
> Exemplo:
```
git checkout -b hotfix-v1.0.1 v1.0.0
```
- Remover Tags:
> Remover Tag Localmente
```
git tag -d nome_da_tag
```
> Remover Tag no Repositório Remoto
```
git push origin --delete tag nome_da_tag
```
- Comandos Úteis:
> Ver detalhes de uma tag: ```git show nome_da_tag```
> <br>
> Comparar diferenças entre tags: ```git diff tag1 tag2```
> <br>
> Listar commits associados a uma tag: ```git log nome_da_tag```

<h5>🔄️ Upstream</h5>

→ O termo "upstream" em Git refere-se a um repositório remoto a partir do qual você fez um `fork` ou do qual você ___deseja manter seu repositório sincronizado___. 
- No contexto de colaboração, especialmente em projetos _open-source_, "upstream" geralmente é o repositório original ou principal de onde você derivou seu repositório (`fork`).

> Diagrama de um repositório Git com upstream:
```
                +----------------------+
                |     Repositório      |
                |       Upstream       |
                |    (original/central)| 
                +----------------------+
                   |
                   |
                 (fetch/pull)
                   |
                   v
                +----------------------+
                |   Repositório Fork   |
                |      (pessoal)       |
                +----------------------+
                   |
                   |
                  (push)
                   |
                   v
                +----------------------+
                |  Working Directory   |
                |      (local)         |
                +----------------------+

```
- O ___Repositório Upstream___ é o repositório original ou central, muitas vezes _o repositório principal do projeto_.
- O ___Repositório Fork___ é uma cópia do repositório upstream no GitHub ou outra plataforma, usado _para desenvolver suas próprias mudanças sem afetar o repositório original_.
- O ___Working Directory___ é o diretório local no qual você faz suas mudanças e desenvolvimentos.

> Adicionar um Repositório Upstream:

```
git remote add upstream https://github.com/original_user/original_repo.git
```

> Verificar os Remotos Configurados:
```
git remote -v
```

> Buscar Atualizações do Upstream:
```
git fetch upstream
```

> Mesclar Atualizações do Upstream:
```
git merge upstream/main
```
```
git rebase upstream/main
```
<h5>🔁 Pull Request</h5>

→ Um `pull request` (PR) é um mecanismo para solicitar a integração de mudanças de uma `branch` (ou `fork`) para outra.

- Criar um Pull Request:
> Primeiro, você cria uma nova `branch` (geralmente a partir da `main` ou `master`) e faz `commits` com suas alterações.
> <br>
> Em seguida, você abre um `pull request` para a `branch` de destino (também conhecida como `base branch`), onde deseja mesclar suas alterações.
- Revisão de Código:
> Outros membros da equipe revisam suas mudanças, deixam comentários e sugerem modificações.
- Integração:
> Após a revisão e aprovação, suas mudanças são integradas à `base branch`.
- Fechar o Pull Request:
> Depois que o `pull request` é mesclado, ele pode ser fechado e removido da lista de `pull requests` ativos.

🤝 ___Facilita a colaboração___: permite que os membros da equipe revisem e discutam as mudanças antes da integração.
<br>
🏷️  ___Assegura qualidade do código___: ajuda a garantir que o código integrado atenda aos padrões de qualidade e não introduza problemas no projeto.
