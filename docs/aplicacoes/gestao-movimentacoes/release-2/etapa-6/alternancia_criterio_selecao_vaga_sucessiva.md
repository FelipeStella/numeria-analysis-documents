---
title: Aplicar regra de alternância de critérios em vagas sucessivas (TASK-2802)
---

> **Release 2 · Etapa 6**

## Contexto

No fluxo de geração de matches de remoção sucessiva, as vagas geradas sucessivamente devem
alternar entre os critérios de seleção **Merecimento** e **Antiguidade na Carreira**.

**Exemplo:**

1. Vaga original → critério **Merecimento**
2. 1ª vaga sucessiva gerada → critério **Antiguidade na Carreira**
3. 2ª vaga sucessiva gerada → critério **Merecimento**
4. E assim sucessivamente, alternando a cada nova vaga sucessiva.

O critério da **vaga original** é o já cadastrado no edital (agora único por vaga, ver
[Modificações necessárias](#modificações-necessárias)); a alternância se aplica somente às
vagas **sucessivas** geradas a partir dela.

## Objetivo

Passar o critério de seleção de uma vaga a ser **único** (em vez de uma lista), e alterar a
regra de geração de vagas sucessivas no fluxo de remoção pra alternar automaticamente entre
os dois critérios a cada nova vaga gerada.

## Modificações necessárias

### Projeto Gestão de Movimentações

- [ ] Alterar formulário de cadastro do edital do tipo remoção para permitir somente **um**
      critério de seleção por vaga (hoje permite múltiplos)
- [ ] Adicionar coluna `IdCriterioSelecao` (FK) na estrutura `EditalRemocaoVaga`
- [ ] Migrar dados existentes: preencher `IdCriterioSelecao` das vagas já cadastradas a partir
      da estrutura atual (N:N), antes de tornar a coluna obrigatória
- [ ] Ajustar service, entidade, DTOs e testes de unidade para comportar a nova estrutura de
      critério único por vaga
- [ ] Remover estrutura `CriterioSelecaoCriterioDesempate` (não é mais necessária: critério de
      seleção deixa de ser uma relação N:N com desempate por prioridade)
- [ ] Remover estrutura `EditalRemocaoVagaCriterioSelecao` (substituída pela FK direta
      `IdCriterioSelecao` em `EditalRemocaoVaga`)

### Projeto Rotinas

- [ ] No fluxo de remoção sucessiva, alterar a etapa de construção de nova vaga para aplicar
      a alternância de critério de seleção (Merecimento ⇄ Antiguidade na Carreira) a cada vaga
      sucessiva gerada

## Critérios de aceite

- [ ] Não é mais possível cadastrar mais de um critério de seleção por vaga no formulário do edital
- [ ] Vagas sucessivas geradas alternam corretamente o critério a cada nova geração, começando
      pelo critério oposto ao da vaga original
- [ ] Editais já existentes continuam funcionando após a migração (sem quebra de dados)
- [ ] Testes de unidade cobrindo a nova regra de alternância (incluindo o caso de 3+ vagas
      sucessivas em sequência)

## Riscos / pontos em aberto

- Confirmar se há edital em produção com vaga tendo **mais de um** critério cadastrado
  atualmente — se sim, definir regra de qual critério prevalece na migração (o de maior
  prioridade? o mais recente?)

## Estimativa

**Tempo estimado:** 5 dias

| Frente                                                          | Estimativa  |
|-----------------------------------------------------------------|-------------|
| Gestão de Movimentações (form, migração, service, DTOs, testes) | 3 dias      |
| Rotinas (regra de alternância)                                  | 1 dia       |
| Testes integrados / validação ponta a ponta                     | 1 dia       |
