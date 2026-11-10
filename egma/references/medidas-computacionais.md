# Medidas computacionais e instrumentos

Quando a análise usa parsing, dicionários, classificadores, embeddings, ASR, OCR, detecção de negação, sentimento, entidades ou outra medida emprestada, a justificativa exige três pernas e um teste local.

## 1. Três pernas

| Perna | Pergunta | Registro necessário |
|---|---|---|
| Teoria | Por que a medida significa algo sobre o constructo? | Tradição e passagem que relacionam estrutura/indicador ao conceito |
| Ferramenta | Como foi operacionalizada? | Ferramenta/modelo/dicionário, versão, parâmetros, idioma e referência verificada |
| Confundidores | Por que o resultado não é artefato? | Erros conhecidos, regras de fronteira, testes e tratamento no corpus |

A terceira perna não é limitação decorativa: erros documentados da ferramenta precisam ser procurados no material e impedidos de virar achado. Se faltar uma perna, a inferência fica pendente ou é rebaixada.

## 2. Âncora e adequação ao corpus

Precedente em outro objeto mostra que a medida foi aplicada, não que funciona no corpus atual. Antes de usá-la como evidência:

1. construa amostra de referência anotada manualmente ou por procedimento independente adequado, com seleção documentada;
2. avalie acerto por relação/categoria, não apenas média agregada;
3. teste estabilidade a normalizações triviais, formato, pontuação, maiúsculas e versões quando pertinentes;
4. inspecione erros por subgrupo/contexto e registre viés de cobertura;
5. classifique o instrumento: `medida direta`, `triagem` ou `descarte`, com justificativa ligada à inferência;
6. preserve configuração, entradas, saídas e correções.

Texto de fala, OCR, redes sociais, documentos históricos e prosa editada têm propriedades diferentes. Desempenho publicado em outro corpus não substitui avaliação local. Magnitude implausível é primeiro hipótese de instrumento/extrator quebrado, não achado sobre o fenômeno.

## 3. Regras de operacionalização

- Publique taxonomia e regras de fronteira antes da codificação confirmatória.
- Distinção conceitual importante precisa de categoria observável própria; não some apagamento, impessoalização ou ausência porque a superfície é semelhante.
- Uma mesma marca formal pode exercer funções diferentes; contagem da marca não mede automaticamente a função.
- Verifique âncoras lexicais contra o corpus e contra a classe residual, não contra a intuição.
- Publique distribuição completa, inclusive `outro/não classificado/indeterminado`, e examine amostra residual.
- Se inspeção mostrar que o indicador mede outro constructo, revogue a medida; não reinterprete o número para salvá-lo.

## 4. Medida, triagem e interpretação

| Estado | Uso permitido | O que não fazer |
|---|---|---|
| Medida direta | Sustentar afirmação dentro do desempenho e desenho demonstrados | Generalizar além do corpus/validação |
| Triagem | Levantar candidatos para decisão humana ou inspeção | Tratar saída automática como rótulo final |
| Descarte | Registrar tentativa e razão | Usar resultado porque confirma expectativa |

Medida interpretativa automatizada continua interpretativa. Quando a inferência exigir confiabilidade, aplique `validacao-humana-cega.md` ou outra validação compatível com a tradição. Se pendente, declare que a afirmação principal não pode repousar nela como medida validada.

## 5. Linguística de corpus e medidas de distribuição

Escolha estatística pela pergunta e abordagem. Em linguística de corpus, frequência, associação e dispersão respondem perguntas distintas:

- frequência normalizada e comparação de keyness: diferença de ocorrência considerando tamanho dos corpora;
- medidas de colocação com janela declarada: atração entre itens;
- dispersão por documento/unidade: concentração versus distribuição.

Frequência sem dispersão pode esconder concentração em uma única fonte. Testes de grupos não respondem automaticamente keyness ou colocação. Declare unidade, normalização, janela, tokenização, significância/efeito e sensibilidade quando aplicáveis, sem receita universal.

## 6. Relato mínimo no método

Inclua, em linguagem direta:

1. constructo e razão teórica da medida;
2. ferramenta/modelo/versão e parâmetros;
3. unidade e regras de decisão;
4. confundidores e tratamento;
5. avaliação no corpus, denominadores e resultados;
6. resíduos, erros e dados excluídos;
7. estado do instrumento e inferência permitida;
8. mudanças posteriores ao plano e respectiva âncora.

Não chame de validado apenas porque há precedente publicado, código executável ou concordância entre modelos.
