# Changelog

Todo registro segue [SemVer](https://semver.org/lang/pt-BR/): **patch** = correção sem mudar comportamento; **minor** = regra ou recurso novo retrocompatível; **major** = mudança que invalida estado ou checklist anterior.

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
