# angkor/__init__.py
import subprocess

def run():
    print("Starting AngkorCMS server on port 7000...")
    subprocess.run(["python", "app.py"])
