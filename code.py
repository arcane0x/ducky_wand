# usb rubber ducky using pico

import time
import os
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

# 🔑 Key mappings
KEY_MAP = {
    "CTRL": Keycode.CONTROL,
    "CONTROL": Keycode.CONTROL,
    "SHIFT": Keycode.SHIFT,
    "ALT": Keycode.ALT,
    "GUI": Keycode.WINDOWS,
    "WINDOWS": Keycode.WINDOWS,
    "ENTER": Keycode.ENTER,
    "ESC": Keycode.ESCAPE,
    "ESCAPE": Keycode.ESCAPE,
    "TAB": Keycode.TAB,
    "SPACE": Keycode.SPACEBAR,
    "BACKSPACE": Keycode.BACKSPACE,
    "DELETE": Keycode.DELETE,
    "UP": Keycode.UP_ARROW,
    "DOWN": Keycode.DOWN_ARROW,
    "LEFT": Keycode.LEFT_ARROW,
    "RIGHT": Keycode.RIGHT_ARROW,
    "HOME": Keycode.HOME,
    "END": Keycode.END,
    "PAGEUP": Keycode.PAGE_UP,
    "PAGEDOWN": Keycode.PAGE_DOWN,
    "CAPSLOCK": Keycode.CAPS_LOCK,
    "PRINTSCREEN": Keycode.PRINT_SCREEN,
    "PAUSE": Keycode.PAUSE,
    "INSERT": Keycode.INSERT,
    "NUMLOCK": Keycode.KEYPAD_NUMLOCK,
    "MENU": Keycode.APPLICATION,
    "F1": Keycode.F1, "F2": Keycode.F2, "F3": Keycode.F3,
    "F4": Keycode.F4, "F5": Keycode.F5, "F6": Keycode.F6,
    "F7": Keycode.F7, "F8": Keycode.F8, "F9": Keycode.F9,
    "F10": Keycode.F10, "F11": Keycode.F11, "F12": Keycode.F12,
    "0": Keycode.ZERO, "1": Keycode.ONE, "2": Keycode.TWO,
    "3": Keycode.THREE, "4": Keycode.FOUR, "5": Keycode.FIVE,
    "6": Keycode.SIX, "7": Keycode.SEVEN, "8": Keycode.EIGHT,
    "9": Keycode.NINE
}

def get_keycode(part):
    part = part.upper()
    if part in KEY_MAP:
        return KEY_MAP[part]
    elif len(part) == 1 and part.isalpha():
        return getattr(Keycode, part.upper(), None)
    return None

def press_keys(line):
    keys = line.split()
    combo = [get_keycode(k) for k in keys if get_keycode(k)]
    if combo:
        keyboard.send(*combo)
        time.sleep(0.1)

def send_char(c):
    if "a" <= c <= "z":
        # Lowercase letter: no shift
        keyboard.press(getattr(Keycode, c.upper()))
    elif "A" <= c <= "Z":
        # Uppercase letter: hold shift
        keyboard.press(Keycode.SHIFT, getattr(Keycode, c))
    elif "0" <= c <= "9":
        keyboard.press(getattr(Keycode, c))
    elif c == " ":
        keyboard.press(Keycode.SPACEBAR)
    elif c == ".":
        keyboard.press(Keycode.PERIOD)
    elif c == ",":
        keyboard.press(Keycode.COMMA)
    elif c == "/":
        keyboard.press(Keycode.FORWARD_SLASH)
    elif c == "!":
        keyboard.press(Keycode.SHIFT, Keycode.ONE)
    elif c == "@":
        keyboard.press(Keycode.SHIFT, Keycode.TWO)
    elif c == "#":
        keyboard.press(Keycode.SHIFT, Keycode.THREE)
    elif c == "$":
        keyboard.press(Keycode.SHIFT, Keycode.FOUR)
    elif c == "%":
        keyboard.press(Keycode.SHIFT, Keycode.FIVE)
    elif c == "^":
        keyboard.press(Keycode.SHIFT, Keycode.SIX)
    elif c == "&":
        keyboard.press(Keycode.SHIFT, Keycode.SEVEN)
    elif c == "*":
        keyboard.press(Keycode.SHIFT, Keycode.EIGHT)
    elif c == "(":
        keyboard.press(Keycode.SHIFT, Keycode.NINE)
    elif c == ")":
        keyboard.press(Keycode.SHIFT, Keycode.ZERO)
    elif c == "-":
        keyboard.press(Keycode.MINUS)
    elif c == "_":
        keyboard.press(Keycode.SHIFT, Keycode.MINUS)
    elif c == "=":
        keyboard.press(Keycode.EQUALS)
    elif c == "+":
        keyboard.press(Keycode.SHIFT, Keycode.EQUALS)
    elif c == "[":
        keyboard.press(Keycode.LEFT_BRACKET)
    elif c == "{":
        keyboard.press(Keycode.SHIFT, Keycode.LEFT_BRACKET)
    elif c == "]":
        keyboard.press(Keycode.RIGHT_BRACKET)
    elif c == "}":
        keyboard.press(Keycode.SHIFT, Keycode.RIGHT_BRACKET)
    elif c == "\\":
        keyboard.press(Keycode.BACKSLASH)
    elif c == "|":
        keyboard.press(Keycode.SHIFT, Keycode.BACKSLASH)
    elif c == ";":
        keyboard.press(Keycode.SEMICOLON)
    elif c == ":":
        keyboard.press(Keycode.SHIFT, Keycode.SEMICOLON)
    elif c == "'":
        keyboard.press(Keycode.QUOTE)
    elif c == '"':
        keyboard.press(Keycode.SHIFT, Keycode.QUOTE)
    elif c == "`":
        keyboard.press(Keycode.GRAVE_ACCENT)
    elif c == "~":
        keyboard.press(Keycode.SHIFT, Keycode.GRAVE_ACCENT)
    elif c == "<":
        keyboard.press(Keycode.SHIFT, Keycode.COMMA)
    elif c == ">":
        keyboard.press(Keycode.SHIFT, Keycode.PERIOD)
    elif c == "?":
        keyboard.press(Keycode.SHIFT, Keycode.FORWARD_SLASH)
    else:
        print(f"⚠️ Unsupported character: {c}")
        return
    keyboard.release_all()
    time.sleep(0.05)

def cast_spell(spell_file):
    with open("/spells/" + spell_file) as f:
        for line in f:
            line = line.strip()
            if line.startswith("REM") or line == "":
                continue
            elif line.startswith("DELAY"):
                delay_ms = int(line.split()[1])
                time.sleep(delay_ms / 1000)
            elif line.startswith("STRING"):
                text = line[7:]
                for c in text:
                    send_char(c)
                time.sleep(0.1)
            else:
                press_keys(line)

# ⏳ Delay before starting to allow OS ready
time.sleep(3)

# 🔁 Run all spells found in /spells/
for spell_file in os.listdir("/spells"):
    if spell_file.endswith(".txt"):
        cast_spell(spell_file)
        time.sleep(1)
