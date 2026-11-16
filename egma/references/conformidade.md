# Conformidade — dos registros às exigências de relato

> **Este arquivo não certifica conformidade.** Ele indica correspondências entre os registros do protocolo e exigências de relato e declaração em vigor; a conferência é do pesquisador, contra a norma aplicável ao seu contexto.

## 1. Aplicabilidade e correspondências

As normas citadas são datadas e têm escopo próprio — a do CNPq é administrativa e vincula o fomento (pesquisa apoiada pelo CNPq); fora desse escopo, use-a como referência. Confira a redação vigente ao usar.

| Artefato do protocolo | Exigência que ajuda a atender |
|---|---|
| Matriz de privacidade (etapa × material × rota × retenção) | Declaração de uso de IA generativa — ferramenta e finalidade (CNPq, 2026, p. 5); sigilo de material de avaliação (p. 4) |
| Manifestos de rodada (modelo/família, contexto, destino) | Itens de contexto e sessão das extensões de relato qualitativo com LLM (COREQ+LLM; Sarvestan et al., 2025; Fehring et al., 2026) |
| Registros de execução, bloco de correções, versões e hashes | Trilha do agente — uso de ferramentas e passos intermediários (Wei et al., 2025, p. 9); o protocolo não retém o raciocínio interno da elaboração |
| Fechamento com denominadores | Relato quantificado do processo (revisores, achados, resolução) |
| Registro da ferramenta e da escolha do modelo (`registros.md` §13) | Justificativa do uso de IA e dos limites conhecidos |
| Decisão sobre consultabilidade dos registros | Dados e registros como produtos citáveis (CNPq, 2026, p. 5) |

## 2. Declaração de uso de IA generativa (modelo)

```text
Declaração de uso de inteligência artificial generativa
- Ferramenta(s), versão(ões) e provedor(es): <...>
- Finalidade e fases: <...>
- Material transmitido e rota: <remissão à matriz de privacidade>
- Mediação humana: <onde e como o pesquisador decidiu>
- Registros disponíveis: <onde estão>
```

## 3. Regras duras

- **Material de terceiros em avaliação**: a Portaria CNPq nº 2.664/2026 (art. 9º, I, «e») veda «a inserção de projetos de pesquisa de terceiros em ferramentas de IAG para elaboração de pareceres científicos»; para pareceristas, resguardar o sigilo das informações e dos pareceres a que tiverem acesso (p. 4). Trate o material como classe própria na triagem, antes de qualquer transmissão.
- **Privacidade, confidencialidade e propriedade intelectual** dos insumos e resultados: aplicar `privacidade.md` antes de transmitir. O texto para discussão da CAPES (Brasil, A., 2025, pp. 10-11) recomenda preservá-las — é registro do debate, não norma.
- **Instrumentos** — registre `conferida em <data>` ao usar; norma alterada abre linha no bloco de correções e reavaliação:
  - **CNPq** — *Portaria nº 2.664, de 6 de março de 2026* (Política de Integridade na Atividade Científica): declaração de uso de IAG; vedação de pareceres de terceiros; dados e registros como produtos citáveis.
  - **CAPES** — *A inteligência artificial na pesquisa e no fomento: desafios e oportunidades* (Texto para Discussão, 2025; opiniões do autor).
  - **ANPD** — *A LGPD e o tratamento de dados pessoais para fins acadêmicos e para a realização de estudos por órgão de pesquisa* (Texto para Discussão nº 1/2022; caráter preliminar).
  - **UNESCO** — *Guidance for Generative AI in Education and Research* (2023).
