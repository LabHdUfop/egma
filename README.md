# EGMA — Elefante–Goldfish Acadêmico

**Protocolo aberto, neutro quanto a agente, modelo e provedor, para enquadrar, planejar e auditar pesquisa acadêmica com apoio de IA.**

Versão 1.1.0 · Licença MIT · LABHD UFOP

> **Abstract (EN).** EGMA is an authorial protocol for framing, planning and auditing academic research with AI agents. It splits the work into a continuity context (Elephant, which holds the question, decisions, artifacts and state) and one or more isolated review contexts (Goldfish, which see only the assigned role, the authorized package and the criteria — never the elaboration conversation). It is harness-, model- and vendor-neutral, and it does not certify scientific validity, privacy or editorial approval.

---

## O problema que a EGMA ataca

Um agente que elabora um objeto e depois o revisa no mesmo contexto não produz revisão independente: revisa à luz da própria conversa, dos próprios atalhos e das próprias justificativas. A EGMA separa esses papéis em contextos distintos e exige que cada verificação deixe evidência observável. O resultado é um rastro auditável de *proposto / executado / verificado / pendente*.

## Os dois contextos

| Contexto | Papel | O que vê |
|---|---|---|
| **Elefante** | Continuidade: pergunta, decisões, artefatos, estado do projeto | Todo o projeto, inclusive o que ainda não foi aprovado |
| **Goldfish** | Revisão em contexto isolado, por papel fixo | Apenas o papel, o pacote autorizado e os critérios — nunca a conversa de elaboração nem pareceres alheios na primeira rodada |

Revisão feita pelo próprio Elefante é registrada como **revisão assistida**, não como independente.

## Instalação

Escolha uma das três formas. Nenhuma exige alterar modelo, provedor, assinatura, credenciais ou configuração global.

### 1. Skill nativa (recomendada)

Copie a pasta `egma/` **inteira** para o mecanismo de skills do seu agente, preservando `SKILL.md`, `references/`, `scripts/` e `templates/`. Não copie apenas o corpo do `SKILL.md`: os links são relativos.

### 2. Leitura explícita por projeto (sem suporte a skills)

Copie `egma/` para `.egm-academico/skill/` no projeto, crie `.egm-academico/ESTADO.md` a partir de `egma/templates/ESTADO.md` e acrescente um único bloco ao arquivo de instruções efetivamente carregado pelo seu agente (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`…). O bloco pronto está em [`egma/references/portabilidade.md`](egma/references/portabilidade.md).

### 3. Documento único (chat ou API sem sistema de arquivos)

Forneça [`EGMA_PORTATIL.md`](EGMA_PORTATIL.md) e indique a seção necessária. Sem busca, execução, persistência ou novos contextos, as verificações dependentes dessas capacidades devem ser registradas como **indisponíveis** — não prometidas.

**Sempre:** teste em sessão nova apenas com dados sintéticos. Um arquivo presente não comprova descoberta; um contexto novo não comprova isolamento nem privacidade.

## Modos de operação

| Modo | Quando usar |
|---|---|
| **Planejamento** | Explorar uma ideia ou possibilidades sem elaborar projeto |
| **Projeto novo** | Elaborar pergunta, literatura, protocolo, piloto, análise ou manuscrito |
| **Objeto pronto** | Auditar projeto, protocolo, análise ou manuscrito existente |
| **Manutenção** | Diagnosticar deriva ou criar estado para projeto anterior à EGMA |
| **Pontual** | Buscar, conferir referências, recalcular ou responder sem ciclo completo |

## Estrutura do repositório

```
egma/
├── SKILL.md                       núcleo operacional: princípios, modos, etapas
├── references/
│   ├── privacidade.md             triagem antes de transmitir material protegido
│   ├── projeto.md                 enquadramento, corpus, acervo cedido
│   ├── revisao.md                 preparar, executar, verificar e consolidar revisão Goldfish
│   ├── bibliografia.md            busca, identidade e sustentação de referências
│   ├── medidas-computacionais.md  justificar e testar medidas computacionais
│   ├── validacao-humana-cega.md   validação humana cega de medidas interpretativas
│   ├── registros.md               fichas, âncoras, matrizes, manifestos e índices
│   ├── manutencao.md              deriva e reconstrução de estado
│   ├── portabilidade.md           instalação e verificação
│   └── papeis/                    rubricas fixas de revisão (método, epistemologia,
│                                  argumentação, leitor ingênuo, bibliografia)
├── templates/ESTADO.md            índice inicial mínimo do projeto
├── scripts/verifica_citacoes.py   conferência auxiliar de citações literais em PDF
├── requirements.txt               dependências do script (Python + PyMuPDF)
└── README.md                      conteúdo e limites do pacote portátil
EGMA_PORTATIL.md                   versão monolítica para ambientes sem pastas
SHA256SUMS.txt                     hashes de integridade do pacote 1.1.0
tests/                             suíte de aceitação do script (11 casos sintéticos)
```

## Verificação de integridade

```bash
sha256sum -c SHA256SUMS.txt      # Linux/macOS/git-bash
```

Os hashes cobrem os 22 arquivos do pacote 1.1.0. Se algum falhar, o pacote foi alterado — não use.

## Testes

```bash
python tests/test_verifica_citacoes.py     # requer Python 3.9+ e PyMuPDF
```

Suíte de aceitação do `verifica_citacoes.py`: 11 casos sobre uma fixture inteiramente
sintética (os PDFs são gerados por PyMuPDF; nenhum dado de pesquisa é usado). Cobre
ocorrência única, repetição em páginas diferentes e na mesma página, ausência de texto,
citação entre páginas, PDFs homônimos, caminho explícito, fonte ausente, folha impressa
observada, offset declarado e identidade da fonte por SHA-256. Todos os 11 passam na
1.1.0; na 1.0.0 apenas 4 passavam.

## Limites — leia antes de usar

- A EGMA **não é um modelo** e **não garante** validade científica, privacidade, ausência de erro ou aprovação editorial.
- A EGMA **não certifica** revisão independente. O isolamento depende de como o ambiente realmente opera contexto, memória e herança — verifique no seu ambiente.
- A política de dados é do **produto, conta, plano e configuração** que você usa. Consulte [`egma/references/privacidade.md`](egma/references/privacidade.md) **antes** de enviar material inédito, protegido ou sob consentimento.
- O script `verifica_citacoes.py` localiza trechos em PDF; não substitui a leitura da fonte nem a validação editorial. O estado `entre_paginas` indica localização na junção de duas páginas e **exige conferência visual**: o trecho foi encontrado, mas não está verificado.
- Protocolo inspirado na separação de contextos do Elephant–Goldfish Model, **sem vínculo oficial com seus autores**.

## Como citar

Veja [`CITATION.cff`](CITATION.cff). Formato sugerido:

> Freire, M. (2026). *EGMA — Elefante–Goldfish Acadêmico, v1.1.0*. Laboratório de Humanidades Digitais, Universidade Federal de Ouro Preto. https://github.com/LabHdUfop/egma

## Contribuições

Issue e pull request são bem-vindos — leia [`CONTRIBUTING.md`](CONTRIBUTING.md). Em resumo: mudança no protocolo exige o defeito real que corrige, e nada entra sem evidência de uso.

## Autoria e licença

Protocolo autoral de Marcelo Freire, no Laboratório de Humanidades Digitais da Universidade Federal de Ouro Preto (LABHD UFOP, Mariana/MG).

Distribuído sob licença **MIT** — veja [`LICENSE`](LICENSE). Use, copie, modifique e redistribua livremente, inclusive em uso comercial, mantendo o aviso de copyright.

<https://labhdufop.org> · <https://painel.labhdufop.org>
