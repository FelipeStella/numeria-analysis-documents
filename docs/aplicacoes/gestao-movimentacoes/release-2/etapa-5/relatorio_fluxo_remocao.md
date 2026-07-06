---
title: Relatório do fluxo de remoção (TASK-2777)
---

> Release 2 · Etapa 5

## Contexto

Relatório detalhado do fluxo de remoção, contendo a seguinte estrutura de dados:

**`ParticipanteRemocao`** (usada tanto pelo vencedor quanto pelos candidatos)

```json
{
  "nrFuncional": "string",
  "nrVinculo": "number",
  "exercicio": {
    "dtExercicio": "date",
    "nrDias": "number"
  },
  "sedeAtual": {
    "dtInicio": "date",
    "nrDias": "number"
  },
  "antiguidadePj": {
    "dtInicio": "date",
    "nrDias": "number"
  },
  "nascimento": {
    "dtNascimento": "date",
    "nrDias": "number"
  },
  "nrAvaliacao": "number",
  "noComarcaOrigem": "string",
  "noComarcaInteresse1": "string",
  "noComarcaInteresse2": "string",
  "noComarcaInteresse3": "string",
  "noComarcaSelecionada": "string"
}
```

**`VagaPreenchida`**

```json
{
  "cdComarca": "string",
  "noComarca": "string",
  "nrVaga": "string",
  "vencedor": "ParticipanteRemocao",
  "candidatos": [
    {
      "...": "ParticipanteRemocao",
      "dsMotivoDesempate": "string"
    }
  ]
}
```

> `candidatos[]` estende `ParticipanteRemocao` adicionando `dsMotivoDesempate`, preenchido quando há critério de desempate aplicado entre candidatos.

**`FluxoVagaRemocaoEdital`**

```json
{
  "vagaOriginal": "VagaPreenchida",
  "vagasSucessivas": "VagaPreenchida[]"
}
```

## Objetivo

Agilizar o processo de validação do fluxo de remoção.

## Modificações necessárias

| # | Item                                                                              | Descrição                                             |
|---|-----------------------------------------------------------------------------------|-------------------------------------------------------|
| 1 | Nova estrutura `FluxoRemocaoHistorico`                                            | Criar tabela com os campos abaixo                     |
| 2 | `MatchRemocaoSucessiva`                                                           | Adicionar coluna `IdRemocaoVaga`                      |
| 3 | `FormacaoMatchRemocaoSimplesExtensions.ResolveCandidatosGrupo`                    | Vincular `IdRemocaoVaga` ao candidato vencedor        |
| 4 | `FormacaoMatchRemocaoSucessivaExtensions.MapearVagasRestantesRemocaoSucessiva`    | Vincular `IdRemocaoVaga` à nova vaga                  |
| 5 | `MatchService.CriarMatchRemocaoSucessivaAsync`                                    | Registrar `IdRemocaoVaga` em `MatchRemocaoSucessiva`  |
| 6 | `FormacaoMatchGestaoMovimentacaoService.ProcessarResultadosRemocaoSimplesAsync`   | Salvar histórico do fluxo de remoção                  |
| 7 | `FormacaoMatchGestaoMovimentacaoService.ProcessarResultadosRemocaoSucessivaAsync` | Salvar histórico do fluxo de remoção                  |
| 8 | Relatório de fluxo de remoção por edital                                          | Novo relatório em PDF (ver detalhes abaixo)           |

### 1. Nova estrutura: `FluxoRemocaoHistorico`

```json
{
  "idFluxoRemocaoHistorico": "number",
  "idMatchRemocaoSucessiva": "number",
  "dtExercicio": "date",
  "dtExercicioSedeAtual": "date",
  "nrTempoServicoPj": "number",
  "dtNascimento": "date",
  "nrNotaAvaliacao": "number"
}
```

### 8. Relatório de fluxo de remoção por edital

- **Filtro:** `NrEdital`
- **Formato de saída:** PDF

## Estimativa de tempo

| Etapa                               | Estimativa  |
|-------------------------------------|-------------|
| Novas estruturas de dados           | 1 dia       |
| Funcionalidades do rotinas          | 3 dias      |
| Query de consulta para o relatório  | 1 dia       |
| Telas do relatório                  | 3 dias      |
| **Total**                           | **8 dias**  |
