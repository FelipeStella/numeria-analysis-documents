---
title: WMS — Empresa - Aba Serviços
---

> Criação de endpoints para listagem e atualização dos serviços do bling vinculados à empresa.

---

## Endpoint

### Busca

```http
GET /wms/Empresa/ServicosBling/?clienteId=
```

### Atualização

```http
GET /wms/Empresa/ServicosBling/update/?clienteId=
```

### Response Busca

```json
[
  {
    "nomeServico": "string",
    "idServicoBling": "string",
  }
]
```

### Payload Atualização dos dados

```json
[
  {
    "nomeServico": "string",
    "idServicoBling": "string",
  }
]
```

### Objetivo

Disponibilizar ao front-end todas as informações exibidas na aba **Serviços** do cadastro da empresa através de um único endpoint.

Permitir que o front-end atualize as informações da aba **Serviços** da empresa utilizando uma estrutura.

---
