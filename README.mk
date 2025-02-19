# Projeto Delivery

Este repositório contém o projeto **Delivery**, uma aplicação de gerenciamento e venda de produtos online, voltada para o setor de delivery de alimentos.

## Descrição

O **Projeto Delivery** visa facilitar o gerenciamento de produtos, categorias, adicionais e opções, além de fornecer uma interface administrativa para o gerenciamento dos itens do sistema. O projeto foi desenvolvido utilizando o framework **Django** e o banco de dados relacional **SQLite**.

## Requisitos do Sistema

Abaixo estão os requisitos analisados para o desenvolvimento do sistema até o momento:

### Requisitos Funcionais

1. **Criação de Superusuário**
   - Permitir a criação de um superusuário para o gerenciamento da plataforma via interface administrativa do Django.
   
2. **Configuração de Templates**
   - Estruturar os templates da aplicação para renderização das páginas HTML, incluindo o template base (`base.html`).

3. **Estruturação do Banco de Dados**
   - Definir a estrutura de dados para o gerenciamento de **produtos**, **categorias**, **adicionais** e **opções**.

4. **Carrinho de Compras**
   - Implementar um sistema de carrinho de compras que armazena os itens do carrinho, com validação de adicionais e cálculo do preço total.

5. **Integração com GitHub**
   - Subir o projeto para um repositório remoto no GitHub para versionamento e controle de código.

### Requisitos Não Funcionais

1. **Performance**
   - A aplicação deve ser eficiente ao processar as requisições e garantir que o desempenho não seja afetado com um grande número de produtos e adicionais.

2. **Usabilidade**
   - A interface administrativa e as páginas do usuário devem ser simples e intuitivas.

3. **Segurança**
   - O sistema de sessões deve ser seguro para garantir a confidencialidade dos dados dos usuários e do carrinho de compras.

## Desafios e Pendências

1. **Correção de Erros em Templates**
   - Ajustes na estrutura de diretórios e definição de bibliotecas para garantir que todos os templates sejam carregados corretamente.
   
2. **Verificação de Quantidade de Itens no Carrinho**
   - A validação das quantidades mínimas e máximas de adicionais precisa ser melhor testada para garantir seu funcionamento.

3. **Ajustes de Layout e Design**
   - O design das páginas precisa de ajustes para garantir uma melhor experiência de usuário, especialmente nas páginas de produtos e carrinho.

## Conclusão

O projeto está na fase de desenvolvimento com funcionalidades principais implementadas, e está pronto para ser continuado, testado e melhorado. 

## Instalação e Execução

1. Clone o repositório:

   ```bash
   git clone https://github.com/Jeffy-ADS/delivery.git
