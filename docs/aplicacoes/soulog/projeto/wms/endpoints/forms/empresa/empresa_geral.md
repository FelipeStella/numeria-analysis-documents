---
title: WMS — Empresa - Aba Geral
---

> Criação de endpoints para consulta e atualização dos dados gerais da empresa.

---

## Endpoint

```http
GET /wms/Empresa/Geral/?clienteId=
```

### Response

```json
{
  "nomeEmpresa": "string",
  "emailCorporativo": "string",
  "razaoSocial": "string",
  "cnpj": "string",
  "inscricaoEstadual": "string",
  "apiKeyBling": "string",
  "endereco": {
    "cep": "string",
    "uf": "string",
    "cidade": "string",
    "logradouro": "string",
    "numeroEndereco": "string",
    "bairro": "string"
  },
  "segmento": "string",
  "contato": {
    "telefone": "string",
    "site": "string"
  },
  "avatar": "string"
}
```

### Objetivo

Disponibilizar ao front-end todas as informações exibidas na aba **Geral** do cadastro da empresa através de um único endpoint.

---

## Endpoint de atualização

### Nova funcionalidade

Criar um endpoint para atualização dos dados editáveis das informações gerais da empresa.

```http
PUT /wms/Empresa/Geral/Edit/?clienteId=
```

### Payload

```json
{
  "nomeEmpresa": "string",
  "emailCorporativo": "string",
  "razaoSocial": "string",
  "cnpj": "string",
  "inscricaoEstadual": "string",
  "apiKeyBling": "string",
  "endereco": {
    "cep": "string",
    "uf": "string",
    "cidade": "string",
    "logradouro": "string",
    "numeroEndereco": "string",
    "bairro": "string"
  },
  "segmento": "string",
  "contato": {
    "telefone": "string",
    "site": "string"
  },
  "avatar": "string"
}
```

### Objetivo do endpoint de atualização

Permitir que o front-end atualize as informações da aba **Geral** da empresa utilizando uma estrutura compatível com o retorno do endpoint de consulta.

---
