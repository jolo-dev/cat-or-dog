import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import warnings  # noqa: E402

warnings.filterwarnings("ignore")


def predict(image):
    from model.utils import predict

    return predict(image)
