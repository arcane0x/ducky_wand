# 🧙 DuckyWand: Arcane USB Spellcaster

A **USB Rubber Ducky** disguised as a magical device that casts “spells” (payloads) when plugged into a computer.
Each spell is a file stored on the Pico that executes scripted keystrokes — like a wizard casting *Notepad Summon* or *Browser Blaze*.

---

## 🔧 What You'll Need

* Raspberry Pi Pico
* Micro USB Cable
* Computer with Thonny or VS Code
* CircuitPython installed on the Pico

---

## 🧪 Step-by-Step Setup

### 🔁 Step 1: Install CircuitPython on Pico

1. Go to 👉 [CircuitPython for Raspberry Pi Pico](https://circuitpython.org/board/raspberry_pi_pico/)
2. Download the `.uf2` file.
3. Hold **BOOTSEL**, then plug in Pico → it shows up as `RPI-RP2`.
4. Drag the `.uf2` file → Pico reboots and shows as `CIRCUITPY`.

---

### 📦 Step 2: Add HID Library

1. Download the **CircuitPython Library Bundle** from Adafruit.
2. From the unzipped `lib` folder, copy:

```
adafruit_hid/
```

→ into `CIRCUITPY/lib/`

---

### 🗂️ Step 3: Organize Your “Spell” Payloads

Folder structure on Pico:

```
CIRCUITPY/
├── code.py                ← Main logic
├── lib/
│   └── adafruit_hid/
├── spells/
│   ├── notepad_summon.txt
│   ├── browser_blaze.txt
│   └── terminal_whisper.txt
```

Each `.txt` file is a keystroke payload.

Example: `notepad_summon.txt`

```
GUI r
DELAY 500
STRING notepad
ENTER
DELAY 500
STRING Hello, I am your enchanted ducky.
ENTER
```

---

### 🧠 Step 4: Add DuckyScript Parser (`code.py`)

```
# Add the code.py file in the root folder 

---

## 🪄 Example Spells

### ✨ Notepad Summon (`notepad_summon.txt`)

```
GUI r
DELAY 300
STRING notepad
ENTER
DELAY 400
STRING ✨ I am your digital familiar. ✨
ENTER
```

---

### 🔥 Browser Blaze (`browser_blaze.txt`)

```
GUI r
DELAY 300
STRING chrome
ENTER
DELAY 800
STRING https://chat.openai.com
ENTER
```

---

### 🌌 Terminal Whisper (`terminal_whisper.txt`)

```
GUI r
DELAY 300
STRING cmd
ENTER
DELAY 400
STRING echo Magic flows through circuits...
ENTER
```

---

## 🧙 Usage

1. Plug the Pico into a target computer.
2. After 3 seconds, it automatically starts casting spells from `/spells/`.
3. Each spell executes in order with a delay between them.

Congratulations — you now wield the **DuckyWand**, a true *Arcane USB Spellcaster*!
