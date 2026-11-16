# Glossário de termos e estados

Termos do protocolo, em uma linha cada. Onde há definição completa, o arquivo indicado prevalece.

## Papéis e contextos

| Termo | Definição |
|---|---|
| **Elefante** | O agente que mantém a continuidade do projeto e produz o material; o contexto de elaboração. |
| **Goldfish** | Revisor em contexto separado, sem histórico de elaboração; revisão do próprio Elefante não é independente. |
| **Contexto novo** | Execução de revisão sem histórico de elaboração, resposta desejada ou pareceres alheios; estados: `comprovado`, `limitado`, `não verificado` (`revisao.md` §1). |
| **Isolamento de arquivos/memória** | Controle real do que o revisor acessa; mesma escala do contexto novo. |
| **Família de modelo** | Linhagem/pesos do modelo — dois provedores servindo os mesmos pesos são a mesma família. Papéis da mesma família **podem** compartilhar erros correlacionados (hipótese a declarar, não medida); diversidade de famílias entre elaboração e verificação é critério de força da rodada. |
| **Revisão assistida** | Preparação e verificação sem contexto novo verificável; não se denomina Goldfish concluída e deixa `revisão independente pendente`. |
| **Sonda de rota** | Verificação prévia da rota do revisor (identificação + leitura de arquivo sintético com linha devolvida sem variação), feita pelo Elefante antes de rodada longa; resultado por revisor no manifesto. |
| **Rodada** | Revisores e papéis sobre uma versão congelada; profundidades compacta e completa; tipos completa ou focal. |
| **Parecer** | Produto do revisor no esquema do seu papel; o achado é sua unidade. |
| **Objeto congelado** | Versão imutável examinada, com hash quando disponível; metadados de trabalho ficam fora. |
| **Manifesto da rodada** | Registro por revisor: papel, versão, arquivos, contexto, modelo/família, destino (`registros.md` §10). |

## Achados e estados

| Termo | Definição |
|---|---|
| **Achado** | Problema apontado por um revisor, com localização, evidência e encaminhamento. |
| **Encaminhamento** | `CORRIGIR`, `VERIFICAR`, `CONTESTAR`, `ESCALONAR`, `ADIAR` ou `REJEITAR` (`SKILL.md` §7). |
| **Resolução** | `resolvido`, `parcialmente resolvido`, `não resolvido` ou `não verificável`. |
| **Consolidação** | Agregação dos pareceres por decisão, preservando objeções minoritárias; não decide por votação. |
| **Bloco de correções** | Registro permanente de cada correção: valor anterior, valor novo, origem e impacto (`registros.md` §9). |
| **Verificação por execução** | Reexecutar a operação (contas, filtros, citações, código) em vez de aceitar a alegação. |

## Projeto e registros

| Termo | Definição |
|---|---|
| **Portões G0–G4** | Etapas com aprovação explícita: G0 pitch (`CONCEITO.md`), G1 enquadramento (`FICHA.md`), G2 protocolo (`ANCORAS.md`), G3 piloto, G4 manuscrito/fechamento (`SKILL.md` §5). |
| **Ficha mínima** | Resumo factual entregue ao revisor: pergunta, abordagem, etapa e restrições. |
| **FICHA.md** | Identificação do projeto: problema, pergunta, universo, fontes, análise, ética e pendências. |
| **Âncora / slot** | Linha de `ANCORAS.md` por escolha ou procedimento; slot `fechada`, `pendente` ou `inédita a confirmar`; resolvido como `ancorada`, `análoga` ou `inédita`. |
| **Matriz afirmação–fonte** | Uma linha por afirmação: o que a fonte sustenta e o que não sustenta (`registros.md` §8). |
| **DRIFT** | Diagnóstico de divergência entre estado, plano, texto, referências e rotas reais (`manutencao.md`). |
| **BOOTSTRAP** | Reconstrução de estado para projeto anterior à EGMA, sem retroagir nem inventar. |
| **Artifact-first** | Entregável longo vai para arquivo; no chat, caminho e pontos decisivos. |
| **Registro de estado** | Único por artefato: versão, pendências e data no mesmo lugar. |
| **Trilha de execução e versões** | O que o protocolo retém por rodada: objeto, briefings, manifesto, pareceres, hashes e logs; não inclui o raciocínio interno da elaboração (`registros.md` §14). |
| **Consultabilidade** | Por artefato: `interna`, `consultável sob pedido` ou `publicável` (exige avaliação de privacidade concluída); declarada no fechamento (`registros.md` §14). |
| **Tipologia do percurso** | Cobertura do *audit trail*: contextual, metodológica e analítica; a resposta pessoal (reflexividade) fica fora do escopo (`registros.md`, intro). |

## Bibliografia, medidas e privacidade

| Termo | Definição |
|---|---|
| **Identidade bibliográfica** | A obra existe e está corretamente identificada: `confirmada`, `divergente`, `ambígua`, `não localizada` ou `não verificada`. |
| **Sustentação** | O conteúdo consultado sustenta a afirmação: `sustentada`, `parcialmente sustentada`, `incompatível` ou `não verificável com acesso disponível`. |
| **Cobertura** | A seleção cobre fundamentos, contrapontos e atualizações pertinentes. |
| **Acesso** | Profundidade do consultado: `integral`, `capítulo/seção`, `resumo`, `metadados` ou `sem acesso`. |
| **Instrumento** | Classificação da medida computacional: `medida direta`, `triagem` ou `descarte`. |
| **Validação humana cega** | Codificação humana sem rótulo de hipótese, com concordância por dimensão quando exigida (`validacao-humana-cega.md`). |
| **Estados de privacidade** | Adequação da rota ao material: `compatível — escopo evidenciado`, `condicionado`, `incompatível` ou `não verificável` (`privacidade.md` §4). |

Definições completas: arquivos de `references/` indicados em cada linha.
