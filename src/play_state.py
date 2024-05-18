import state


class PlayState(state.State):
    def __init__(self):
        super().__init__()

    def enter(self, enter_params=None):
        pass

    def exit(self):
        pass

    def handle_input(self, inputs):
        pass

    def update(self):
        pass

    def draw(self):
        pass
