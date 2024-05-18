from enum import Enum

import actor


class ActorType(Enum):
    player = 0
    npc = 1


defs = {
    "player": {
        "create": player.player_actor.Player,
        "type": ActorType.player,
        "states": {
            "idle": {"frames": ((224, 240), (240, 240)), "frame_speed": 0.5},
            "run": {"frames": ((224, 224), (240, 224)), "frame_speed": 0.1},
            "jump": {
                "frames": ((224, 192), (240, 192)),
                "frame_speed": 0.15,
                "loop": False,
            },
            "fall": {"frames": ((240, 176),), "frame_speed": 0.15, "loop": False},
            "climb": {
                "frames": ((240, 160),),
                "frame_speed": 0.15,
            },
            "talk": {
                "frames": ((224, 240), (240, 240)),
                "frame_speed": 0.15,
            },
        },
        "size": (16, 16),
        "hitbox": (4, 2, 8, 14),
    },
    "old_lady": {
        "create": actor.Actor,
        "type": ActorType.npc,
        "states": {
            "idle": {"frames": ((192, 240), (208, 240)), "frame_speed": 1},
        },
        "size": (16, 16),
        "hitbox": (4, 2, 8, 14),
    },
}
