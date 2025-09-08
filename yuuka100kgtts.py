#!/usr/bin/env python3
"""
Simple Tkinter + pyttsx3 TTS GUI (with Fix 2: manual event loop)
--------------------------------------------------
Dependencies:
    pip install pyttsx3
"""

import tkinter as tk
from tkinter import ttk, messagebox
import pyttsx3
import threading

# Init engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
speaking = False
thread = None

def speak(text):
    global speaking
    try:
        # Apply settings
        engine.setProperty("rate", rate_scale.get())
        engine.setProperty("volume", volume_scale.get() / 100.0)
        selected_voice = voice_combo.current()
        engine.setProperty("voice", voices[selected_voice].id)

        engine.say(text)
        engine.startLoop(False)   # start loop, non-blocking
        while engine.isBusy():    # let it speak fully
            engine.iterate()
        engine.endLoop()
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        speaking = False

def start_speaking():
    global speaking, thread
    if speaking:
        return
    text = text_box.get("1.0", "end").strip()
    if not text:
        messagebox.showwarning("No text", "Please enter some text to speak.")
        return
    speaking = True
    thread = threading.Thread(target=speak, args=(text,), daemon=True)
    thread.start()

def stop_speaking():
    global speaking
    if speaking:
        engine.stop()
        speaking = False

# Tkinter UI
root = tk.Tk()
root.title("Simple TTS")
root.geometry("500x350")

tk.Label(root, text="Enter text:").pack(anchor="w", padx=10, pady=(10, 0))
text_box = tk.Text(root, wrap="word", height=8)
text_box.pack(fill="both", expand=True, padx=10, pady=5)

control_frame = tk.Frame(root)
control_frame.pack(fill="x", padx=10, pady=5)

tk.Label(control_frame, text="Voice:").grid(row=0, column=0, sticky="w")
voice_combo = ttk.Combobox(
    control_frame,
    values=[v.name for v in voices],
    state="readonly",
    width=20
)
voice_combo.grid(row=0, column=1, padx=5, sticky="ew")
voice_combo.current(0)

tk.Label(control_frame, text="Rate:").grid(row=1, column=0, sticky="w")
rate_scale = tk.Scale(control_frame, from_=100, to=300, orient="horizontal")
rate_scale.set(engine.getProperty("rate"))
rate_scale.grid(row=1, column=1, sticky="ew")

tk.Label(control_frame, text="Volume:").grid(row=2, column=0, sticky="w")
volume_scale = tk.Scale(control_frame, from_=0, to=100, orient="horizontal")
volume_scale.set(int(engine.getProperty("volume") * 100))
volume_scale.grid(row=2, column=1, sticky="ew")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Speak", command=start_speaking).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Stop", command=stop_speaking).grid(row=0, column=1, padx=5)

root.mainloop()
