import os


class Constants(object):
    """
    A helper class with broad used constants.
    """

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    WINDOW_SIZE = str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT)

    ROOT_IMAGE_PATH, tail = os.path.split(os.path.abspath(__file__).replace("\\", "/"))
    PATH_CARD = ROOT_IMAGE_PATH + "/card_images/"
    PATH_BACK_CARD = PATH_CARD + "/back1.png"
    ICON_PATH = ROOT_IMAGE_PATH + "/icons/ic_memory1.png"
    RECORDS_FILE_PATH = ROOT_IMAGE_PATH + "/game_records.csv"
