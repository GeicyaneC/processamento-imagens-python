from image_process import image

# Inicializar uma imagem
img = image('caminho_da_imagem')

# Exibir a imagem
img.show_image_pillow()

# Exibir a matriz de pixels
img.show_array()

# Inverter a imagem horizontalmente
img.invert()

# Aplicar um filtro no canal vermelho (ex.: aumentar o canal vermelho em 100)
img.filter(['r', 'b'], [5, 20])

# Reduzir o brilho da imagem
img.weak()
