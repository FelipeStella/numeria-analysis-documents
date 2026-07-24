---
title: Candidatos aptos - Relatório de candidatos por sede (TASK-2818)
---

> **Release 2 · Etapa 6**

## Contexto

O relatório em Excel de candidato por sede possui uma aba que lista todos os candidatos que
concorreram, de alguma forma, em pelo menos um match **concluído**. O cliente identificou a
necessidade de também listar todos os candidatos **aptos** ao processo — ou seja, que
atendem aos requisitos do edital para concorrer — independentemente de terem sido de fato
selecionados no match final.

**Exemplo:** o servidor João da Silva estava apto a participar de um match para a comarca de
Porto Alegre, cujo critério de seleção é Merecimento. O sistema identificou que ele não
possui nota de avaliação e, por isso, foi excluído do processo de match. Ainda assim, João
deve aparecer na nova aba, já que ele era elegível a concorrer — a ausência de nota de
avaliação impede a **classificação** dele, não a **elegibilidade**.

## Objetivo

Adicionar uma nova aba ao relatório de candidato por sede, listando todos os candidatos
aptos a participar do processo de geração de matches do tipo remoção — inclusive os que
foram excluídos por falta de critério de desempate/seleção — para que o administrador possa
validar o processo por completo, não só os matches concluídos.

## Modificações necessárias

- [ ] Criar consulta para buscar, com `DISTINCT`, todos os candidatos vinculados ao edital a
      partir de `FluxoRemocaoHistorico` (histórico de todo o fluxo de remoção, incluindo
      candidatos excluídos em etapas intermediárias)
- [ ] Reaproveitar a estrutura de `ParticipanteRemocaoDto` para popular a nova aba (mesmos
      campos já usados na aba atual de candidatos)
- [ ] Adicionar a nova aba "Candidatos Aptos" ao relatório de candidato por sede, junto à
      aba existente de candidatos em matches concluídos

## Critérios de aceite

- [ ] A nova aba lista todos os candidatos aptos ao edital, incluindo os excluídos por falta
      de critério de desempate/seleção (ex: sem nota de avaliação)
- [ ] Candidatos que nunca chegaram a ser elegíveis (ex: cargo/comarca fora do escopo do
      edital) **não** aparecem na nova aba
- [ ] A aba existente (candidatos em matches concluídos) permanece inalterada
- [ ] Informações exibidas seguem o mesmo padrão de campos de `ParticipanteRemocaoDto`

## Riscos / pontos em aberto

- Definir com o cliente o que exatamente caracteriza "apto" (ver observação no Contexto)
- Validar se `FluxoRemocaoHistorico` já registra o motivo da exclusão (útil para eventual
  coluna de "motivo" na nova aba, caso o cliente peça isso numa próxima iteração)

## Estimativa

**Tempo estimado:** 3 dias
