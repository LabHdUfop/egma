# MEPA — Elephant–Goldfish Academic

**Open protocol, neutral with respect to agent, model and provider, for framing, planning and auditing academic research with AI support.**

Version 1.3.0 · MIT License · LABHD UFOP

**Languages:** [Português](README.md) · **English** · [Español](README.es.md)

> **Abstract.** MEPA is an authorial protocol for framing, planning and auditing academic research with AI agents. It splits the work into a continuity context (Elephant, which holds the question, decisions, artifacts and state) and one or more isolated review contexts (Goldfish, which see only the assigned role, the authorized package and the criteria — never the elaboration conversation). It is harness-, model- and vendor-neutral, and it does not certify scientific validity, privacy or editorial approval.

*This is the English edition of the documentation. The canonical protocol package (`egma/`, `EGMA_PORTATIL.md`) remains in Brazilian Portuguese; the translations are companion editions of the same protocol.*

---

## The problem MEPA addresses

An agent that elaborates an object and then reviews it in the same context does not produce an independent review: it reviews in the light of its own conversation, its own shortcuts and its own justifications. MEPA separates these roles into distinct contexts and requires every verification to leave observable evidence. The result is an auditable trail of *proposed / executed / verified / pending*.

## The two contexts

| Context | Role | What it sees |
|---|---|---|
| **Elephant** | Continuity: question, decisions, artifacts, project state | The whole project, including what has not yet been approved |
| **Goldfish** | Review in an isolated context, by fixed role | Only the role, the authorized package and the criteria — never the elaboration conversation nor other reviewers' reports in the first round |

A review performed by the Elephant itself is recorded as an **assisted review**, not as independent.

## Installation

Choose one of the three ways. None requires changing model, provider, subscription, credentials or global configuration.

### 1. Native skill (recommended)

Copy the whole `egma/` folder into your agent's skill mechanism, preserving `SKILL.md`, `references/`, `scripts/` and `templates/`. Do not copy only the body of `SKILL.md`: the links are relative.

### 2. Explicit per-project reading (no skill support)

Copy `egma/` to `.egm-academico/skill/` in the project, create `.egm-academico/ESTADO.md` from `egma/templates/ESTADO.md` and add a single block to the instructions file effectively loaded by your agent (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`…). The ready-made block is in [`egma/references/portabilidade.md`](egma/references/portabilidade.md).

### 3. Single document (chat or API without a filesystem)

Provide [`EGMA_PORTATIL.en.md`](EGMA_PORTATIL.en.md) (this edition; the canonical Portuguese original is [`EGMA_PORTATIL.md`](EGMA_PORTATIL.md)) and point to the required section. Without search, execution, persistence or fresh contexts, the verifications that depend on those capabilities must be recorded as **unavailable** — not promised.

**Always:** test in a fresh session with synthetic data only. A file being present does not prove discovery; a fresh context does not prove isolation or privacy.

## Operating modes

| Mode | When to use |
|---|---|
| **Planning** | Explore an idea or possibilities without elaborating a project |
| **New project** | Elaborate question, literature, protocol, pilot, analysis or manuscript |
| **Existing object** | Audit an existing project, protocol, analysis or manuscript |
| **Maintenance** | Diagnose drift or create state for a project predating MEPA |
| **One-off** | Search, check references, recompute or answer without a full cycle |

## Repository structure

```
egma/
├── SKILL.md                       operational core: principles, modes, stages
├── references/
│   ├── privacidade.md             screening before transmitting protected material
│   ├── projeto.md                 framing, corpus, contributed collection
│   ├── revisao.md                 prepare, run, verify and consolidate Goldfish review
│   ├── bibliografia.md            search, identity and support of references
│   ├── medidas-computacionais.md  justify and test computational measures
│   ├── validacao-humana-cega.md   blind human validation of interpretive measures
│   ├── registros.md               records, anchors, matrices, manifests and indexes
│   ├── manutencao.md              drift and state reconstruction
│   ├── fundamentos.md             where each component comes from (tradition → adaptation)
│   ├── glossario.md               protocol terms and states
│   ├── conformidade.md            records → reporting and declaration requirements
│   ├── portabilidade.md           installation and verification
│   └── papeis/                    fixed review rubrics (method, epistemology,
│                                  argumentation, naïve reader, bibliography)
├── templates/ESTADO.md            minimal initial project index
├── scripts/verifica_citacoes.py   auxiliary check of verbatim quotations in PDFs
├── requirements.txt               script dependencies (Python + PyMuPDF)
└── README.md                      contents and limits of the portable package
EGMA_PORTATIL.md                   monolithic version for environments without folders
EGMA_PORTATIL.en.md                English edition of the single document
EGMA_PORTATIL.es.md                Spanish edition of the single document
SHA256SUMS.txt                     integrity hashes of package 1.3.0
tests/                             script acceptance suite (11 synthetic cases)
```

## Integrity verification

```bash
sha256sum -c SHA256SUMS.txt      # Linux/macOS/git-bash
```

The hashes cover the 25 files of package 1.3.0. If any fails, the package was altered — do not use it.

## Tests

```bash
python tests/test_verifica_citacoes.py     # requires Python 3.9+ and PyMuPDF
```

Acceptance suite for `verifica_citacoes.py`: 11 cases over an entirely synthetic fixture (the PDFs are generated by PyMuPDF; no research data is used). It covers single occurrence, repetition on different pages and on the same page, absence of text, quotation spanning pages, same-named PDFs, explicit path, missing source, observed printed page, declared offset and source identity by SHA-256. All 11 pass on 1.3.0 (as on 1.2.0 and 1.1.0); on 1.0.0 only 4 passed.

## Limits — read before use

- MEPA **is not a model** and **does not guarantee** scientific validity, privacy, absence of error or editorial approval.
- MEPA **does not certify** independent review. Isolation depends on how the environment actually handles context, memory and inheritance — verify it in your environment.
- The data policy belongs to the **product, account, plan and configuration** you use. Consult [`egma/references/privacidade.md`](egma/references/privacidade.md) **before** sending unpublished, protected or consented material.
- The `verifica_citacoes.py` script locates passages in PDFs; it does not replace reading the source or editorial validation. The `entre_paginas` state indicates location at the junction of two pages and **requires a visual check**: the passage was found, but it is not verified.
- Protocol inspired by the context separation of the Elephant–Goldfish Model, **without official affiliation with its authors**.

## How to cite

See [`CITATION.cff`](CITATION.cff). Suggested format:

> Freire, M. (2026). *MEPA — Elephant–Goldfish Academic Model, v1.3.0*. Laboratório de Humanidades Digitais, Universidade Federal de Ouro Preto. https://github.com/LabHdUfop/mepa

## Contributions

Issues and pull requests are welcome — read [`CONTRIBUTING.md`](CONTRIBUTING.md) (in Portuguese). In short: a change to the protocol requires the real defect it fixes, and nothing enters without evidence of use.

## Authorship and license

An authorial protocol by Marcelo Freire, at the Digital Humanities Laboratory of the Federal University of Ouro Preto (LABHD UFOP, Mariana/MG, Brazil).

Distributed under the **MIT** license — see [`LICENSE`](LICENSE). Use, copy, modify and redistribute freely, including for commercial use, keeping the copyright notice.

<https://labhdufop.org> · <https://painel.labhdufop.org>
