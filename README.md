# ExpertSinta - Sistema de Encadeamento para Trás

## Descrição do Projeto

O **ExpertSinta** é um sistema de exemplo que implementa um motor de inferência utilizando encadeamento para trás (backward chaining). Este sistema é projetado para gerenciar especialistas em uma plataforma, permitindo verificar se certas condições foram atendidas para que eventos específicos ocorram, como o agendamento de uma sessão ou a recomendação de um especialista.

## Funcionalidades

- Cadastro de especialistas com verificação de credenciais.
- Agendamento de sessões entre clientes e especialistas.
- Confirmação de pagamento antes da realização de sessões.
- Registro de feedbacks após a realização de sessões.
- Destaque de especialistas recomendados na plataforma.

## Estrutura do Projeto

O projeto está organizado em uma classe principal `ExpertSinta`, que encapsula os fatos e regras do sistema. As regras são definidas como métodos da classe, que são aplicadas para atualizar o estado dos fatos conforme necessário.

### Fatos

Os fatos representam o estado atual do sistema, como se um especialista foi cadastrado, se o pagamento foi confirmado, etc.

### Regras

As regras são funções que verificam certas condições e, se satisfeitas, atualizam o estado dos fatos correspondentes. Cada regra é numerada de `R1` a `R10` e segue uma lógica específica, baseada nos requisitos da plataforma.

## Exemplo de Uso

Aqui está um exemplo de como o sistema pode ser utilizado:

```python
# Example usage of the ExpertSinta system
system = ExpertSinta()

# Setting initial facts
system.facts["user_registered_as_expert"] = True
system.facts["credentials_verified"] = True

# Checking if the expert became recommended
system.backward_chaining("is_recommended_expert")

# Printing the final state of the facts
print(system.facts)
