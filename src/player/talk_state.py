import state


class Talk(state.State):
    def __init__(self, player, state_machine, world) -> None:
        super().__init__()

        self.name = "talk"
        self.player = player
        self.state_machine = state_machine
        self.world = world

    def enter(self, enter_params=None):
        self.player.sprite.set_state("talk")

    def exit(self):
        pass

    def handle_input(self, inputs):
        if inputs.tapped("button_idle"):
            self.state_machine.change("idle")
            return

    def update(self):
        pass

    def draw(self):
        pass
