---
title: WMS — Notas de Entradas
---

## WMS — Notas de Entradas

> Endpoint GET existente para busca de entradas por período. O campo `uf` atualmente é extraído do XML no front-end — se possível, passar a retorná-lo diretamente na response para simplificar o consumo.

---

### Endpoint

```http
GET /wms/Portal/Entrada/BuscarEntradas
```

#### Melhoria sugerida

O campo `uf` hoje é resolvido no front-end via leitura do XML da NF-e.

Propõe-se que o backend passe a retorná-lo diretamente na response.

---

### Endpoint excluir registro

#### Nova funcionalidade

Implementar um endpoint para exclusão de registros de nota de entrada através do identificador da nota.

Exemplo:

```http
DELETE /wms/Portal/Entrada/{id}
```

ou

```http
DELETE /wms/Portal/Entrada/Excluir?id={id}
```

#### Objetivo

Permitir que o front-end realize a exclusão de uma nota de entrada informando apenas o ID do registro, sem necessidade de operações adicionais ou manipulações diretas na base de dados.

---
