# Registros reutilizáveis

Crie somente os registros necessários. Use Markdown/CSV/planilha conforme volume e acesso. Mantenha IDs estáveis, datas, versões e histórico. Cada artefato tem um único registro de estado — versão, pendências e data no mesmo lugar; dois estados divergentes do mesmo artefato são defeito a resolver. Valores desconhecidos ficam `pendente`, `não aplicável` ou `não verificado`, com motivo quando necessário.

Cobertura do percurso (tipologia do audit trail): os registros cobrem o contextual (estado e histórico do projeto), o metodológico (rodadas, manifestos, execução) e o analítico (matriz afirmação–fonte, decisões, correções); a resposta pessoal — reflexividade do pesquisador sobre a própria posição — fica fora do escopo do protocolo e não é substituída por registro (Rodgers; Cowles, 1993, p. 221).

## 1. `ESTADO.md`

Índice mínimo do Elefante, sem dados ou hipóteses protegidas:

```markdown
# Estado do projeto acadêmico
- **MEPA:** 1.3.0
- **Criação do registro:** AAAA-MM-DD
- **Etapa/modo:**
- **Escopo autorizado:**
- **Artefatos e versões:**
- **Decisões do pesquisador:**
- **Pendências/limites:**
- **Revisão:** não iniciada | independente | limitada | assistida; isolamento: comprovado | limitado | não verificado
- **Privacidade:** não avaliada | escopo avaliado em AAAA-MM-DD
- **Descoberta em nova sessão:** não verificada
- **Próxima ação:**
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

Em projeto anterior que já use `CONCEITO.md`, preserve o nome e o histórico; não renomeie silenciosamente. A ficha só abre depois do gate de prontidão e das decisões necessárias.

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

| rodada/papel | versão/hash | arquivos + conteúdo esperado | busca/operações | contexto novo | isolamento (arquivos/memória) | modelo/família/produto sem segredos | destino | limites |
|---|---|---|---|---|---|---|---|

Preserve um parecer original por revisor. Confira `ARQUIVOS LIDOS` contra o manifesto. Não importe automaticamente esses manifestos para outros Peixe-Dourado.

Registre a família do modelo quando conhecida (linhagem/pesos): diversidade de famílias entre elaboração e verificação é critério de força da rodada; papéis da mesma família podem compartilhar erros correlacionados — declare a hipótese no consolidado. Registre também o resultado da sonda de rota por revisor.

## 11. Decisões e resolução

| decisão ID | data | achados/origem | alternativas | estado | evidência/justificativa | responsável | impacto | verificação de resolução |
|---|---|---|---|---|---|---|---|---|

Estados de achado: `CORRIGIR`, `VERIFICAR`, `CONTESTAR`, `ESCALONAR`, `ADIAR`, `REJEITAR`. Resolução: `resolvido`, `parcialmente resolvido`, `não resolvido`, `não verificável`.

## 12. Fechamento

Informe escopo/versão, materiais acessados, mudanças/decisões, operações/verificações, achados resolvidos/pendentes, cobertura com denominadores, identidade/sustentação/cobertura bibliográfica, condição de revisão, correlação entre revisores (quando houver), consultabilidade dos registros, privacidade avaliada e próxima ação. Quando o objeto for o próprio protocolo, instrumento ou método do pesquisador, declare a posição (autoria/proponente) e como ela foi tratada no desenho (rodadas independentes, verificação por execução).

## 13. Ferramenta e escolha de modelo

Registre, por rodada ou etapa de análise, a ferramenta usada e seus limites (preenchido pelo Elefante; o revisor declara no parecer o que souber):

| campo | conteúdo |
|---|---|
| ferramenta/modelo | identificador e versão |
| provedor/rota | produto, conta/plano quando aplicável (privacidade é avaliação separada) |
| parâmetros | configuração relevante (temperatura, limites, ferramentas habilitadas) |
| limites conhecidos | erros documentados, cobertura de idioma, vieses registrados — com fonte; sem fonte, `não verificado` com motivo |
| workarounds | contornos aplicados e por quê |

Quando houver escolha deliberada entre alternativas, registre a razão (adequação linguística, abertura do peso, soberania dos dados, custo) — o protocolo não recomenda modelo, mas exige que a escolha registrada seja reconstruível.

## 14. Trilha de execução e versões (consultabilidade)

| item | conteúdo |
|---|---|
| retido por rodada | objeto congelado, briefings, manifesto, pareceres originais, hashes e logs de execução |
| não retido | raciocínio interno da elaboração, conversa, memória do Elefante e material não autorizado |
| consultabilidade | por artefato: `interna`, `consultável sob pedido` ou `publicável` (exige avaliação de privacidade concluída) — declarada no fechamento |

Registrado não é publicável: a consultabilidade de cada artefato é decisão do projeto, com privacidade avaliada (`privacidade.md`) antes de qualquer publicação. A trilha registra execução e versões; o raciocínio interno da elaboração não integra o pacote.

## 15. Exemplo sintético de achado

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
