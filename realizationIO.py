from abc import ABC, abstractmethod


class IO(ABC):
    @abstractmethod
    def print(sefl, *args, **kwargs):
        pass

    @abstractmethod
    def input(sefl, *args, **kwargs):
        pass


class CLI(IO):

    def print(sefl, *args, **kwargs):
        print(*args, **kwargs)

    def input(sefl, *args, **kwargs):
        return input(*args, **kwargs)

cli = CLI()
