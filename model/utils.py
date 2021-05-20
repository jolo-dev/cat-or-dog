import io
import os

import requests
import keras
import numpy
import PIL
import PIL.ImageOps

import tensorflow

tensorflow.compat.v1.logging.set_verbosity(tensorflow.compat.v1.logging.ERROR)


def predict(original_image):
    """
    run the prediction on the image handed in.
    """
    model = _construct_model()
    model.load_weights(
        _get_weights("https://challenge.dkb-ai.cloud/DevOps/data/cats_and_dogs.h5")
    )

    image = _preprocess_image(original_image)
    pred = model.predict(image.reshape((1,) + image.shape))[0, 0]

    if pred > 0.5:
        retval = f"{pred * 100:.0f}% dog"
    else:
        retval = f"{(1 - pred) * 100:.0f}% cat"

    return retval


def _get_weights(url):
    local_filename = "weights.h5"
    r = requests.get(url, local_filename)
    open(local_filename, "wb").write(r.content)
    return local_filename


def _construct_model():
    """
    constructs the model skeleton
    """
    model = keras.models.Sequential()

    model.add(
        keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(150, 150, 3))
    )
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Conv2D(64, (3, 3), activation="relu"))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Conv2D(128, (3, 3), activation="relu"))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Conv2D(128, (3, 3), activation="relu"))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dropout(0.5))
    model.add(keras.layers.Dense(512, activation="relu"))
    model.add(keras.layers.Dense(1, activation="sigmoid"))

    model.compile(
        loss="binary_crossentropy",
        optimizer=keras.optimizers.Adam(lr=1e-4),
        metrics=["acc"],
    )

    return model


def _preprocess_image(original_image):
    """
    Converts a url, a local file, a captured image or a numpy array to
    the proper format for model inference.
    """
    if type(original_image) == str:
        # url
        if "http" in original_image:
            image = PIL.Image.open(io.BytesIO(requests.get(original_image).content))
        # local image path
        else:
            image = PIL.Image.open(original_image)
    elif type(original_image) == numpy.ndarray:
        # already a numpy array
        image = PIL.Image.fromarray((original_image * 255).astype("uint8"))
    else:
        # captured image (ipywidgets.widgets.widget_media.Image)
        image = PIL.Image.open(io.BytesIO(original_image.value))
    # cut to square
    image = PIL.ImageOps.fit(
        image, (min(image.size), min(image.size)), PIL.Image.ANTIALIAS
    )
    # resize to target size
    image.thumbnail((150, 150), PIL.Image.ANTIALIAS)

    # convert to numpy array, drop alpha channel if present
    return numpy.array(image)[:, :, :3] / 255
