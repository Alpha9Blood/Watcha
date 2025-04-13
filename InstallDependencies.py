import sys
import subprocess

def install_dependencies():
    print("Installing dependencies...")
    dependencies = [
        "tkinter",  # GUI library
        "tktooltip", # Tooltip library
        "pillow", # Image library
        "requests" # HTTP library
    ]

    for dependency in dependencies:
        try:
            print(f"Installing {dependency}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", dependency])
            print(f"{dependency} installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Failed to install {dependency}. Please check your internet connection or the package name.")

if __name__ == "__main__":
    install_dependencies()