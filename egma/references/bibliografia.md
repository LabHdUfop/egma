# Busca e auditoria bibliográfica

Nenhuma referência pode ser criada de memória. A profundidade de verificação acompanha o uso: identidade, sustentação e cobertura são tarefas distintas.

## 1. Planejar e registrar a busca

Defina conceitos, sinônimos, variantes históricas, grafias, nomes verificados, idiomas, período e tipos documentais. Conforme o objeto, inclua artigos, livros, capítulos, teses, relatórios, normas, documentos e dados primários.

Use fontes complementares efetivamente acessíveis: bases especializadas/multidisciplinares, catálogos de bibliotecas/editoras, repositórios, periódicos e associações. Busca geral ajuda descoberta; registros editoriais/institucionais e textos consultados sustentam verificação. Não alegue acesso a base fechada nem consulta não realizada.

Cada busca registra fonte, consulta exata, filtros, idiomas, data, total informado, páginas/registros examinados, critérios, exclusões e limites. Total anunciado não é total triado. Deduplique preservando edições, traduções, preprints e versões publicadas. Rastreie referências e citações posteriores quando disponível e registre a origem do candidato.

## 2. Cobertura, centralidade e atualização

Para cada candidata, registre contribuição potencial, relação com a pergunta, tradição, contexto, data, tipo, acesso e função: fundamento, síntese, evidência, método, atualização ou contraponto.

Avalie centralidade por recorrência em revisões, uso conceitual e debates, além de indicadores disponíveis. Métricas exigem base, data e contextualização por área, idade, idioma e tipo documental. Não some valores incomparáveis nem invente percentis.

Defina janela recente pelo ritmo do tema, sem substituir fundamentos por recência. Busque críticas atuais aos fundamentos e trabalhos em outros idiomas/contextos quando pertinentes. Mapeie conceito/debate × fundamento, evidência, método, contraponto e atualização; explique vazios sem preenchimento decorativo.

Encerre após o protocolo de busca planejado ou limite documentado de tempo/acesso. Não chame de sistemática, exaustiva ou completa sem desenho e execução compatíveis. No fechamento, atualize e registre data e intervalo coberto.

## 3. Identidade bibliográfica

Confira autoria, título, ano, veículo/editora, volume/número, páginas ou identificador, DOI/ISBN/URL, edição e tradução conforme o tipo. Priorize registro editorial, periódico, catálogo confiável ou repositório institucional.

Abra identificadores quando possível e compare a obra retornada. Não complete DOI, volume ou páginas por padrão. Ausência de DOI não invalida referência. Diferencie publicação online/edição, homônimos, duplicatas e versões.

Procure correções, retratações e atualizações quando pertinente e registre implicação. Uma única busca não prova ausência. Para item não localizado, tente variantes e outra fonte apropriada, preservando tentativas.

Estados: `confirmada`, `divergente`, `ambígua`, `não localizada`, `não verificada`. Preserve metadados originais e corrigidos.

## 4. Sustentação das afirmações

Extraia afirmações com citação e afirmações centrais sem fonte. Vincule cada afirmação à parte da obra efetivamente consultada. Registre acesso:

- `integral`;
- `capítulo/seção`;
- `resumo`;
- `metadados`;
- `sem acesso`.

Disponibilidade não é força de evidência. Quem leu só metadados não pode afirmar o argumento; resumo só sustenta o que está presente nele e não confirma página, mecanismo ou argumento do texto completo.

### Citações diretas

Confira palavras, omissões, inserções, tradução e localização na edição consultada. Diferencie página impressa, página do PDF e localizador digital. Nunca invente página. Marque tradução própria e confronte com o original quando possível. Respeite limites autorais na reprodução.

### Paráfrases e inferências

Avalie contexto, população, período, direção, ressalvas, incerteza e tipo de inferência. Não converta associação em causalidade nem obra isolada em consenso. Separe afirmação da fonte e inferência do autor. Identifique citação secundária e não a apresente como consulta ao original.

Estados: `sustentada`, `parcialmente sustentada`, `incompatível`, `não verificável com acesso disponível`. Registre limite/correção por item.

## 5. Cobertura da auditoria

Em auditoria completa, confira todos os registros, todas as citações diretas, todas as afirmações centrais e idealmente cada vínculo afirmação–fonte. Se houver amostragem por tempo/acesso, declare critério, universo, quantidade conferida, exclusões e pendências; não apresente amostra como conferência integral.

Faça reconciliação nos dois sentidos:

- texto → referências: toda citação tem registro;
- referências → texto: todo item foi citado ou pertence a bibliografia consultada explicitamente separada.

Só depois aplique a norma de formatação solicitada, verificando regras atuais se necessário. Correção de estilo não corrige identidade ou sustentação.

## 6. Inclusões e lacuna

Para cada obra sugerida, explique evidência, debate ou atualização acrescentada e onde entra no argumento. Candidata não verificada permanece fora da bibliografia final. Não cite para decorar nem para simular cobertura.

Leia os vizinhos mais próximos antes de alegar novidade. Busca encontra candidatos; leitura estabelece se já fizeram a análise. Escreva lacuna delimitada ao objeto, busca, idiomas, período e acesso. Se a leitura deslocar a contribuição, registre a mudança como resultado.

## 7. Verificação literal por script

`scripts/verifica_citacoes.py` procura trechos normalizados dentro de páginas de PDFs e devolve correspondências e páginas do arquivo. Recebe JSON de citações e, opcionalmente, offsets declarados. `ok=True` exige correspondência única; múltiplas ocorrências ficam `estado=ambigua`, sem escolha automática de página, e mantêm o código de saída de pendência.

Limites:

- correspondência textual não valida contexto, tradução, autoria ou interpretação;
- OCR e extração ruins podem produzir falsos negativos;
- normalização pode produzir falsos positivos em trecho curto; use trecho suficiente e confira visualmente;
- página impressa só é confiável quando confirmada por cabeçalho/rodapé ou offset conferido contra evidência independente;
- correspondência em mais de um lugar é ambiguidade a resolver;
- falha exige corrigir citação/extração, nunca ajustar página até passar.

Tabelas com células mescladas devem ser conferidas visualmente; não reconstrua sua estrutura apenas do texto extraído.
