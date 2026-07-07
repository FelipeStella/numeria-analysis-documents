---
title: Controle de data de corte por comarca (TASK-2780) (parte 1)
---

> Release 2 · Etapa 5

## Contexto

A data de corte é uma informação vinculada ao edital que indica uma data específica na qual o servidor já deveria estar atuando na comarca para poder participar do edital. Exemplo: se a data de corte do edital é 01/01/2020 e o servidor entrou na comarca em 02/01/2020, ele não poderá participar do edital.

Atualmente esse controle existe em dois lugares:

- No **edital**, como a data de corte em si (`DtCorte`);
- Na **vaga do edital**, como uma flag indicando se aquela vaga específica deve ou não respeitar a data de corte do edital.

Vamos centralizar esse controle numa nova estrutura vinculada à **comarca**, contendo a data de corte e se ela deve ou não ser aplicada.

## Objetivo

Implementar um controle centralizado da data de corte por comarca.

## Modificações necessárias

| # | Item                                                                                    | Descrição                                                                             |
|---|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| 1 | `Edital`                                                                                | Remover coluna `DtCorte`; ajustar entidade, DTOs, CRUD e formulário (front)           |
| 2 | `EditalRemocaoVaga`                                                                     | Remover coluna `FgAplicarDtCorte`; ajustar entidade, DTOs, CRUD e formulário (front)  |
| 3 | Nova estrutura `ComarcaAtuacao`                                                         | Criar tabela com os campos abaixo                                                     |
| 4 | `GestaoMovimentacoesService.GetVagasEditalRemocaoAsync`                                 | Adicionar `FgControlaDtCorte` e `DtCorte` em `VagaRemocaoDto`                         |
| 5 | `FormacaoMatchRemocaoSimplesExtensions.ResolveCandidatosGrupo`                          | Filtrar candidatos pela data de corte da vaga, quando existir                         |

### 3. Nova estrutura: `ComarcaAtuacao`

```json
{
  "idComarcaAtuacao": "number",
  "cdComarca": "string",
  "noComarca": "string",
  "fgControlaDtCorte": "bool",
  "dtCorte": "date"
}
```

## Estimativa de tempo

| Etapa                             | Estimativa  |
|-----------------------------------|-------------|
| Remoção dos campos e ajustes      | 1 dia       |
| Fluxo remoção simples e sucessiva | 3 dias      |
| Nova estrutura de dados           | 1 dia       |
| **Total**                         | **5 dias**  |
