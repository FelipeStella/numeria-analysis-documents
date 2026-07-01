---
title: Setores sem vínculo com comarca (TASK-2732)
---

> Release 2 · Etapa 4

## Contexto

Setores iniciados com o prefixo `0302800*` não possuem comarca vinculada. Será necessário implementar uma lógica para associá-los à comarca de Porto Alegre.

## Objetivo

Mapear e corrigir os setores sem comarca de origem definida.

## Modificações necessárias

### 1. `RheTJService.ResolverNormalizadorSetor`

* Implementar lógica para que setores iniciados com `0302800` sejam automaticamente vinculados à comarca de Porto Alegre.

## Tempo estimado

> 1 dia
