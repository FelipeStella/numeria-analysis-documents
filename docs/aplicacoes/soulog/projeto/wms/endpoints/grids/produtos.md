---
title: WMS — Produto - Movimentação do estoque
---

> Correção necessária na funcionalidade de visualização da DANFE de saída disponível na grid de movimentação de estoque acessada através das ações da grid de pedidos.

---

## Endpoint

```http
GET /wms/Estoque/XmlDanfeSaida?chaveNF=
```

### Problema identificado

Na grid de movimentação do estoque existe uma funcionalidade para exibição da DANFE.

Atualmente:

- A visualização da DANFE de entrada está funcionando corretamente.
- A visualização da DANFE de saída não está funcionando.

Ao consultar o endpoint de DANFE de saída, independentemente da chave informada, a resposta retornada é uma página HTML contendo a mensagem:

```text
Nota fiscal não encontrada ou URL inválida/expirada.
```

### Resultado atual

O endpoint retorna um conteúdo HTML semelhante ao seguinte:

```html
<!DOCTYPE html>
<html>
...
<p>Nota fiscal não encontrada ou URL inválida/expirada.</p>
...
</html>
```

### Resultado esperado

O endpoint deve retornar corretamente o XML ou o conteúdo da DANFE correspondente à chave da NF-e informada, da mesma forma que já ocorre na funcionalidade de DANFE de entrada.

### Objetivo

Restabelecer o funcionamento da visualização da DANFE de saída para que os usuários possam consultar os documentos fiscais diretamente pela grid de movimentação de estoque.

---
