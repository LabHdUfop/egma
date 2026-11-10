# Privacidade, não treinamento e retenção

Aplique antes de encaminhar conteúdo acadêmico protegido a qualquer agente, modelo, ferramenta ou serviço. Reavalie quando mudar etapa, material, produto, conta, plano, configuração, endpoint, ferramenta, armazenamento, destino ou política. Esta referência não recomenda fornecedores, modelos ou rotas e não altera contas ou assinaturas.

## 1. Princípio

Adequação depende do **material e da rota real**, não da marca do modelo, do preço, do fato de ser assinatura, de o aplicativo ser local ou de a sessão ser nova. Não transpõe condições de API para aplicativo, de um plano para outro, de um produto para outro ou de uma conta pessoal para institucional.

Para conteúdo intelectual inédito, dados de terceiros, entrevistas, material sob consentimento, dados identificáveis ou informação institucional protegida:

- verifique compromissos aplicáveis de não uso para treinamento e melhoria de modelos;
- verifique retenção, exceções, revisão humana, logs, caches, backups e destinatários;
- respeite consentimento, contrato, ética e autorizações do projeto;
- se isso não puder ser confirmado no escopo necessário, **não transmita o material protegido por essa rota**.

Material público não é automaticamente livre de restrições: uma consulta, interpretação, seleção ou hipótese pode revelar conteúdo inédito.

## 2. Mapear a rota inteira

Inventarie separadamente:

1. interface, harness, histórico, memória automática, telemetria e relatórios de erro;
2. produto, conta, plano, modelo, provedor, endpoint e modalidade;
3. intermediários, gateways, balanceamento e todos os fallbacks;
4. busca, navegação, OCR, transcrição, embeddings, RAG, execução de código e análise de imagem/áudio;
5. memória do Elefante, resumos, bancos vetoriais, arquivos, versões e backups;
6. transporte e destino final dos artefatos e pareceres.

Saídas derivadas — resumo, embedding, figura, tabela ou transcrição — podem conservar conteúdo protegido. Nomes de arquivos e consultas também podem revelá-lo. O modelo principal ter condição adequada não cobre ferramentas auxiliares. Aplicativo local que chama serviço remoto não é processamento inteiramente local; servidor hospedado exige avaliar acessos, snapshots, logs e backups.

## 3. Evidências aceitas e limites

Use documentação primária atual, termos/contratos aplicáveis e configurações observáveis da conta/organização/projeto quando acessíveis. Registre URL ou documento, data, produto, plano, escopo e trecho/síntese. Diferencie:

- declaração comercial;
- compromisso documental ou contratual;
- configuração inspecionada;
- teste técnico local com dados sintéticos.

Uma declaração não prova implementação interna. Um teste de rede demonstra apenas o comportamento observado. A resposta do próprio modelo não é evidência de política. Não peça nem registre segredos.

Examine retenção por segurança/abuso, exceções legais, suporte, revisão humana, histórico, estado da aplicação, anexos, processamento em lote, caches, backups e opções de melhoria do serviço. Registre divergências e duração conhecida. Não afirme ausência absoluta de treinamento ou retenção.

## 4. Estados de decisão

| Estado | Significado | Conduta para material protegido |
|---|---|---|
| `compatível — escopo evidenciado` | Requisitos documentados/configuração observada cobrem material e etapa | Usar somente dentro desse escopo; sem garantia absoluta |
| `condicionado` | Há mudança ou ação necessária ainda não realizada/verificada | Não transmitir até concluir |
| `incompatível` | Há conflito demonstrado com requisito ou autorização | Não usar para esse material |
| `não verificável` | Faltam termos, acesso ou configuração essencial | Não transmitir; seguir com alternativa permitida |

Avalie **não treinamento**, **retenção** e **autorização** em colunas separadas. Desconhecido não é violação comprovada, mas também não é permissão. Ausência de retenção não equivale a não treinamento; não treinamento não elimina retenção.

Se uma rota estiver bloqueada, suspenda apenas a transferência afetada. Continue trabalho legítimo com materiais públicos sem detalhes protegidos, consultas genéricas, exemplos sintéticos ou processamento local previamente autorizado e avaliado. Não apague originais ou backups para “cumprir” a política sem autorização específica.

## 5. Memória e Goldfish

A memória do Elefante é armazenamento intencional, separado da retenção pelo serviço de inferência. Mantenha-a apenas em local autorizado, com minimização, controle de acesso e política de preservação/descarte. Resumos e índices também podem ser confidenciais.

Contexto novo não elimina histórico da conta, memória, logs nem retenção. Antes de cada rodada, confira o destino individual de cada revisor e envie o pacote mínimo necessário. O revisor de privacidade recebe arquitetura e evidências, não o conteúdo protegido que está avaliando.

Pseudonimização não garante anonimização: considere identificadores indiretos, citações localizáveis, voz, rosto, datas e locais. Não declare conformidade legal ou institucional sem avaliação competente.

## 6. Registro mínimo

Use uma matriz etapa × material × componente/destino × produto/conta/plano × não treinamento × retenção/exceções × configuração × evidência/data × estado × ação. Inclua memória, logs, backups, fallbacks e data de reavaliação. Não copie conteúdo protegido nem credenciais para a matriz.

No relatório, declare que a skill apenas avalia e orienta: ela não muda termos, conta, configuração ou retenção. Conteúdo já enviado não recebe proteção retroativa.
