---
title: Dashboard WMS
---

## Dashboard WMS

> Endpoint unificado que retorna todos os dados necessários ao dashboard em uma única chamada, seguindo o mesmo padrão do dashboard de envio.

---

### Endpoint

```http
GET /api/dashboard/wms
```

#### Query params

| Parâmetro  | Tipo     | Formato      | Obrigatório |
| ---------- | -------- | ------------ | ----------- |
| `dtInicio` | `string` | `DD-MM-YYYY` |             |
| `dtFim`    | `string` | `DD-MM-YYYY` |             |

**Exemplo de chamada:**

```http
GET /api/dashboard/wms?dtInicio=01-01-2025&dtFim=31-01-2025
```

---

### Response

#### Estrutura geral

```json
{
  "kpis": { ... },
  "salesOrdersSummary": { ... },
  "salesOrdersChart": { ... }
}
```

---

#### `kpis`

Indicadores gerais exibidos nos cards do topo do dashboard.

```json
{
  "kpis": {
    "nrPendencias": "number",
    "nrPrevistas": "number",
    "nrRecebidas": "number",
    "nrEmConferencia": "number",
    "nrArmazenadas": "number"
  }
}
```

---

#### `salesOrdersSummary`

Totais por status para exibição nos cards de resumo.

```json
{
  "salesOrdersSummary": {
    "novos": "number",
    "separando": "number",
    "embalando": "number",
    "aguardandoEtiqueta": "number",
    "aguardandoColeta": "number",
    "expedidos": "number",
    "semEstoque": "number",
    "erros": "number",
    "total": "number"
  }
}
```

---

#### `salesOrdersChart`

Série temporal por status para o gráfico de linha/barra, agrupada por hora.

```json
{
  "salesOrdersChart": {
    "labels": ["00h", "02h", "04h", "06h", "08h", "10h", "12h", "14h", "16h", "18h", "20h", "22h"],
    "groupData": {
      "novos": [ { "hour": "string", "status": "number", "quantity": "number", "valueMoney": "number" } ],
      "separando": [ { "hour": "string", "status": "number", "quantity": "number", "valueMoney": "number" } ],
      "embalando": [ { "hour": "string", "status": "number", "quantity": "number", "valueMoney": "number" } ],
      "aguardandoEtiqueta": [ { "hour": "string", "status": "number", "quantity": "number", "valueMoney": "number" } ],
      "aguardandoColeta": [ { "hour": "string", "status": "number", "quantity": "number", "valueMoney": "number" } ],
      "expedidos": [ { "hour": "string", "status": "number", "quantity": "number", "valueMoney": "number" } ],
      "semEstoque": [ { "hour": "string", "status": "number", "quantity": "number", "valueMoney": "number" } ],
      "erros": [ { "hour": "string", "status": "number", "quantity": "number", "valueMoney": "number" } ]
    }
  }
}
```

##### Campos de cada item em `groupData`

| Campo        | Tipo     | Descrição                       |
| ------------ | -------- | ------------------------------- |
| `hour`       | `string` | Hora do agrupamento ex: `"08h"` |
| `status`     | `number` | Código numérico do status       |
| `quantity`   | `number` | Quantidade de pedidos           |
| `valueMoney` | `number` | Valor monetário total           |

> **Labels:** horários de `00h` até `22h` de duas em duas horas (12 pontos no eixo X).

---

### Observações

- **`salesOrdersSummary`** — totais consolidados, usados nos cards do dashboard
- **`salesOrdersChart`** — dados para o gráfico, separados por hora e status
- Os campos `salesOrdersSummary` e `salesOrdersChart` foram nomeados distintos para evitar conflito de chave duplicada no JSON original
- Os status disponíveis em `groupData` seguem a mesma ordem de exibição do dashboard
