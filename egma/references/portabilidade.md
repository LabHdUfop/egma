# Portabilidade, instalação e verificação

A EGMA separa quatro coisas: protocolo, harness, modelo e provedor/produto. Trocar uma delas não instala as outras. Não presuma compatibilidade, descoberta automática, isolamento ou mesma política de dados.

## 1. Formas de uso

### Skill nativa

Instale a pasta `egma/` inteira no mecanismo de skills documentado pelo harness de destino, preservando `SKILL.md`, `references/`, `scripts/` e `templates/`. Não copie apenas o corpo: os links são relativos. Consulte a documentação da versão instalada para saber o diretório e o modo de ativação.

### Leitura explícita por projeto

Se não houver suporte a skills, copie `egma/` para `.egm-academico/skill/` no projeto. Crie `.egm-academico/ESTADO.md` a partir de `templates/ESTADO.md` somente se ainda não existir. No arquivo de instruções efetivamente carregado, acrescente um único bloco, sem apagar o restante:

```markdown
<!-- EGMA:START -->
## Elefante–Goldfish Acadêmico
Em tarefas acadêmicas, leia `.egm-academico/skill/SKILL.md` e os recursos
pertinentes, e consulte `.egm-academico/ESTADO.md` se existir. Preserve
artefatos, decisões e pendências. Não execute planos ainda não aprovados.
Antes de transmitir material protegido, aplique a referência de privacidade.
Goldfish recebe apenas papel, pacote e critérios explicitamente fornecidos;
não herda automaticamente índice, conversa, memória ou pareceres do Elefante.
<!-- EGMA:END -->
```

Ajuste os caminhos à localização real do arquivo de instruções. Esse bloco orienta leitura; não é controle de acesso nem comprova carregamento automático de links.

### Documento único

Em chat/API sem arquivos de projeto, forneça `EGMA_PORTATIL.md` e indique a seção necessária. Sem ferramentas de busca, execução, persistência ou novos contextos, registre essas verificações como indisponíveis; não prometa automação.

## 2. Descoberta de instruções

Pontos de partida comuns, conferidos na documentação oficial em 2026-11-09. A versão e a configuração local prevalecem:

| Ambiente | Ponto de partida | Verificação necessária |
|---|---|---|
| Codex | `AGENTS.md`; `AGENTS.override.md` pode prevalecer | Cadeia global/projeto, diretório atual, precedência e limite de leitura |
| Claude Code | `CLAUDE.md`; suporte a `AGENTS.md` e regras/skill conforme configuração | Escopo, memória adicional e o que cada contexto herda |
| OpenCode | `AGENTS.md`; compatibilidade com convenções do Claude Code pode existir | Precedência e se compatibilidade está habilitada |
| Gemini CLI | `GEMINI.md` ou nomes configurados | Hierarquia, nome configurado e contexto realmente carregado |
| Hermes, Antigravity e outros | Mecanismo documentado da versão instalada | Não presumir nomes ou imports de outro produto; usar leitura explícita até verificar |

Documentação: Codex (`https://learn.chatgpt.com/docs/agent-configuration/agents-md`), Claude Code (`https://code.claude.com/docs/en/memory`), OpenCode (`https://opencode.ai/docs/rules/`) e Gemini CLI (`https://geminicli.com/docs/cli/gemini-md/`). Rechecar na instalação.

## 3. Regras de instalação segura

1. Confirme pasta autorizada, sistema, harness/versão e arquivo efetivo; não exiba credenciais.
2. Preserve regras anteriores e configurações globais. Não crie override que esconda instruções existentes.
3. Não sobrescreva protocolo/estado anterior. Compare versões, preserve decisões e resolva conflitos explicitamente.
4. Mantenha um bloco EGMA único e idempotente. Marcadores duplicados ou malformados exigem relatório, não exclusão em massa.
5. Não altere modelo, provedor, assinatura, endpoint, roteamento, credenciais ou serviços para instalar a EGMA.
6. Não use importação automática de toda a pasta de pesquisa em revisores. Restrinja arquivos e memória conforme o papel.
7. Teste apenas com material sintético.

## 4. Aceitação

| Verificação | Evidência mínima | Se indisponível |
|---|---|---|
| Integridade | Todos os links relativos e arquivos existem | Corrigir antes de usar |
| Preservação | Conteúdo fora do bloco permanece intacto | Reverter somente a alteração defeituosa |
| Idempotência | Segunda aplicação não duplica nem zera estado | Corrigir instalação |
| Descoberta | Nova sessão demonstra carregamento/leitura sem novo caminho fornecido | Marcar não verificada; usar leitura explícita |
| Goldfish | Pacote do contexto contém só o autorizado; memória/herança conhecidas | Marcar revisão independente pendente |
| Privacidade | Produto, conta, plano, configuração, ferramentas e destinos avaliados | Não transmitir material protegido |

Um “li” do agente não comprova carregamento ou isolamento. Se o harness não expuser evidência, registre o limite. Não use pesquisa real para testar integração.

## 5. Degradação de capacidades

- Sem delegação isolada: revisão assistida e instruções para sessões separadas operadas pelo pesquisador.
- Sem busca: verificação bibliográfica externa pendente.
- Sem execução: recálculos e testes de pipeline pendentes.
- Sem arquivos: registros na conversa, continuidade persistente não verificada.
- Sem evidência de política de dados: somente materiais públicos/genéricos/sintéticos permitidos.

Registre modelo e produto apenas como metadados de reprodutibilidade, sem segredos. Não converta nome de modelo em alegação de privacidade ou qualidade.
