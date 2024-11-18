from enum import Enum
import json

class Emotions(Enum):
    HAPPY = 'happy'
    SAD = 'sad'
    ANGRY = 'angry'
    SURPRISED = 'surprised'
    DISGUSTED = 'disgusted'
    SCARED = 'scared'
    NEUTRAL = 'neutral'

class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.value
        return json.JSONEncoder.default(self, obj)
