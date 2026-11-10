# Changelog

Todo registro segue [SemVer](https://semver.org/lang/pt-BR/): **patch** = correção sem mudar comportamento; **minor** = regra ou recurso novo retrocompatível; **major** = mudança que invalida estado ou checklist anterior.

## [1.1.0] — 2026-11-10

Corrige os defeitos de verificação de citações identificados na avaliação da proposta
v1.1 e restaura a paráfrase do leitor ingênuo. Nenhuma regra de revisão, privacidade ou
portabilidade mudou de comportamento; a mudança é no verificador e na rubrica.

**Adicionado**

- `scripts/verifica_citacoes.py`: indexação por **caminho relativo** à base, em vez de
  nome de arquivo, com resolução de homônimos e rejeição de seleção por ordem de varredura.
- Novos estados de saída: `entre_paginas` (localizado na junção de páginas adjacentes, com
  `ok=False` e conferência visual pendente), `arquivo_ausente` (fonte declarada inexistente,
  distinta de texto ausente) e `arquivo_ambiguo` (nome repetido sem caminho).
- Contagem por **ocorrência**, não por par (arquivo, página): repetição dentro da mesma
  página deixa de ser reportada como localização única.
- `caminho` e `sha256` do arquivo usado em todo registro, para identificar qual exemplar
  foi verificado.
- `pagina_impressa_origem`: `observado`, `offset_declarado` ou `indeterminado`.
- Junção entre páginas com desconto de cabeçalho, rodapé e número de folha, e tratamento
  de hifenização.
- Import compatível com `pymupdf` e `fitz`.
- Rubrica do leitor ingênuo: as duas paráfrases obrigatórias (o que o estudo pergunta e
  defende; como o método produz a resposta) antes dos achados.
- `tests/test_verifica_citacoes.py`: suíte de aceitação com 11 casos sintéticos e assertivas
  de estado.

**Corrigido**

- Falso negativo em citação que atravessa páginas (`nao_encontrado` onde o texto existia).
- Fonte tornada inacessível por colisão de nomes de arquivo em pastas diferentes.
- Caminho relativo declarado em `quotes.json` não era resolvido.
- Fonte ausente e texto ausente terminavam no mesmo estado.
- Ausência de marcador de origem para a folha impressa observada.

**Não aplicado**

- Expansão da `description` da skill: sem necessidade demonstrada e com custo de roteamento
  em todas as sessões. Fica condicionada a um teste que demonstre falha de descoberta.

## [1.0.0] — 2026-11-10

Primeira edição pública. Consolida o protocolo portátil anterior e os acréscimos da skill em uso no LABHD UFOP.

**Adicionado**

- Núcleo operacional único (`egma/SKILL.md`) com princípios obrigatórios, seleção de modo e etapas.
- Separação Elefante (continuidade) / Goldfish (revisão em contexto isolado), com papéis fixos de revisão em `egma/references/papeis/`.
- Referências de privacidade, projeto, revisão, bibliografia, medidas computacionais, validação humana cega, registros, manutenção e portabilidade.
- Rubricas bibliográficas separadas para **identidade**, **sustentação** e **cobertura**.
- Papel **leitor ingênuo**; rotinas **DRIFT**, **BOOTSTRAP**, **artifact-first**, **contestação** e **lastro contínuo**.
- Tratamento de **corpus cedido** e de **medidas computacionais** justificadas e testadas.
- `EGMA_PORTATIL.md`: versão monolítica para ambientes sem instalação de pastas.
- `scripts/verifica_citacoes.py`: conferência auxiliar de citações literais em PDF (requer Python e PyMuPDF).
- `SHA256SUMS.txt` para verificação de integridade do pacote.

**Alterado**

- A escolha de rota deixa de ser prescritiva e passa a ser uma **avaliação** aplicável ao produto, conta, plano, configuração e cadeia de ferramentas realmente usados — inclusive em assinaturas.

**Removido**

- Comandos, caminhos pessoais, ferramentas específicas e telemetria de um único harness.
- Recomendações de modelos/provedores e qualquer roteamento de inferência.

**Notas de uso**

- A EGMA não é um modelo, não garante validade científica ou privacidade e não certifica revisão independente.
- A política de dados precisa ser verificada no ambiente real, antes de transmitir material protegido.
