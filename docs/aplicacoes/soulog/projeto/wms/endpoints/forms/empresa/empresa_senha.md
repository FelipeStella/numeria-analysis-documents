---
title: WMS — Empresa - Aba Alterar Senha
---

> Criar endpoint para atualizar a senha de acesso ao módulo WMS.

---

## Endpoint

```http
GET /wms/Empresa/Senha/Update?clienteId=
```

### Payload

```json
{
  "senhaAntiga": "string",
  "novaSenha": "string",
  "comfirmeSenha": "string",
}
```

> Os dados precisam estar mascarados

### Objetivo

Permitir que o front-end atualize a senha da empresa utilizada no acesso ao sistema.

---
