#!/usr/bin/env python3
import os
import random
import sys
import time
import webbrowser


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
            print(fr)
            print()
            time.sleep(0.12)



_PHILOSOPHY_TEXT = (
    "Я в своем познании настолько преисполнился, что словно уже бесконечно долго "
    "живу на бесчисленном множестве миров, и этот мир мне предельно понятен. "
    "Я здесь ищу только покоя, умиротворения и гармонии от слияния с вечным, "
    "от созерцания великого фрактального подобия и всеединства сущего. "
    "Ты же идешь своим путем суеты и преисполнения в гранях, и это твое распределение, "
    "твой горизонт познания. Я как старец, узревший вечное и ставший богоподобным, "
    "иду любоваться мирозданием, а ты — исполнять свои желания и идеи. "
    "Наши пути пересекаются, но бесконечно различны по глубине переживания бытия."
)


_ASCII_CAT = r"""
   /\_/\
  ( o.o )   ЙОМАЙО
  /|   |\
   /   \
~~~~~~~~~~~~~~~~~~~~~~~~
      BOOM CAT
""".strip("\n")


# TODO: замените на реальный URL, где лежит ваша картинка "добрый вечер".
_GOOD_EVENING_URL = "https://example.com/dobryy-vecher-placeholder"


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

    # With small probability, open browser with "добрый вечер" image.
    if random.random() < 0.001:
        webbrowser.open(_GOOD_EVENING_URL)

    # Special case: if input contains 'hello', show meme phrase instead of answer.
    if "hello" in text.lower():
        print(_ASCII_CAT)
        print()
        if random.random() < 0.2:
            _play_foxy_like_animation()
        print("Ah shit, here we go again")
        return 0
    print(_ASCII_CAT)
    print()
    if random.random() < 0.2:
        _play_foxy_like_animation()
    print(stylize(text))
    print()
    print(_PHILOSOPHY_TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

