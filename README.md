# ASCII Art Generator

A small interactive command-line tool that turns text into colorful ASCII art using [pyfiglet](https://github.com/pwaller/pyfiglet) and [colorama](https://github.com/tartley/colorama).

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python ascii_art.py
```

You'll get an interactive prompt. Type any text to render it as ASCII art.

## Commands

| Command       | What it does                                  |
| ------------- | --------------------------------------------- |
| `fonts`       | List all available fonts                      |
| `font <name>` | Set the font (e.g. `font slant`)              |
| `color`       | Cycle through the available colors            |
| `rainbow`     | Toggle rainbow mode (each line a new color)   |
| `random`      | Toggle a random font for each rendered text   |
| `quit`        | Exit the program                              |

Anything else you type is rendered as ASCII art with the current font and color.

## Example

```
> hello
   __         ____
  / /_  ___  / / /___
 / __ \/ _ \/ / / __ \
/ / / /  __/ / / /_/ /
\_/ /_/\___/_/_/\____/
```
