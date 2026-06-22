---
title: Kpi´s de Permuta e Remoção
---

> Release 2 · Etapa 4

## Contexto

Atualmente, os KPIs exibidos na página inicial apresentam apenas informações relacionadas às permutas. Nesta etapa, será implementado um comportamento para que os indicadores sejam atualizados dinamicamente conforme a aba selecionada pelo usuário.

Ao alternar entre as abas **Permuta** e **Remoção**, os KPIs deverão refletir os dados correspondentes à opção selecionada, garantindo que as informações exibidas estejam sempre alinhadas ao contexto visualizado pelo usuário.

## Objetivo

Garantir que os KPIs exibidos na página inicial reflitam corretamente o contexto selecionado pelo usuário, atualizando dinamicamente as métricas apresentadas ao alternar entre as abas Permuta e Remoção.

## Modificações necessárias

### 1. `Páginal Inicial - Kpi´s (Front)`

* Adicionar flag Remoção/Permuta no topo a direita do card do kpi
* Implementar estilo personalizado para cada aba para poder melhor a visualização do contexto selecionado

### 2. `InteresseMovimentacaoService.GetInfosKpisAsync`

Adequar a consulta para que os dados dos KPIs sejam obtidos de acordo com o tipo de movimentação (tpMovimento) informado, retornando exclusivamente as métricas correspondentes ao contexto selecionado (Permuta ou Remoção).

## Tempo estimado

> 3 dias
