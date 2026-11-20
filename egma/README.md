# MEPA portátil 1.3.1

**MEPA (Modelo Elefante–Peixe-Dourado Acadêmico)** é uma skill neutra quanto a harness, modelo e provedor para enquadrar, planejar e auditar pesquisa acadêmica com memória do Elefante e revisão Peixe-Dourado em contextos separados.

Apresentação, instalação passo a passo e licença: [`../README.md`](../README.md).

## Conteúdo

- `SKILL.md`: núcleo operacional e seleção de modo/etapa.
- `references/`: privacidade, projeto, revisão, bibliografia, medidas, validação, registros, manutenção, fundamentos, glossário, conformidade e portabilidade.
- `references/papeis/`: rubricas fixas de revisão.
- `scripts/verifica_citacoes.py`: conferência auxiliar de citações em PDF.
- `templates/ESTADO.md`: índice inicial mínimo.
- `../EGMA_PORTATIL.md`: versão monolítica para ambientes sem instalação de pastas.

## Instalação resumida

1. Preserve a pasta `egma/` inteira e instale pelo mecanismo de skills da versão do harness, se disponível.
2. Alternativamente, copie-a para `.egm-academico/skill/` e siga `references/portabilidade.md` para criar o bloco de leitura no arquivo de instruções efetivo.
3. Não altere configuração global, credenciais, modelo, assinatura ou provedor para instalar.
4. Teste em nova sessão apenas com dados sintéticos. Um arquivo presente não comprova descoberta; um contexto novo não comprova isolamento ou privacidade.

## O que mudou nesta edição

- **1.3.1** — compatibilidade de nome: `MEPA` e `EGMA` designam o mesmo protocolo; o campo de versão do `ESTADO.md` e os marcadores de bloco aceitam as duas formas na leitura e gravam a forma canônica. Sem mudança de regra.
- **1.3.0** — nome do protocolo passa de EGMA para **MEPA (Modelo Elefante–Peixe-Dourado Acadêmico)**, com "Goldfish" traduzido como "Peixe-Dourado" na edição pt-BR; sem mudança de regra e sem caminho novo.
- **1.2.0** — glossário de termos e estados (`references/glossario.md`); fundamentos (de onde vem cada componente) e conformidade (relato e declaração de uso de IA) como referências novas; critérios de decisão dos estados de contexto/isolamento, com evidência mínima; portão da paráfrase (o veredito não fica com o autor); família do modelo no manifesto, com diversidade de famílias como critério de força da rodada; higiene do congelamento; sonda de rota antes de rodadas longas; registro de estado único por artefato; ferramenta e escolha de modelo registradas; análise separada antes da síntese; antipadrões de análise assistida como checklist (catálogo provisório); trilha de execução e consultabilidade (não retém o raciocínio da elaboração); campo de versão dos templates corrigido.
- **Base consolidada** — leitor ingênuo, DRIFT, BOOTSTRAP, artifact-first, contestação, lastro contínuo, medidas computacionais, validação humana e corpus cedido; neutro quanto a harness, modelo e provedor; sem recomendações de modelos/provedores nem roteamento de inferência; rubricas bibliográficas separadas para identidade, sustentação e cobertura.

## O que a MEPA não é

- **Não é automação da pesquisa**: as decisões são do pesquisador; o protocolo organiza, registra e verifica.
- **Não é taxonomia nem método de análise**: disciplina o processo, sem substituir o desenho do estudo.
- **Não é norma de relato**: complementa checklists de relato (ver `references/conformidade.md`), sem os substituir.
- **Não é simulação de revisão por pares**: as rodadas preparam o material para a avaliação real, e não a substituem.

## Limites

A MEPA não é um modelo, não garante validade científica ou privacidade e não certifica revisão independente. A política de dados precisa ser verificada no ambiente real. Consulte `references/privacidade.md` antes de usar material inédito ou protegido.

## Frentes abertas

- **Avaliação sistemática**: desenhos que comparem percursos com e sem os dispositivos do protocolo, medindo o que ele entrega e o que custa.
- **Extensão a outros campos**: a migração para outros domínios é, ela mesma, uma forma de verificação.
- **Matriz de privacidade**: amadurecimento contínuo, acompanhando provedores, normas e retenção.
- **Consultabilidade dos registros**: política de publicação dos registros (`registros.md` §14).

O script requer Python e PyMuPDF (`requirements.txt`). Sua saída auxilia localização de trechos; não substitui leitura da fonte nem validação editorial.
