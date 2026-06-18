---
title: Eventos de Comarca de Origem
---

## Comarca de Origem

> Release 2 · Etapa 4

### Contexto

Servidores removidos temporariamente podem ter sua comarca de origem definida por um evento específico na carga de dados. Quando esse evento não está presente na carga, a comarca de origem (e o respectivo tempo de serviço na comarca atual) não pode ser calculada corretamente pela regra atual.

### Objetivo

Criar uma fonte alternativa de dados (`RheEventoComarcaOrigem`) para suprir a comarca de origem e o início das atividades nos casos em que o evento de origem não está presente na carga, ajustando as regras de negócio que dependem dessa informação.

### Fonte de dados

Os dados para popular `RheEventoComarcaOrigem` virão da planilha [Comarcas a corrigir SIGEP.xlsx](<./anexos/Comarcas a corrigir SIGEP.xlsx>).

### Estrutura de dados

#### Nova tabela: `RheEventoComarcaOrigem`

| Campo                    | Tipo   | Descrição                                           |
| ------------------------ | ------ | --------------------------------------------------- |
| IdRheEventoComarcaOrigem | number | Identificador único do registro (chave primária).   |
| NrFuncional              | string | Número funcional do servidor.                       |
| NrVinculo                | number | Número do vínculo do servidor.                      |
| NoServidor               | string | Nome do servidor.                                   |
| NoComarcaOrigem          | string | Nome da comarca de origem do servidor.              |
| DtInicioAtividades       | date   | Data de início das atividades na comarca de origem. |

> `NrFuncional` + `NrVinculo` identificam o servidor/vínculo ao qual o registro se refere.

```json
{
  "IdRheEventoComarcaOrigem": "number",
  "NrFuncional": "string",
  "NrVinculo": "number",
  "NoServidor": "string",
  "NoComarcaOrigem": "string",
  "DtInicioAtividades": "date"
}
```

### Modificações necessárias

#### 1. `RheTJService.GetTempoServicoComarcaAtualAsync`

Ao calcular o tempo de serviço na comarca atual para eventos de cargo `'CARGO EFETIVO'`, buscar também o registro correspondente em `RheEventoComarcaOrigem` (por `NrFuncional` + `NrVinculo`) e considerar `DtInicioAtividades` como ponto de partida do cálculo quando o evento de origem não estiver presente na carga.

#### 2. `SharedService.GetComarcaOrigemAsync`

Quando a comarca de origem não puder ser determinada pelo evento da carga, buscar o valor de `NoComarcaOrigem` em `RheEventoComarcaOrigem` (por `NrFuncional` + `NrVinculo`) como fallback.

### Tempo estimado

> 3 dias
