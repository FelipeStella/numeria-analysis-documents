---
title: Critério de seleção por merecimento (TASK-2769)
---

> Release 2 · Etapa 4

## Contexto

Regras para definição de elegibilidade do servidor nas vagas por merecimento:

* Se o servidor não possui atributo referente ao último ano, ele não concorre às vagas por merecimento.
* Se possui atributo, mas o campo "info2" está preenchido como "Período não avaliativo", ele também não concorre às vagas por merecimento.

## Objetivo

Ajustar a lógica de definição da nota por merecimento, considerando os critérios de elegibilidade acima.

## Modificações necessárias

### 1. `GestaoMovimentacoesService.BuscarContextoCriteriosSelecaoAsync`

* Alterar a lógica atual que atribui valor zero, contemplando o cenário em que a última avaliação do servidor não existe.

### 2. `FormacaoMatchRemocaoSimplesExtensions.ResolveCandidatosGrupo`

* Remover do grupo de candidatos o servidor que não atender aos pré-requisitos de merecimento.

## Tempo estimado

> 3 dias
