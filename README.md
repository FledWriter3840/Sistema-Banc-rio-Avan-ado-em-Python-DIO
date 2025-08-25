# 🏦 Sistema Bancário em Python

Este projeto implementa um **sistema bancário simples** em Python, que permite gerenciar **clientes, contas e transações financeiras** como depósitos, saques, extratos e saldo.

## 🚀 Funcionalidades

* Criar clientes com dados como nome, CPF, data de nascimento e endereço.
* Criar contas bancárias vinculadas a clientes.
* Realizar **depósitos** e **saques** com controle de limite e número máximo de saques.
* Consultar o **extrato** de movimentações.
* Consultar o **saldo disponível**.
* Listar todas as **contas cadastradas**.

## 📋 Menu de Operações

```
[1] Depositar  
[2] Sacar  
[3] Extrato  
[4] Saldo  
[5] Criar Conta Bancária  
[6] Criar Cliente  
[7] Contas Cadastradas  
[8] Sair  
```

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**

## 📂 Estrutura do Projeto

* `menu()` → Exibe o menu principal.
* `depositar()` → Realiza depósitos.
* `sacar()` → Controla saques com regras de limite e quantidade.
* `saldo()` → Mostra o saldo da conta.
* `exibir_extrato()` → Mostra o extrato de movimentações.
* `cadastro_cliente()` → Cadastra novos clientes.
* `conta_bancaria()` → Cria contas vinculadas a clientes.
* `contas_cadastradas()` → Lista todas as contas criadas.
* `main()` → Função principal que gerencia o fluxo do sistema.

## 📌 Observações

* O limite de saque é **R\$ 500,00 por operação**.
* O número máximo de saques diários é **3**.
* Cada cliente é identificado unicamente pelo **CPF**.

