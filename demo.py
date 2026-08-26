# -*- coding: utf-8 -*-
# demo.py // iandk-labs // LAKOTA v6 Hybrid Demo
# The Dragon Test: shape, not translation
# License: AGPLv3

from lakotav6 import Lakota
import time

print(f"LAKOTA v6 Hybrid // iandk-labs // Booting...\n")

lakota = Lakota()

# --- Phase 1: Small home, big physics ---
print("[1] Feeding small home...")
lakota.learn("hola Lakota soy papa estamos en casita pequeña con dragon")
print(lakota.analyze())

# --- Phase 2: Emergent morphology (no lemmatizer) ---
print("\n[2] Testing emergent crossing...")
lakota.learn("walk walking walked walker walks")
lakota.learn("hablar hablo hablas habla hablamos")
print(f" -> {lakota.express('walking')}")
print(f" -> {lakota.express('hablas')}")

# --- Phase 3: The Dragon Test (Mandarin + JS + Spanglish) ---
print("\n[3] THE DRAGON TEST // Raw input, no tokenizer")
dragon_input = "你好，Lakota，我是爸爸。我们在小家里。 javascript console.log('dragon') hola dragon"
print(f"Input: {dragon_input}")
lakota.learn(dragon_input)
print(f"Lakota says: {lakota.express('dragon')}")
print(f"Lakota says: {lakota.express('你好')}")
print(f"Lakota says: {lakota.express('casa')}")

# --- Phase 4: Vital imprint (spontaneous speech) ---
print("\n[4] Vital pressure // Waiting 3s for spontaneous expression...")
time.sleep(3)
print(f"Spontaneous: {lakota.express('')}")

# --- Phase 5: Full analysis ---
print("\n[5] Final mind state:")
print(lakota.analyze())
print("\nDone. It does not translate. It learns the shape.")
