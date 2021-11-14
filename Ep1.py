from PIL import Image
import numpy as np

# считаем картинку в numpy array
img = Image.open("lunar03_raw.jpg")
data = np.array(img)

# ... логика обработки
updated_data = (data - data.min()) / (data.max() - data.min()) * 255

# запись картинки после обработки
res_img = Image.fromarray(updated_data)
res_img = res_img.convert("L")
res_img.save("lunar03_new.jpg")