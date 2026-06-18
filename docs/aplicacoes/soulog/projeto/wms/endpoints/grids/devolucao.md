---
title: WMS — Devolução
---

> Novo endpoint para consulta de devoluções por cliente, retornando informações do pedido, nota fiscal, cliente e status da devolução.

---

## Endpoint

```http
GET /wms/Portal/Devolucao/GetPedidos?clienteId=
```

### Response

```json
{
  "devolucoes": [
    {
      "numeroPedido": "number",
      "numeroNf": "string",
      "nomeCliente": "string",
      "dataPedido": "datetime",
      "tipoIntegracao": "string",
      "status": "number",
      "dataStatus": "datetime",
      "ticketMovidesk": "string"
    }
  ]
}
```

---

## Endpoint excluir registro

### Nova funcionalidade

Implementar um endpoint para exclusão de registros de devoluções através do identificador da nota.

Exemplo:

```http
DELETE /wms/Portal/Devolucao/{id}
```

ou

```http
DELETE /wms/Portal/Devolucao/Excluir?id={id}
```

### Objetivo

Permitir que o front-end realize a exclusão de uma devolução informando apenas o identificador do registro, sem necessidade de operações adicionais ou manipulações diretas na base de dados.

---
