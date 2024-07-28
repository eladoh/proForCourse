from keyboard import press, send, release
import keyboard
import time


hotkeys = []
letters = 'abcdefghijklmnopqrstuvwxyz'
for i in range(2):
    for letter in range(26):
        if i == 0:
            hotkeys.append(f"ctrl+{letters[letter]}")
        else:
            hotkeys.append(f"alt+{letters[letter]}")
print(hotkeys)


hotkey_state = False

def handle_event(event):
    global hotkey_state
    if event.event_type == keyboard.KEY_DOWN:
        for hotkey in hotkeys:
            if keyboard.is_pressed(hotkey):
                hotkey_state = True
                key_pressed = hotkey
                print(key_pressed)
                break
        else:
            hotkey_state = False

    if event.event_type == keyboard.KEY_UP and not hotkey_state:
        key_pressed = event.name
        print(key_pressed)

keyboard.hook(handle_event)

keyboard.wait("esc")
