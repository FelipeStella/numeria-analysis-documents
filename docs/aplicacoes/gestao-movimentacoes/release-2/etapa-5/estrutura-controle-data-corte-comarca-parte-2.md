---
title: Controle de data de corte por comarca (TASK-2780) (parte 2)
---

> Release 2 · Etapa 5

## Contexto

Na [parte 1](./TASK-2780-controle-data-corte-comarca.md) foi criada a nova estrutura `ComarcaAtuacao`, centralizando o controle de data de corte por comarca. Esta segunda parte detalha a criação da service responsável por essa estrutura e as telas de front necessárias para sua manutenção (listagem e cadastro).

## Objetivo

Disponibilizar a manutenção completa de `ComarcaAtuacao` — back-end (service) e front-end (listagem com filtro e formulário de cadastro/edição).

## Modificações necessárias

| # | Item                        | Descrição                                   |
|---|-----------------------------|---------------------------------------------|
| 1 | `ComarcaAtuacaoService`     | Criar service com `Get`, `List` e `Update`  |
| 3 | Tela de listagem (front)    | Grid com filtro por comarca                 |
| 4 | Tela de formulário (front)  | Cadastro/edição de uma `ComarcaAtuacao`     |

### 1. `ComarcaAtuacaoService`

| Método                                      | Descrição                                                         |
|---------------------------------------------|-------------------------------------------------------------------|
| `GetByIdAsync(int idComarcaAtuacao)`        | Retorna uma `ComarcaAtuacao` pelo id                              |
| `ListAsync(ComarcaAtuacaoFiltroDto filtro)` | Retorna a listagem paginada, com opções de filtro                 |
| `UpdateAsync(ComarcaAtuacaoDto dto)`        | Atualiza `fgControlaDtCorte` e `dtCorte` de uma comarca existente |

#### DTOs

```json
// ComarcaAtuacaoDto
{
  "idComarcaAtuacao": "number",
  "cdComarca": "string",
  "noComarca": "string",
  "fgControlaDtCorte": "bool",
  "dtCorte": "date"
}
```

```json
// ComarcaAtuacaoFiltroDto
{
  "noComarca": "string",
  "fgControlaDtCorte": "bool | null"
}
```

### 3. Tela de listagem (front)

- **Grid** com colunas: Comarca, Controla data de corte, Data de corte.
- **Filtros:**
  - `noComarca` — busca textual.
  - `fgControlaDtCorte` — sim / não / todos.
- Ação de editar em cada linha, direcionando para a tela de formulário (item 4).

### 4. Tela de formulário (front)

- Campos: Código comarca (input disabled), Nome comarca (input disabled), Controla data de corte (toggle), Data de corte (date picker, habilitado apenas quando "Controla data de corte" estiver marcado).
- Validação: se `fgControlaDtCorte` for `true`, `dtCorte` é obrigatório.

## Estimativa de tempo

| Etapa                                               | Estimativa  |
|-----------------------------------------------------|-------------|
| `ComarcaAtuacaoService` (get, list, update, create) | 1 dia       |
| Tela de listagem com filtro                         | 1 dia       |
| Tela de formulário de cadastro/edição               | 2 dia       |
| **Total**                                           | **3 dias**  |
