import os


def init():
    if os.path.isfile("tracker.csv"):
        return
    else:
        # TODO: Create file
        pass


if __name__ == "__main__":
    init()
