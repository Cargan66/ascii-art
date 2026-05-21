import random
import sys
import pyfiglet
from colorama import init, Fore, Style

init(autoreset=True)

COLORS = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE,
    Fore.MAGENTA, Fore.CYAN, Fore.WHITE,
]

FONTS = [
    "big", "block", "bubble", "digital", "isometric1",
    "larry3d", "lean", "mini", "ogre", "puffy",
    "shadow", "slant", "small", "speed", "standard",
    "star_wars", "stop", "thin",
]

MENU = f"""
{Fore.CYAN}╔══════════════════════════════════╗
║       ASCII Art Generator        ║
╚══════════════════════════════════╝{Style.RESET_ALL}
Commands:
  {Fore.YELLOW}fonts{Style.RESET_ALL}      — list available fonts
  {Fore.YELLOW}font <name>{Style.RESET_ALL} — set font  (e.g. font slant)
  {Fore.YELLOW}color{Style.RESET_ALL}      — cycle through colors
  {Fore.YELLOW}rainbow{Style.RESET_ALL}    — toggle rainbow mode
  {Fore.YELLOW}random{Style.RESET_ALL}     — use a random font each time
  {Fore.YELLOW}quit{Style.RESET_ALL}       — exit
"""


def render(text: str, font: str, color: str, rainbow: bool) -> str:
    try:
        art = pyfiglet.figlet_format(text, font=font)
    except pyfiglet.FontNotFound:
        art = pyfiglet.figlet_format(text, font="standard")

    if not rainbow:
        return color + art + Style.RESET_ALL

    lines = art.splitlines()
    colored = []
    for i, line in enumerate(lines):
        colored.append(COLORS[i % len(COLORS)] + line)
    return "\n".join(colored) + Style.RESET_ALL


def main():
    print(MENU)

    font = "slant"
    color_index = 2  # yellow
    rainbow = False
    use_random_font = False

    while True:
        try:
            raw = input(f"{Fore.GREEN}>{Style.RESET_ALL} ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Fore.CYAN}bye!{Style.RESET_ALL}")
            sys.exit(0)

        if not raw:
            continue

        lower = raw.lower()

        if lower == "quit":
            print(f"{Fore.CYAN}bye!{Style.RESET_ALL}")
            sys.exit(0)

        elif lower == "fonts":
            cols = 4
            rows = [FONTS[i:i+cols] for i in range(0, len(FONTS), cols)]
            print()
            for row in rows:
                print("  " + "  ".join(f"{Fore.YELLOW}{f:<14}{Style.RESET_ALL}" for f in row))
            print()

        elif lower.startswith("font "):
            name = raw[5:].strip()
            if name in FONTS:
                font = name
                use_random_font = False
                print(f"Font set to {Fore.YELLOW}{font}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Unknown font. Type 'fonts' to see options.{Style.RESET_ALL}")

        elif lower == "color":
            color_index = (color_index + 1) % len(COLORS)
            names = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
            print(f"Color set to {COLORS[color_index]}{names[color_index]}{Style.RESET_ALL}")

        elif lower == "rainbow":
            rainbow = not rainbow
            state = "ON" if rainbow else "OFF"
            print(f"Rainbow mode {Fore.MAGENTA}{state}{Style.RESET_ALL}")

        elif lower == "random":
            use_random_font = not use_random_font
            state = "ON" if use_random_font else "OFF"
            print(f"Random font mode {Fore.YELLOW}{state}{Style.RESET_ALL}")

        else:
            chosen_font = random.choice(FONTS) if use_random_font else font
            print()
            print(render(raw, chosen_font, COLORS[color_index], rainbow))
            if use_random_font:
                print(f"  {Fore.CYAN}(font: {chosen_font}){Style.RESET_ALL}")
            print()


if __name__ == "__main__":
    main()
