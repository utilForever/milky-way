from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def enter(self, enter_params=None):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def handle_input(self, inputs):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass
