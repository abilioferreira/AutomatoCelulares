# Simulações Baseadas em Autômatos Celulares

Este repositório contém implementações de três modelos baseados em autômatos celulares: **Game of Life**, **Bacterial Growth** e **Predator-Prey**. Esses modelos são usados para simular fenômenos naturais e interações dinâmicas em ambientes controlados, sendo importantes para estudar sistemas biológicos, ecológicos e computacionais.

## Modelos Implementados

### 1. **Game of Life** (Jogo da Vida)
Criado por John Conway em 1970, o **Game of Life** é um autômato celular onde células em uma grade podem estar vivas ou mortas. A evolução das células segue regras simples que geram padrões complexos. As regras são:
- Uma célula viva com menos de dois vizinhos vivos morre por solidão.
- Uma célula viva com dois ou três vizinhos vivos continua viva.
- Uma célula viva com mais de três vizinhos vivos morre por superpopulação.
- Uma célula morta com exatamente três vizinhos vivos se torna viva por reprodução.

### 2. **Bacterial Growth** (Crescimento Bacteriano)
Este modelo simula o crescimento de colônias bacterianas em um ambiente digital. As bactérias crescem em espaços adjacentes com uma probabilidade determinada e dependem da presença de outras bactérias para se expandirem. Esse modelo é útil para simular dinâmicas microbiológicas e processos como propagação de infecções e resistência a antibióticos.

### 3. **Predator-Prey** (Predador e Presa)
Neste modelo, predadores e presas interagem em um ambiente digital. Presas se reproduzem com uma probabilidade determinada, enquanto predadores se alimentam das presas e têm um tempo limite antes de morrerem de fome. Este modelo ajuda a estudar dinâmicas populacionais e interações ecológicas, sendo aplicável em biologia e ecologia.

## Instalação

Para rodar os modelos, você precisará de Python 3.x e das bibliotecas necessárias. Siga os passos abaixo para configurar o ambiente:

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu_usuario/sua_repo.git
    cd sua_repo
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/macOS
    venv\Scripts\activate  # Para Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Executando os Modelos

- **Game of Life**: Para rodar o modelo **Game of Life**, execute o arquivo `game_of_life.py`.
  
- **Bacterial Growth**: Para rodar o modelo **Bacterial Growth**, execute o arquivo `bacterial_growth.py`.
  
- **Predator-Prey**: Para rodar o modelo **Predator-Prey**, execute o arquivo `predator_prey.py`.

Cada modelo usa o Pygame para visualização e permite interatividade com a grade de células. Você pode interagir com os modelos usando o teclado e o mouse.

## Importância das Simulações Baseadas em Autômatos Celulares

Os autômatos celulares são ferramentas poderosas para modelar e entender fenômenos naturais e artificiais, como o crescimento celular, a propagação de doenças e as interações ecológicas. Esses modelos são aplicáveis em várias áreas:

- **Biologia e Medicina**: Simulação de processos biológicos, como o crescimento de populações de microrganismos ou a propagação de doenças.
- **Ciência da Computação**: Estudo de sistemas auto-organizados e algoritmos evolutivos.
- **Inteligência Artificial**: Modelagem de agentes autônomos baseados em regras locais e interações com o ambiente.
  
Além disso, podem ser usados para estudar fenômenos em redes sociais, economia e sistemas de transporte.

## Conclusão

Este projeto visa ilustrar como regras simples podem gerar padrões complexos e interações dinâmicas. O **Game of Life** destaca a emergência de padrões a partir de regras locais, enquanto **Bacterial Growth** e **Predator-Prey** aplicam esses conceitos em contextos biológicos reais, proporcionando uma melhor compreensão de dinâmicas ecológicas e processos naturais.


