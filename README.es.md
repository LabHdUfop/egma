# MEPA — Modelo Elefante–Pez Dorado Académico

**Protocolo abierto, neutro respecto de agente, modelo y proveedor, para encuadrar, planificar y auditar investigación académica con apoyo de IA.**

Versión 1.3.0 · Licencia MIT · LABHD UFOP

**Idiomas:** [Português](README.md) · [English](README.en.md) · **Español**

> **Resumen.** MEPA es un protocolo autoral para encuadrar, planificar y auditar investigación académica con agentes de IA. Divide el trabajo en un contexto de continuidad (Elefante, que sostiene la pregunta, las decisiones, los artefactos y el estado) y uno o más contextos de revisión aislados (Pez Dorado, que solo ven el rol asignado, el paquete autorizado y los criterios — nunca la conversación de elaboración). Es neutro respecto de harness, modelo y proveedor, y no certifica validez científica, privacidad ni aprobación editorial.

*Esta es la edición española de la documentación. El paquete canónico del protocolo (`egma/`, `EGMA_PORTATIL.md`) permanece en portugués brasileño; las traducciones son ediciones complementarias del mismo protocolo.*

---

## El problema que MEPA ataca

Un agente que elabora un objeto y luego lo revisa en el mismo contexto no produce una revisión independiente: revisa a la luz de su propia conversación, de sus propios atajos y de sus propias justificaciones. MEPA separa esos roles en contextos distintos y exige que cada verificación deje evidencia observable. El resultado es un rastro auditable de *propuesto / ejecutado / verificado / pendiente*.

## Los dos contextos

| Contexto | Rol | Qué ve |
|---|---|---|
| **Elefante** | Continuidad: pregunta, decisiones, artefactos, estado del proyecto | Todo el proyecto, incluso lo que aún no fue aprobado |
| **Pez Dorado** | Revisión en contexto aislado, por rol fijo | Solo el rol, el paquete autorizado y los criterios — nunca la conversación de elaboración ni informes ajenos en la primera ronda |

La revisión hecha por el propio Elefante se registra como **revisión asistida**, no como independiente.

## Instalación

Elija una de las tres formas. Ninguna exige cambiar modelo, proveedor, suscripción, credenciales ni configuración global.

### 1. Skill nativa (recomendada)

Copie la carpeta `egma/` **entera** al mecanismo de skills de su agente, conservando `SKILL.md`, `references/`, `scripts/` y `templates/`. No copie solo el cuerpo de `SKILL.md`: los enlaces son relativos.

### 2. Lectura explícita por proyecto (sin soporte de skills)

Copie `egma/` a `.egm-academico/skill/` en el proyecto, cree `.egm-academico/ESTADO.md` a partir de `egma/templates/ESTADO.md` y agregue un único bloque al archivo de instrucciones que su agente carga efectivamente (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`…). El bloque listo está en [`egma/references/portabilidade.md`](egma/references/portabilidade.md).

### 3. Documento único (chat o API sin sistema de archivos)

Proporcione [`EGMA_PORTATIL.es.md`](EGMA_PORTATIL.es.md) (esta edición; el original canónico en portugués es [`EGMA_PORTATIL.md`](EGMA_PORTATIL.md)) e indique la sección necesaria. Sin búsqueda, ejecución, persistencia ni contextos nuevos, las verificaciones que dependen de esas capacidades deben registrarse como **no disponibles** — no prometerse.

**Siempre:** pruebe en una sesión nueva solo con datos sintéticos. Un archivo presente no comprueba descubrimiento; un contexto nuevo no comprueba aislamiento ni privacidad.

## Modos de operación

| Modo | Cuándo usarlo |
|---|---|
| **Planificación** | Explorar una idea o posibilidades sin elaborar proyecto |
| **Proyecto nuevo** | Elaborar pregunta, literatura, protocolo, piloto, análisis o manuscrito |
| **Objeto existente** | Auditar proyecto, protocolo, análisis o manuscrito existente |
| **Mantenimiento** | Diagnosticar deriva o crear estado para un proyecto anterior a MEPA |
| **Puntual** | Buscar, verificar referencias, recalcular o responder sin ciclo completo |

## Estructura del repositorio

```
egma/
├── SKILL.md                       núcleo operativo: principios, modos, etapas
├── references/
│   ├── privacidade.md             cribado antes de transmitir material protegido
│   ├── projeto.md                 encuadre, corpus, acervo cedido
│   ├── revisao.md                 preparar, ejecutar, verificar y consolidar la revisión Pez Dorado
│   ├── bibliografia.md            búsqueda, identidad y sustento de referencias
│   ├── medidas-computacionais.md  justificar y probar medidas computacionales
│   ├── validacao-humana-cega.md   validación humana ciega de medidas interpretativas
│   ├── registros.md               fichas, anclas, matrices, manifiestos e índices
│   ├── manutencao.md              deriva y reconstrucción de estado
│   ├── fundamentos.md             de dónde viene cada componente (tradición → adaptación)
│   ├── glossario.md               términos y estados del protocolo
│   ├── conformidade.md            registros → exigencias de reporte y declaración
│   ├── portabilidade.md           instalación y verificación
│   └── papeis/                    rúbricas fijas de revisión (método, epistemología,
│                                  argumentación, lector ingenuo, bibliografía)
├── templates/ESTADO.md            índice inicial mínimo del proyecto
├── scripts/verifica_citacoes.py   verificación auxiliar de citas literales en PDF
├── requirements.txt               dependencias del script (Python + PyMuPDF)
└── README.md                      contenido y límites del paquete portátil
EGMA_PORTATIL.md                   versión monolítica para entornos sin carpetas
EGMA_PORTATIL.en.md                edición inglesa del documento único
EGMA_PORTATIL.es.md                edición española del documento único
SHA256SUMS.txt                     hashes de integridad del paquete 1.3.0
tests/                             suite de aceptación del script (11 casos sintéticos)
```

## Verificación de integridad

```bash
sha256sum -c SHA256SUMS.txt      # Linux/macOS/git-bash
```

Los hashes cubren los 25 archivos del paquete 1.3.0. Si alguno falla, el paquete fue alterado — no lo use.

## Pruebas

```bash
python tests/test_verifica_citacoes.py     # requiere Python 3.9+ y PyMuPDF
```

Suite de aceptación de `verifica_citacoes.py`: 11 casos sobre una fixture totalmente sintética (los PDF los genera PyMuPDF; no se usa ningún dato de investigación). Cubre ocurrencia única, repetición en páginas distintas y en la misma página, ausencia de texto, cita entre páginas, PDF homónimos, ruta explícita, fuente ausente, página impresa observada, offset declarado e identidad de la fuente por SHA-256. Los 11 pasan en la 1.3.0 (como en la 1.2.0 y la 1.1.0); en la 1.0.0 solo pasaban 4.

## Límites — leer antes de usar

- MEPA **no es un modelo** y **no garantiza** validez científica, privacidad, ausencia de error ni aprobación editorial.
- MEPA **no certifica** revisión independiente. El aislamiento depende de cómo el entorno opera realmente contexto, memoria y herencia — verifíquelo en su entorno.
- La política de datos es del **producto, cuenta, plan y configuración** que usted use. Consulte [`egma/references/privacidade.md`](egma/references/privacidade.md) **antes** de enviar material inédito, protegido o bajo consentimiento.
- El script `verifica_citacoes.py` localiza pasajes en PDF; no sustituye la lectura de la fuente ni la validación editorial. El estado `entre_paginas` indica ubicación en la unión de dos páginas y **exige verificación visual**: el pasaje fue encontrado, pero no está verificado.
- Protocolo inspirado en la separación de contextos del Elephant–Goldfish Model, **sin vínculo oficial con sus autores**.

## Cómo citar

Vea [`CITATION.cff`](CITATION.cff). Formato sugerido:

> Freire, M. (2026). *MEPA — Modelo Elefante–Pez Dorado Académico, v1.3.0*. Laboratório de Humanidades Digitais, Universidade Federal de Ouro Preto. https://github.com/LabHdUfop/mepa

## Contribuciones

Issues y pull requests son bienvenidos — lea [`CONTRIBUTING.md`](CONTRIBUTING.md) (en portugués). En resumen: un cambio en el protocolo exige el defecto real que corrige, y nada entra sin evidencia de uso.

## Autoría y licencia

Protocolo autoral de Marcelo Freire, en el Laboratorio de Humanidades Digitales de la Universidad Federal de Ouro Preto (LABHD UFOP, Mariana/MG, Brasil).

Distribuido bajo licencia **MIT** — vea [`LICENSE`](LICENSE). Use, copie, modifique y redistribuya libremente, incluso con uso comercial, manteniendo el aviso de copyright.

<https://labhdufop.org> · <https://painel.labhdufop.org>
