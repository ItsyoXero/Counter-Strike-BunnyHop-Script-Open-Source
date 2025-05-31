import threading
import sys
from time import sleep
from keyboard import is_pressed, add_hotkey
from pymem import Pymem, process
from pystray import Icon, MenuItem as Item, Menu
from PIL import Image, ImageDraw

# Game memory addresses (update if needed)
FORCE_JUMP_ADDRESS = 0x12D048
ON_GROUND_ADDRESS = 0x11FDAB4

class BunnyHop:
    def __init__(self):
        self.enabled = False
        self.running = True
        self.delay_jump = 0.05
        self.active_key = 'space'
        self.game_handle = Pymem('hl.exe')
        self.client_dll = process.module_from_name(
            self.game_handle.process_handle, 'client.dll'
        ).lpBaseOfDll
        self.hw_dll = process.module_from_name(
            self.game_handle.process_handle, 'hw.dll'
        ).lpBaseOfDll

    def on_ground(self) -> bool:
        return self.game_handle.read_int(self.hw_dll + ON_GROUND_ADDRESS) == 1

    def jump(self):
        if self.on_ground():
            self.game_handle.write_int(self.client_dll + FORCE_JUMP_ADDRESS, 5)
            sleep(self.delay_jump)
            self.game_handle.write_int(self.client_dll + FORCE_JUMP_ADDRESS, 4)

    def toggle(self, from_hotkey=False):
        self.enabled = not self.enabled
        source = "F1" if from_hotkey else "Tray"
        print(f"[{source}] BunnyHop {'ENABLED' if self.enabled else 'DISABLED'}")

    def stop(self, icon):
        print("[Tray] Exiting...")
        self.running = False
        icon.stop()
        sys.exit()

    def loop(self):
        while self.running:
            if self.enabled and is_pressed(self.active_key):
                self.jump()
            sleep(0.001)

def create_icon(bhop: BunnyHop):
    # Create a small red/green icon
    def create_image(enabled):
        color = "green" if enabled else "red"
        img = Image.new("RGB", (64, 64), color)
        draw = ImageDraw.Draw(img)
        draw.ellipse((16, 16, 48, 48), fill="white")
        return img

    def update_icon(icon):
        icon.icon = create_image(bhop.enabled)

    icon = Icon("BunnyHop")
    icon.menu = Menu(
        Item(lambda item: f"{'✔' if bhop.enabled else '❌'} AutoHop", lambda: [bhop.toggle(), update_icon(icon)]),
        Item("Exit", lambda: bhop.stop(icon))
    )
    icon.icon = create_image(False)
    threading.Thread(target=icon.run, daemon=True).start()

def main():
    bhop = BunnyHop()
    add_hotkey('F1', lambda: bhop.toggle(from_hotkey=True))
    create_icon(bhop)
    print("[BunnyHop] Running in background. Use tray icon or press F1 to toggle.")
    bhop.loop()

if __name__ == '__main__':
    main()
