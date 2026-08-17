# Factory Method — Logistics

Implementação do padrão de projeto **Factory Method** em Python, utilizando um sistema de logística capaz de criar diferentes tipos de transporte, como **caminhão, navio e avião**.

## Sobre o projeto

O projeto demonstra a aplicação do padrão **Factory Method** para separar a criação dos objetos de transporte da lógica de entrega.

A classe `Logistics` define o método `createTransport()`, responsável pela criação do transporte. Cada subclasse de logística implementa esse método de acordo com o tipo de transporte utilizado:

- `RoadLogistics` → `Truck`
- `SeaLogistics` → `Ship`
- `FlyLogistics` → `Plane`

Dessa forma, o método `planDelivery()` pode trabalhar com diferentes tipos de transporte sem precisar conhecer diretamente suas implementações.


## Como executar

Certifique-se de possuir o **Python 3** instalado.

Clone o repositório e acesse o diretório do projeto:

```bash
git clone git@github.com:mariaritalustosa/factory-method-.git
cd <project-direct>
```

Execute o programa:

```bash
python3 factory_method.py
```

## Exemplo de saída

```text
Carregado com RoadLogistics. Logistics: Transporte sendo preparado...
('truck preparado para a entrega: Caminhão1', 'Transporte térreo...')


Carregado com SeaLogistics. Logistics: Transporte sendo preparado...
('ship preparado para a entrega: Navio1', 'Transporte marítimo...')


Carregado com FlyLogistics. Logistics: Transporte sendo preparado...
('plane preparado para a entrega: Avião1', 'Transporte aéreo...')
```