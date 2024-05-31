"""Copied from https://github.com/pre-commit/pre-commit/blob/d827e9aa7211456965bf7d16f06ac6a85b0f2984/pre_commit/color.py"""

import os
import sys


terminal_supports_color = True

RED = "\033[41m"
GREEN = "\033[42m"
BLUE = "\033[44m"
YELLOW = "\033[43;30m"
TURQUOISE = "\033[46;30m"
BOLD = "\033[1m"
SUBTLE = "\033[2m"
NORMAL = "\033[m"
SUCCESS = "\033[32m"
INFO = "\033[34m"
ERROR = "\033[31m"


def format_color(text: str, color: str, use_color_setting: bool) -> str:
    """Format text with color.

    Args:
        text - Text to be formatted with color if `use_color`
        color - The color start string
        use_color_setting - Whether or not to color
    """
    if use_color_setting:
        return f"{color}{text}{NORMAL}"
    else:
        return text


COLOR_CHOICES = ("auto", "always", "never")


def use_color(setting: str) -> bool:
    """Choose whether to use color based on the command argument.

    Args:
        setting - Either `auto`, `always`, or `never`
    """
    if setting not in COLOR_CHOICES:
        raise ValueError(setting)

    return setting == "always" or (
        setting == "auto"
        and sys.stderr.isatty()
        and terminal_supports_color
        and os.getenv("TERM") != "dumb"
    )
