from typing import TYPE_CHECKING

from nonebot import get_plugin_config
from nonebot.utils import resolve_dot_notation
from pydantic import BaseModel

if TYPE_CHECKING:
    from pydantic import field_validator  # V2
else:
    from nonebot.compat import field_validator


class PluginConfig(BaseModel):
    enable_scheduler: bool = True
    scene_color_start: tuple[int, int, int] = (29, 113, 48)  # 1d7130
    scene_color_end: tuple[int, int, int] = (52, 208, 88)  # 34d058
    user_color_fn: str | None = None

    @field_validator("scene_color_start", "scene_color_end", mode="after")
    @staticmethod
    def validate_color(value: tuple[int, int, int]) -> tuple[int, int, int]:
        if not all(0 <= c <= 255 for c in value):
            raise ValueError("RGB values must be in the range 0-255.")
        return value

    @field_validator("user_color_fn", mode="after")
    @staticmethod
    def validate_user_color_fn(value: str | None) -> str | None:
        if value is None:
            return None

        if ":" not in value:
            raise ValueError("user_color_fn must be in the format 'module:attribute'.")

        try:
            obj = resolve_dot_notation(value, "")
        except (ImportError, AttributeError) as e:
            raise ValueError(f"Invalid user_color_fn: {value}") from e

        if not callable(obj):
            raise TypeError(f"user_color_fn must be callable: {value}")

        return value


class Config(BaseModel):
    talk_stats: PluginConfig = PluginConfig()


config = get_plugin_config(Config).talk_stats
