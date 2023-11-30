import os, random, subprocess
from utils.constants import HOME
from libqtile.command import lazy
from settings import keymap


def run_script(command: str):
    subprocess.call([HOME + command])


def random_wallpaper():
    wallpaper_directory = f"{HOME}/Pictures/wallpapers/"

    image_formats = (".png", ".jpg", ".jpeg")
    image_files = [
        file
        for file in os.listdir(wallpaper_directory)
        if file.lower().endswith(image_formats)
    ]

    if not image_files:
        print("No image found")
        return

    selected_image = random.choice(image_files)
    image_path = os.path.join(wallpaper_directory, selected_image)
    os.system(f"feh --bg-fill {image_path}")
    print(f"The wallpaper has been changed {image_path}")


def send_window_to_group(window: object, workspace: int):
    group = keymap.workspaces_keybindings[workspace]
    window.togroup(group)
    lazy.group[group].toscreen()