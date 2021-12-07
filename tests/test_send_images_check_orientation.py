from deep_check_orientation import check_orientation
from utils.image_view import view_image

image = 'images/image_test.jpg'

# VERIFICANDO A ROTAÇÃO DA IMAGEM
predictions, number_rotate, image_correct_orientation = check_orientation().orchesta_model(image)

# VISUALIZANDO A IMAGEM ROTACIONADA
view_image(image_correct_orientation)