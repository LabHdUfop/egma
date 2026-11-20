# Revisão Peixe-Dourado e consolidação adversarial

Leia antes de preparar ou consolidar qualquer rodada. A revisão examina uma versão congelada; não substitui julgamento do pesquisador nem verificação por execução.

## 1. Escopo e isolamento

Registre modo, versão do objeto, pergunta/abordagem, arquivos autorizados, operações permitidas e critérios. O pacote delimita o que pode ser achado:

- revisão de relatórios é revisão documental;
- auditoria de dados exige dados, dicionário e procedimentos pertinentes;
- auditoria de pipeline exige código, configuração, versões e saídas;
- auditoria bibliográfica exige fontes ou acesso externo autorizado.

Não apresente cobertura maior que o pacote. Se um artefato central não puder ser compartilhado, o Elefante deve verificar por execução quando autorizado ou registrar o ponto como não verificável.

Congele o objeto como o leitor o veria: metadados de trabalho (notas de estado, versões de rascunho, instruções internas) são **excluídos** do objeto — o que sai fica fora do pacote, não dentro dele marcado; quem monta o congelamento confere o resultado e lista no manifesto o que foi excluído.

Cada revisor de primeira rodada recebe contexto separado, sem histórico de elaboração, resposta desejada ou pareceres alheios. Contexto novo deve ser confirmado na medida exposta pelo harness. Isolamento textual sem controle real de arquivos/memória é limitado. Sem isolamento, use revisão assistida.

Estados — duas dimensões, declaradas separadamente e com evidência registrada:

**Contexto novo** (a execução carrega histórico de elaboração?):

| Estado | Evidência registrada |
|---|---|
| `comprovado` | sessão nova, sem histórico de elaboração — registre o produto/harness usado e o que o revisor recebeu |
| `limitado` | histórico não controlado ou não demonstrável (ex.: memória do provedor) — descreva o que não pôde ser excluído |
| `não verificado` | sem confirmação possível |

**Isolamento de arquivos/memória** (o revisor alcança o material de elaboração?):

| Estado | Evidência registrada |
|---|---|
| `comprovado` | separação demonstrada na medida exposta pelo harness — registre a capacidade verificada e o inventário do que ficou acessível |
| `limitado` | acesso parcial (filesystem herdado, arquivos do projeto) ou separação apenas por instrução — descreva o acesso real |
| `não verificado` | sem confirmação possível |

Atribuição: o **revisor** declara no cabeçalho o que observou; o **Elefante** confere e registra o estado final no manifesto, a partir da evidência. Restrição textual — pedir que não leia algo — **não** sustenta `comprovado` em nenhuma das dimensões; sem evidência, o estado é `não verificado`. O estado declarado limita o que a rodada pode alegar: `comprovado` permite apresentar a verificação como cega ao histórico no escopo registrado; `limitado` e `não verificado`, não.

## 2. Papéis da rodada

Na compacta:

1. `references/papeis/epistemologia.md`, incluindo ética/reflexividade na pergunta e contribuição;
2. `references/papeis/metodo.md`, incluindo corpus/amostragem, operacionalização e rastreabilidade;
3. `references/papeis/argumentacao.md`;
4. `references/papeis/leitor-ingenuo.md` para protocolo/manuscrito e sempre que a autossuficiência do documento (self-containment) for relevante.

Na completa de manuscrito, use esses papéis e acrescente as três funções bibliográficas em revisores separados: identidade, sustentação e cobertura. A separação evita que metadados válidos sejam tomados como evidência de sustentação ou cobertura.

Use **um papel por revisor**. Se o harness obrigar agrupamento, declare a revisão como limitada/assistida e descreva quais critérios foram combinados; não alegue independência entre papéis no mesmo contexto. Privacidade da rota é avaliação separada, não papel acadêmico a ser improvisado.

Modelos iguais ou diferentes são escolha operacional do usuário/harness, não garantia metodológica. Diversidade não corrige pacote incompleto. Concordância não transforma alegação em fato. Registre a família de cada modelo no manifesto — família é a linhagem/pesos (dois provedores servindo os mesmos pesos são a mesma família): diversidade de famílias entre elaboração e verificação é critério de força da rodada, e papéis da mesma família **podem** compartilhar erros correlacionados — declare a hipótese no consolidado, sem tratá-la como medida. A ferramenta e seus limites são registrados por rodada (`registros.md` §13); a crítica da ferramenta é parte do método.

## 3. Manifesto e pacote

Para cada revisor, registre:

```text
RODADA: <ID> | PAPEL: <papel> | VERSÃO: <ID/hash quando disponível>
OBJETO: <arquivos/trechos>
ARQUIVOS AUTORIZADOS: <lista exaustiva>
CONTEÚDO ESPERADO: <uma linha por arquivo/trecho>
FONTES EXTERNAS: permitidas/proibidas + escopo
OPERAÇÕES: leitura/busca/código permitidas ou não
CONTEXTO NOVO: comprovado/limitado/não verificado
ISOLAMENTO DE ARQUIVOS/MEMÓRIA: comprovado/limitado/não verificado
SONDA DE ROTA: aprovada/reprovada (data)
MEMÓRIA E HERANÇA: <o que se sabe>
DESTINO DO PARECER: <arquivo ou retorno>
```

Instrução-base:

> Leia somente o pacote indicado e fontes externas expressamente autorizadas. Não procure conversas, memórias ou pareceres alheios. Examine o objeto segundo seu papel e a abordagem declarada. Distinga erro demonstrado, suspeita verificável, informação ausente, divergência epistemológica e oportunidade. Não invente falhas nem elogios. Não altere o objeto; produza apenas o parecer no destino indicado. Declare o que leu, executou e não pôde verificar.

Antes de gastar as revisões longas, sonde cada rota (executada pelo Elefante, com material sintético): identificação, quando aplicável, e leitura real de um arquivo sintético, devolvendo uma linha exata **sem variação** — este é o critério de aceite. O objeto real não entra numa rota ainda não sondada; rota que não lê arquivo não autoriza revisão que dependa de leitura. Registre no manifesto o resultado por revisor (aprovada/reprovada).

EP, MD, ARG e LI seguem os oito campos de seus arquivos de papel. BI, BS e BC usam os esquemas bibliográficos específicos, com o mesmo cabeçalho de contexto/isolamento. Parecer sem achados é válido apenas quando informa o que examinou e confirma leitura dos arquivos necessários. Se `ARQUIVOS LIDOS` omitir arquivo do pacote ou a cobertura esperada ficar ausente, devolva para complementação ou reexecute; não consolide como `SEM ACHADOS`. Elogios genéricos não substituem exame dos limites declarados.

## 4. Verificar antes de endossar

Reexecute os achados decisivos no escopo autorizado:

- denominadores, tamanhos de célula, eventos, perdas e duplicações;
- filtros, joins, normalizações, pesos e transformações;
- comparações entre grandezas ponderadas/não ponderadas;
- famílias de testes, multiplicidade e separação confirmatório/exploratório;
- tabelas/figuras versus texto, código e saídas;
- trechos e páginas de citações;
- procedimentos inseridos depois do plano versus `ANCORAS.md`.

Não trate regras numéricas como universais: relacione estabilidade e inferência ao desenho. Quando houver células pequenas ou medidas frágeis, mostre o efeito da restrição/sensibilidade e classifique o que é reportável com justificativa. Defina famílias confirmatórias antes de olhar resultados sempre que o desenho for confirmatório.

Se a verificação revelar erro no material do Elefante, registre valor antigo, valor novo, data e origem. Se o teste quebrar, declare-o falho e não use sua saída como confirmação.

### Extração e contagem

Antes de agregar pareceres:

1. conte achados por arquivo/papel;
2. compare volume e cabeçalhos com o padrão esperado;
3. investigue zero em parecer substancial;
4. use parser tolerante a formatos ou normalize a saída sem alterar conteúdo;
5. deduplique por ID + localização + problema, preservando origem.

Um extrator vazio é suspeita de falha até inspeção. Não fabrique contagem a partir da aparência do texto: programe ou confira item a item e registre o denominador.

## 5. Medidas interpretativas e residuais

Diferencie:

- medidas de output/forma observável, com regras reproduzíveis e testes de instrumento;
- triagem automatizada, em que um codificador decide;
- medidas interpretativas de conteúdo, que exigem validação compatível antes de sustentar inferência.

Automação não elimina julgamento. Quando concordância for exigida, calcule-a por dimensão, com nível de medida e desenho apropriados; não use limiar universal para todas as tradições. Se a validação estiver pendente, rebaixe a inferência e declare-o.

Publique a classe residual (`outro`, `não classificado`, `indeterminado`) e inspecione uma amostra. Residual elevado pode indicar subdetecção, não raridade. Reclassificação que alterar taxa exige correção registrada, não substituição silenciosa.

## 6. Referências de revisores

Toda obra nomeada por um revisor é candidata até verificação independente. Verifique identidade e conteúdo necessário para o uso; registre `confirmada`, `divergente`, `ambígua`, `não localizada` ou `não verificada`.

`Não localizada` não é sinônimo de inexistente, mas não entra como literatura confirmada. Aceite diagnóstico e referências separadamente. Refaça a busca para localizar vizinhos e contrapontos em vez de apenas ratificar a lista recebida.

## 7. Consolidação e contestação

Analise cada parecer separadamente antes de sintetizar: registre os achados de cada revisor, confronte-os e só então consolide — não leia os pareceres como um texto único (Carter et al., 2014, p. 546).

Agrupe por decisão, preserve objeções minoritárias sustentadas e atribua um estado: `CORRIGIR`, `VERIFICAR`, `CONTESTAR`, `ESCALONAR`, `ADIAR` ou `REJEITAR`.

- `CORRIGIR` significa problema demonstrado e correção autorizada.
- `VERIFICAR` significa evidência/execução adicional antes de aceitar ou rejeitar.
- `CONTESTAR` impugna a existência/validade do problema e exige evidência conferível; “foi intencional” não basta.
- `ESCALONAR` vale para decisões do pesquisador e para informações fora de todo material disponível ao revisor.
- `ADIAR` registra consequência e condição de retomada.
- `REJEITAR` reconhece o problema, mas não aceita o encaminhamento proposto; exige justificativa evidenciada e alternativa quando aplicável.
- O Elefante escreveu o objeto e, por isso, deve apresentar evidência tanto para aceitar quanto para rejeitar um achado.
- Antes de contestar que um artefato não existe, abra todas as versões disponíveis — texto, CSV, planilha e exportação. Versões divergentes devem ser reconciliadas.
- Não escolha por maioria, custo de reescrita ou preferência estética.

O relato da rodada informa os denominadores do processo — revisores e papéis, estados de contexto/isolamento, achados por estado e resolução, correlação entre revisores (famílias repetidas) — e o que não foi verificado.

## 8. Rodada completa ou focal

| Mudança | Rodada |
|---|---|
| Objeto, pergunta, recorte, corpus ou pacote documental | Completa nas partes afetadas |
| Números, medidas ou análise | Completa + verificação por execução |
| Apenas redação/consolidação, com objeto, pacote e conclusões estáveis | Focal |

Rodada focal recebe versão revista, achados e evidências das correções. Classifique resolução como `resolvido`, `parcialmente resolvido`, `não resolvido` ou `não verificável`; não a chame de primeira leitura cega nem a use para alegar busca de novos problemas. Encerre com pendências explícitas, sem exigir unanimidade.
