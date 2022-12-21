import os
import matplotlib.pyplot as plt
import numpy as np

def print_image(out_sync):
    figureure_size = 32 / float(100), 32 / float(100)
    figure = plt.figure(figsize=figureure_size)
    ax = figure.add_axes([0, 0, 1, 1])
    ax.imshow(out_sync * 255, cmap='binary')
    ax.axis("off")
    plt.show()

def get_arr_image(name_directory: str) -> list:
    global arr_image
    for begin_directory, _, arr_image in os.walk(name_directory):
        arr_image = [os.path.join(begin_directory, name_photo) for name_photo in arr_image]
    return arr_image

def to_predict_file_directory_image(name_directory: str, model, iter, async_iter):
    np.random.seed(1)
    image = np.mean(plt.imread(name_directory), axis=2)
    try:
        for _ in image:
            continue
    finally:
        output_async = model.predict(image, name_directory)#, iter, async_iter)

    if True:
        print_image(np.where(image < 0.5, 1, -1))
        print_image(output_async)