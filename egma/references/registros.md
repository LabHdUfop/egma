# Registros reutilizáveis

Crie somente os registros necessários. Use Markdown/CSV/planilha conforme volume e acesso. Mantenha IDs estáveis, datas, versões e histórico. Valores desconhecidos ficam `pendente`, `não aplicável` ou `não verificado`, com motivo quando necessário.

## 1. `ESTADO.md`

Índice mínimo do Elefante, sem dados ou hipóteses protegidas:

```markdown
# Estado do projeto
- EGMA: 1.0.0
- Etapa/modo:
- Escopo autorizado:
- Artefatos e versões:
- Decisões do pesquisador:
- Pendências/limites:
- Revisão: não iniciada | independente | limitada | assistida
- Privacidade: escopo avaliado e data | não verificada
- Próxima ação:
```

Não redefina estado existente. Registre ausência de índice anterior sem inventar retrospecto.

## 2. `CONCEITO.md`

Criado no G0 antes da ficha:

```markdown
# Conceito da pesquisa
- Problema e destinatário:
- Hipótese/pitch em duas ou três frases:
- Dentro do escopo:
- Fora do escopo:
- Restrições inegociáveis:
- Critérios de sucesso:
- Alternativas rejeitadas e motivo de cada uma:
- Resultado das cinco lentes do G0:
- Decisões confirmadas pelo pesquisador:
- Decisões que seguem para a ficha:
```

Em projeto anterior que já use `CONCEPTO.md`, preserve o nome e o histórico; não renomeie silenciosamente. A ficha só abre depois do gate de prontidão e das decisões necessárias.

## 3. `FICHA.md`

Identificação/responsável, versão/data, problema, pergunta, contribuição provisória, tradição/abordagem, conceitos, universo/unidade/seleção, corpus/período/local, fontes/acesso/coleta/tratamento, plano de análise, ética/reflexividade/privacidade, recursos, piloto, limites e pendências.

## 4. `PLANO_DE_ANALISE.md`

| ID | pergunta | conceito | material/unidade | variável/categoria | procedimento/versão | pressupostos | produto | inferência permitida | limites/alternativa |
|---|---|---|---|---|---|---|---|---|---|

Registre também desvios aceitos, data, razão, autorização e impacto. Procedimento não listado abre âncora antes da execução. Se o plano preceder a bibliografia, ligue cada procedimento ao slot correspondente e não faça alegações sobre literatura com slot aberto.

## 5. `ANCORAS.md`

| ID | slot | escolha/procedimento | base teórica | aplicação e objeto | confundidores/limites | acesso | estado | risco/ação |
|---|---|---|---|---|---|---|---|---|

- Slot: `fechada`, `pendente`, `inédita a confirmar`.
- Estado após resolução: `ancorada`, `análoga`, `inédita`.
- Todo slot crítico precisa estar fechado antes da coleta. Unidade e taxonomia são críticas; os demais prazos são declarados no plano.
- O ID da linha deve aparecer no risco correspondente e no método quando aplicável.

## 6. Registro de privacidade

| etapa/material | classe | componente/destino | produto/conta/plano | não treinamento | retenção/exceções | configuração | evidência/data | estado | ação |
|---|---|---|---|---|---|---|---|---|---|

Inclua ferramentas auxiliares, memória, logs, backups e fallbacks. Não inclua segredos ou conteúdo protegido.

## 7. Busca e obras

| busca ID | data | fonte | consulta exata | filtros/idiomas | total informado | registros triados | critérios/exclusões | limites | arquivo |
|---|---|---|---|---|---|---|---|---|---|

| obra ID | referência original | metadados conferidos | identificador | descoberta | fonte/data | identidade | acesso | papel/pertinência | influência contextualizada | correções/atualizações |
|---|---|---|---|---|---|---|---|---|---|---|

## 8. `MATRIZ_AFIRMACAO_FONTE.md`

| afirmação ID/local | texto/escopo | obra/dado ID | uso | edição/localizador | evidência consultada | acesso | o que sustenta | o que não sustenta | estado/correção | data/revisor |
|---|---|---|---|---|---|---|---|---|---|---|

Uma linha por afirmação, não por obra. Vincule observações empíricas aos dados e à execução, não apenas à literatura.

## 9. Execução e correções

| operação ID | data | entrada/versão | procedimento/código | parâmetros | saída/versão | verificação | limites | desvio/razão |
|---|---|---|---|---|---|---|---|---|

Bloco permanente de correções:

| data | local/ID | valor/redação anterior | valor/redação nova | origem da correção | impacto |
|---|---|---|---|---|---|

Não apague a linha anterior nem dissolva correção decisiva em prosa.

## 10. Manifesto da rodada

| rodada/papel | versão/hash | arquivos + conteúdo esperado | busca/operações | contexto/memória | modelo/produto sem segredos | destino | limites |
|---|---|---|---|---|---|---|---|

Preserve um parecer original por revisor. Confira `ARQUIVOS LIDOS` contra o manifesto. Não importe automaticamente esses manifestos para outros Goldfish.

## 11. Decisões e resolução

| decisão ID | data | achados/origem | alternativas | estado | evidência/justificativa | responsável | impacto | verificação de resolução |
|---|---|---|---|---|---|---|---|---|

Estados de achado: `CORRIGIR`, `VERIFICAR`, `CONTESTAR`, `ESCALONAR`, `ADIAR`, `REJEITAR`. Resolução: `resolvido`, `parcialmente resolvido`, `não resolvido`, `não verificável`.

## 12. Fechamento

Informe escopo/versão, materiais acessados, mudanças/decisões, operações/verificações, achados resolvidos/pendentes, cobertura com denominadores, identidade/sustentação/cobertura bibliográfica, condição de revisão, privacidade avaliada e próxima ação.

## 13. Exemplo sintético de achado

```text
ACHADO MD-01 — Escopo da conclusão excede a seleção documentada
Localização: manuscrito.md, objetivo 2 e conclusão, §4
Problema: a conclusão generaliza para todos os usuários, mas o corpus contém apenas comentários selecionados.
Natureza: erro demonstrado
Evidência: FICHA.md lista cinco publicações e nenhum procedimento de amostragem da população.
Consequência: o material sustenta análise dos comentários selecionados, não prevalência entre usuários.
Gravidade: crítica
Certeza: demonstrado
Encaminhamento: delimitar objetivo/conclusões ou planejar nova seleção; decisão do pesquisador.
```

Este exemplo é sintético e não constitui evidência empírica nem recomendação universal de amostragem.
