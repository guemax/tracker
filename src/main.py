import os


def create_tracker_file(filename: str) -> None:
    with open(filename, "w") as f:
        pass


def file_exists(filename: str) -> bool:
    return os.path.isfile(filename)


def init():
    filename = "tracker.csv"
    if file_exists(filename):
        return
    else:
        create_tracker_file(filename)


if __name__ == "__main__":
    init()
