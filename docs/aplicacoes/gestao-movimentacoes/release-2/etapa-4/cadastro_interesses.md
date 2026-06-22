---
title: Cadastro de Interesse
---

> Release 2 · Etapa 4

## Contexto

Atualmente, a funcionalidade de exclusão de interesse está disponível apenas na tela de histórico. Nesta etapa, ela será estendida para o formulário de cadastro de interesse, permitindo que o usuário realize a exclusão diretamente durante o preenchimento ou edição do formulário.

## Objetivo

Permitir que o usuário exclua um interesse diretamente pelo formulário de interesse, sem a necessidade de acessar a tela de histórico, tornando o fluxo mais simples, intuitivo e consistente com as demais funcionalidades da aplicação.

## Modificações necessárias

### 1. `CadastroInteresseForm (Front)`

* Adicionar ação de exclusão no formulário de Cadastro de Interesse.
* Exibir botão **Excluir Interesse** para registros já cadastrados.
* Solicitar confirmação do usuário antes de executar a exclusão.
* Após a exclusão, atualizar a interface de acordo com o fluxo definido pela aplicação.

## Tempo estimado

> 1 dia
