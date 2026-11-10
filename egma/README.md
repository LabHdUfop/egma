# EGMA portátil 1.1.0

Skill neutra quanto a harness, modelo e provedor para enquadrar, planejar e auditar pesquisa acadêmica com memória do Elefante e revisão Goldfish em contextos separados.

Apresentação, instalação passo a passo e licença: [`../README.md`](../README.md).

## Conteúdo

- `SKILL.md`: núcleo operacional e seleção de modo/etapa.
- `references/`: privacidade, projeto, revisão, bibliografia, medidas, validação, registros, manutenção e portabilidade.
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

- Consolida o protocolo portátil anterior e os acréscimos da skill atual: leitor ingênuo, DRIFT, BOOTSTRAP, artifact-first, contestação, lastro contínuo, medidas computacionais, validação humana e corpus cedido.
- Remove comandos, caminhos pessoais, ferramentas específicas e telemetria de um harness.
- Remove recomendações de modelos/provedores ZDR e qualquer roteamento de inferência.
- Substitui escolha de rota por avaliação aplicável ao produto, conta, plano, configuração e cadeia de ferramentas realmente usados, inclusive em assinaturas.
- Adiciona rubricas bibliográficas separadas para identidade, sustentação e cobertura.

## Limites

A EGMA não é um modelo, não garante validade científica ou privacidade e não certifica revisão independente. A política de dados precisa ser verificada no ambiente real. Consulte `references/privacidade.md` antes de usar material inédito ou protegido.

O script requer Python e PyMuPDF (`requirements.txt`). Sua saída auxilia localização de trechos; não substitui leitura da fonte nem validação editorial.
