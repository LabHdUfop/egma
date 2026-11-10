# Contribuindo

Obrigado pelo interesse. A EGMA é um protocolo, não um software convencional: o que se contribui aqui é **regra operacional**, e regra sem lastro é ruído.

## O que esperamos de uma mudança

1. **O defeito que a mudança corrige.** Toda regra nova na EGMA nasceu de um caso real em que a ausência dela produziu erro, retrabalho ou alegação indevida. Descreva o caso — pode ser anonimizado, mas precisa ser real.
2. **Evidência de uso.** Se a regra já foi aplicada, diga onde e com que resultado. Se não foi, marque como **proposta não verificada** no texto; não a apresente como validada.
3. **Neutralidade de harness, modelo e provedor.** Não entram comandos, caminhos pessoais, nomes de produtos como requisito, recomendações de roteamento de inferência ou telemetria de um ambiente específico.
4. **Linguagem e formato.** Português (pt-BR), markdown, arquivos com menos de 300 linhas. Ao atingir o limite, divida em sub-arquivo com link relativo.
5. **Nada de referência inventada.** Toda citação acadêmica precisa de DOI, URL ou metadado verificável. Sem verificação, não entra.

## Como propor

- **Correção pontual** (erro de link, typo, hash): abra um PR direto.
- **Regra nova, modo novo, papel novo**: abra uma **issue** primeiro, com o defeito e a evidência. Discutimos antes do PR.
- **Adaptação para outro agente**: bem-vinda, em `adaptadores/<agente>/`. Preserve a estrutura relativa e documente o que a adaptação assume.

## O que não entra

- Configuração que altere modelo, provedor, credenciais, assinatura ou configuração global do usuário.
- Qualquer coisa que prometa validade científica, privacidade ou aprovação editorial.
- Dados, corpus, entrevistas ou material sob consentimento.
- Automação que publique, submeta, envie e-mail ou contate pessoas sem intervenção humana.

## Versionamento

Seguimos SemVer: **patch** (correção sem mudar comportamento), **minor** (regra ou recurso novo, retrocompatível), **major** (mudança de comportamento que invalida estado ou checklist anterior). Toda release atualiza `CHANGELOG.md` e regera `SHA256SUMS.txt`.

## Licença

Contribuições são aceitas sob a licença MIT do repositório. Ao abrir um PR, você concorda com a distribuição da sua contribuição nos mesmos termos.
