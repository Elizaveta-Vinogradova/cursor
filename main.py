#!/usr/bin/env python3
import os
import random
import sys
import time


def _build_mapping() -> dict[str, str]:
    # 15 replacements (ASCII letters -> symbols)
    return {
        "a": "∆",
        "b": "■",
        "c": "¢",
        "d": "◊",
        "e": "€",
        "f": "ƒ",
        "g": "ɢ",
        "h": "Ħ",
        "i": "¡",
        "j": "ʝ",
        "k": "Ҡ",
        "l": "Ł",
        "m": "₥",
        "n": "₦",
        "o": "⊙",
    }


def stylize(text: str) -> str:
    mapping = _build_mapping()
    out: list[str] = []
    for ch in text:
        lower = ch.lower()
        repl = mapping.get(lower)
        if repl is None:
            out.append(ch)
            continue

        if ch.isupper():
            out.append(repl.upper())
        else:
            out.append(repl)
    return "".join(out)


def _clear_screen() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        # ANSI clear + home
        print("\x1b[2J\x1b[H", end="")


def _play_foxy_like_animation() -> None:
    # Original ASCII animation (not a copyrighted GIF).
    frames = [
        r"""
      /\_/\ 
     ( o.o )   *tap*
      > ^ < 
    """.strip("\n"),
        r"""
      /\_/\ 
     ( O.O )   *tap tap*
      > ^ < 
    """.strip("\n"),
        r"""
      /\_/\ 
     ( O.O )  yarrr!
     /  ^  \__
    """.strip("\n"),
        r"""
      /\_/\ 
     ( x.x )  ...
      > ^ < 
    """.strip("\n"),
    ]

    for _ in range(2):
        for fr in frames:
            _clear_screen()
            print(fr)
            time.sleep(0.12)
    _clear_screen()


def main(argv: list[str]) -> int:
    # Ensure Unicode output works on Windows consoles with legacy code pages.
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    if len(argv) < 2:
        prog = argv[0] if argv else "main.py"
        print(f"Usage: {prog} <text>")
        print('Example: python main.py "Hello, World!"')
        return 2

    text = " ".join(argv[1:])
    if random.random() < 0.001:
        _play_foxy_like_animation()
    print(stylize(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

