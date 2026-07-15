---
title: Cálculo de Tempo de Serviço no Poder Judiciário (TASK-2787)
---

> **Release 2 · Etapa 5**

## Contexto

Atualmente, o cálculo do tempo de serviço no Poder Judiciário não considera corretamente os períodos de múltiplos vínculos do servidor com o **TJRS**.

A regra deve contemplar todos os vínculos pertencentes à empresa **TJRS (6)**, desde que não exista interrupção entre o término de um vínculo e o início do vínculo seguinte.

## Objetivo

Adequar a regra de negócio para que o cálculo do tempo de serviço no Poder Judiciário considere a sequência contínua de vínculos com o TJRS, somando esse período ao tempo já registrado no histórico.

## Regra de cálculo

O tempo de serviço no Poder Judiciário será composto por:

- O somatório dos períodos dos vínculos (`RheVinculo`) pertencentes à empresa **TJRS (6)**, desde que sejam contínuos;
- O tempo já registrado em `HistoricoTempoServicoPJRS.NrTempo`.

Um vínculo será considerado contínuo quando:

```text
DtExercicio do vínculo atual = DtVacancia do próximo vínculo
```

**Fórmula:**

```text
Tempo de Serviço no PJ =
Σ Períodos contínuos de RheVinculo (Empresa = TJRS)
+
HistoricoTempoServicoPJRS.NrTempo
```

## Modificações necessárias

| # | Componente                                                | Alteração                                                                                                                                                 |
|---|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | `GestaoMovimentacoesService.BuscarContextoDesempateAsync` | Implementar a busca de todos os vínculos da empresa **TJRS (6)**, preservando a ordem cronológica necessária para identificar a continuidade entre eles.  |
| 2 | `TempoCarreiraStrategy.CalcularAsync`                     | Calcular o tempo total dos vínculos contínuos e somá-lo ao valor de `HistoricoTempoServicoPJRS.NrTempo`.                                                  |

## Estimativa

**Tempo estimado:** 1 dia.
