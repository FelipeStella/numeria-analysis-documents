---
title: WMS — Empresa - Aba Integrações
---

> Criar endpoints para busca e atualização dos dados de integração vinculados à empresa.

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
{
  "frenetAtivo": "boolean",
  "tokenFrenet": "string",
  "rastreioAtivo": "boolean",
  "linkRastreio": "string",
  "blingAtivo": "boolean",
  "apiKeyBling": "string",
}
```

### Payload Atualização dos dados

```json
{
  "frenetAtivo": "boolean",
  "tokenFrenet": "string",
  "rastreioAtivo": "boolean",
  "linkRastreio": "string",
  "blingAtivo": "boolean",
  "apiKeyBling": "string",
}
```

### Objetivo

Disponibilizar ao front-end todas as informações exibidas na aba **Integrações** do cadastro da empresa através de um único endpoint.

Permitir que o front-end atualize as informações da aba **Integrações** da empresa utilizando uma estrutura.

---
