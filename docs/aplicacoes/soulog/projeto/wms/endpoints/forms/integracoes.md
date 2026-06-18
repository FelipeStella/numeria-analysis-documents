---
title: WMS — Integrações
---

> Ajustes e novos endpoints para gerenciamento das configurações de integração dos canais de venda.

---

## Endpoint

```http
GET /wms/B2B/ListaCanalVenda?clienteId=
```

### Melhoria sugerida

Adicionar as seguintes informações ao JSON de resposta do endpoint:

- `horaVenda`
- `horaPostagem`
- `horaExpedicao`

Alternativamente, criar um novo endpoint específico para consulta das integrações.

---

## Novo Endpoint

```http
GET /wms/Integracoes?clienteId=
```

### Response

```json
{
  "IdIntegracao": "number",
  "idCanalVenda": "number",
  "nomeCanalVenda": "string",
  "horaVenda": "timestamp",
  "horaPostagem": "timestamp",
  "horaExpedicao": "timestamp"
}
```

### Objetivo

Disponibilizar ao front-end as configurações de horários utilizadas pelas integrações de cada canal de venda, sem necessidade de consultas adicionais.

---

## Endpoint de edição

### Nova funcionalidade

Criar um endpoint para atualização das configurações de integração.

```http
PUT /wms/Integracoes/Edit
```

### Payload

```json
{
  "idIntegracao": "number",
  "idCanalVenda": "number",
  "horaVenda": "timestamp",
  "horaPostagem": "timestamp",
  "horaExpedicao": "timestamp"
}
```

### Objetivo edição integração

Permitir que o front-end atualize os horários de venda, postagem e expedição associados a uma integração, mantendo as configurações sincronizadas com os canais de venda cadastrados.

---
