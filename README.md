# Processamento de Imagens com Python

Este projeto é uma biblioteca simples para processamento de imagens usando Python. Ele permite a manipulação de imagens, como exibição, inversão, aplicação de filtros e redução de brilho.

## Requisitos

- Python 3.8 ou superior
- Bibliotecas: `numpy`, `matplotlib`, `PIL`

Você pode instalar as bibliotecas necessárias usando o comando:

```bash
pip install numpy matplotlib pillow
```

# Estrutura do projeto

```processamento-imagens-python/
│
├── __init__.py
├── image_process.py
└── setup.py
```

# Métodos Disponíveis

- show_image_pillow(): Exibe a imagem usando a biblioteca PIL.
- show_array(): Imprime a matriz de pixels da imagem.
- invert(): Inverte a imagem horizontalmente.
- filter(color, filter): Aplica um filtro em um ou mais canais de cor. Exemplo: img.filter(['r', 'g'], [10, 20]).
- weak(): Reduz o brilho da imagem.

### Notas Finais

- Certifique-se de substituir `'caminho_da_imagem'` por um caminho válido onde sua imagem está armazenada.
- Você pode ajustar a seção de "Dificuldades" conforme sua preferência, se desejar adicionar mais detalhes ou se sentir que outros pontos são importantes.

# Contribuições

Sinta-se à vontade para contribuir com melhorias ou correções. Seu feedback é bem-vindo!
