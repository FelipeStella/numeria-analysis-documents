---
title: Cálculo de Tempo de Carreira (TASK-2790)
---

> **Release 2 · Etapa 5**

## Contexto

Atualmente, o cálculo do tempo de carreira não considera determinados afastamentos que devem compor o tempo de serviço do servidor.

É necessário ajustar a regra de negócio para que os afastamentos dos tipos **penas disciplinares** e **normal** sejam incluídos no cálculo.

## Objetivo

Adequar o cálculo do tempo de carreira para considerar os afastamentos elegíveis, garantindo que o tempo de serviço seja calculado conforme a regra de negócio.

## Regra de cálculo

O tempo de carreira será composto por:

- **Tempo de carreira** (`RheTempoServico.NrCarreira`);
- **Somatório dos dias** (`RheAfastamento.NrDias`) dos afastamentos cujo `CdMnemonico` seja um dos seguintes:
  - `SMV`
  - `SSV`
  - `FNJ`
  - `GRE`
  - `LIP`

**Fórmula:**

```text
Tempo de Carreira =
RheTempoServico.NrCarreira +
Σ RheAfastamento.NrDias
```

Onde:

```text
CdMnemonico ∈ { SMV, SSV, FNJ, GRE, LIP }
```

## Modificações necessárias

| # | Componente                                                | Alteração                                                                                                                                           |
|---|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | `GestaoMovimentacoesService.BuscarContextoDesempateAsync` | Implementar a busca dos afastamentos dos tipos **penas disciplinares** e **normal**, considerando os mnemônicos `SMV`, `SSV`, `FNJ`, `GRE` e `LIP`. |
| 2 | `TempoCarreiraStrategy.CalcularAsync`                     | Somar ao tempo de carreira (`NrCarreira`) o total de dias (`NrDias`) dos afastamentos recuperados.                                                  |

## Estimativa

**Tempo estimado:** 1 dia.
