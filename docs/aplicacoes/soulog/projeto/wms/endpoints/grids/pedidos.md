---
title: WMS — Pedidos
---

## WMS — Pedidos

> Ajustes sugeridos para os endpoints relacionados a pedidos e canais de venda, visando simplificar o consumo das APIs pelo front-end.

---

### Endpoint

```http
GET /wms/Portal/Pedido/BuscaPedidosSeparacaoClienteId?clienteId=
```

#### Melhoria sugerida

Adicionar o campo `nomeCliente` no JSON de resposta do endpoint.

Atualmente, o front-end não exibe essa informação na grid.

---

### Endpoint canal venda

```http
GET /wms/B2B/ListaCanalVenda?clienteId=
```

#### Melhoria sugerida canal venda

Permitir a listagem dos canais de venda sem a obrigatoriedade de informar o parâmetro `clienteId`.

Alternativas:

- Tornar o parâmetro `clienteId` opcional no endpoint atual.
- Criar um novo endpoint específico para retornar todos os canais de venda disponíveis.

Exemplo:

```http
GET /wms/B2B/ListaCanalVenda
```

ou

```http
GET /wms/ListaCanaisVenda
```

Dessa forma, o front-end poderá carregar a lista de canais de venda independentemente da seleção prévia de um cliente.

### Endpoint excluir registro

#### Nova funcionalidade

Implementar um endpoint para exclusão de registros de pedidos através do identificador da nota.

Exemplo:

```http
DELETE /wms/Portal/Pedido/{id}
```

ou

```http
DELETE /wms/Portal/Pedido/Excluir?id={id}
```

#### Objetivo

Permitir que o front-end realize a exclusão de um pedido informando apenas o ID do registro, sem necessidade de operações adicionais ou manipulações diretas na base de dados.

---
