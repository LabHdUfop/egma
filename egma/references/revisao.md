# Revisão Goldfish e consolidação adversarial

Leia antes de preparar ou consolidar qualquer rodada. A revisão examina uma versão congelada; não substitui julgamento do pesquisador nem verificação por execução.

## 1. Escopo e isolamento

Registre modo, versão do objeto, pergunta/abordagem, arquivos autorizados, operações permitidas e critérios. O pacote delimita o que pode ser achado:

- revisão de relatórios é revisão documental;
- auditoria de dados exige dados, dicionário e procedimentos pertinentes;
- auditoria de pipeline exige código, configuração, versões e saídas;
- auditoria bibliográfica exige fontes ou acesso externo autorizado.

Não apresente cobertura maior que o pacote. Se um artefato central não puder ser compartilhado, o Elefante deve verificar por execução quando autorizado ou registrar o ponto como não verificável.

Cada revisor de primeira rodada recebe contexto separado, sem histórico de elaboração, resposta desejada ou pareceres alheios. Contexto novo deve ser confirmado na medida exposta pelo harness. Isolamento textual sem controle real de arquivos/memória é limitado. Sem isolamento, use revisão assistida.

## 2. Papéis da rodada

Na compacta:

1. `references/papeis/epistemologia.md`, incluindo ética/reflexividade na pergunta e contribuição;
2. `references/papeis/metodo.md`, incluindo corpus/amostragem, operacionalização e rastreabilidade;
3. `references/papeis/argumentacao.md`;
4. `references/papeis/leitor-ingenuo.md` para protocolo/manuscrito e sempre que a autossuficiência do documento (self-containment) for relevante.

Na completa de manuscrito, use esses papéis e acrescente as três funções bibliográficas em revisores separados: identidade, sustentação e cobertura. A separação evita que metadados válidos sejam tomados como evidência de sustentação ou cobertura.

Use **um papel por revisor**. Se o harness obrigar agrupamento, declare a revisão como limitada/assistida e descreva quais critérios foram combinados; não alegue independência entre papéis no mesmo contexto. Privacidade da rota é avaliação separada, não papel acadêmico a ser improvisado.

Modelos iguais ou diferentes são escolha operacional do usuário/harness, não garantia metodológica. Diversidade não corrige pacote incompleto. Concordância não transforma alegação em fato.

## 3. Manifesto e pacote

Para cada revisor, registre:

```text
RODADA: <ID> | PAPEL: <papel> | VERSÃO: <ID/hash quando disponível>
OBJETO: <arquivos/trechos>
ARQUIVOS AUTORIZADOS: <lista exaustiva>
CONTEÚDO ESPERADO: <uma linha por arquivo/trecho>
FONTES EXTERNAS: permitidas/proibidas + escopo
OPERAÇÕES: leitura/busca/código permitidas ou não
CONTEXTO NOVO: confirmado/limitado/não verificado
MEMÓRIA E HERANÇA: <o que se sabe>
DESTINO DO PARECER: <arquivo ou retorno>
```

Instrução-base:

> Leia somente o pacote indicado e fontes externas expressamente autorizadas. Não procure conversas, memórias ou pareceres alheios. Examine o objeto segundo seu papel e a abordagem declarada. Distinga erro demonstrado, suspeita verificável, informação ausente, divergência epistemológica e oportunidade. Não invente falhas nem elogios. Não altere o objeto; produza apenas o parecer no destino indicado. Declare o que leu, executou e não pôde verificar.

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

## 8. Rodada completa ou focal

| Mudança | Rodada |
|---|---|
| Objeto, pergunta, recorte, corpus ou pacote documental | Completa nas partes afetadas |
| Números, medidas ou análise | Completa + verificação por execução |
| Apenas redação/consolidação, com objeto, pacote e conclusões estáveis | Focal |

Rodada focal recebe versão revista, achados e evidências das correções. Classifique resolução como `resolvido`, `parcialmente resolvido`, `não resolvido` ou `não verificável`; não a chame de primeira leitura cega nem a use para alegar busca de novos problemas. Encerre com pendências explícitas, sem exigir unanimidade.
