---
title: WMS — Separação B2B
---

## WMS — Separação B2B

> Ajustes sugeridos para o endpoint de consulta de pedidos B2B e implementação da funcionalidade de exclusão de registros de separação.

---

### Endpoint

```http
GET /wms/B2B/ListaPedidosB2B?clienteId=
```

#### Melhoria sugerida

Adicionar os campos `razaoSocial` e `cnpjDestinatario` no JSON de resposta do endpoint.

Atualmente, essas informações não são retornadas pela API.

---

### Endpoint excluir registro

#### Nova funcionalidade

Implementar um endpoint para exclusão de registros de separação B2B através do identificador da nota.

Exemplo:

```http
DELETE /wms/Portal/SeparacaoB2B/{id}
```

ou

```http
DELETE /wms/Portal/SeparacaoB2B/Excluir?id={id}
```

#### Objetivo

Permitir que o front-end realize a exclusão de um pedido de separação B2B informando apenas o identificador do registro, sem necessidade de operações adicionais ou manipulações diretas na base de dados.

---
