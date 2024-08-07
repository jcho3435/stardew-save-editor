import pytest
import os
import sys
import subprocess
import time
import webbrowser

# Add the root directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def run_app():
    return subprocess.Popen([sys.executable, 'runner.py'])

def cleanup():
    import functions.program_lock as program_lock
    program_lock.clean_up()

def test_base():
    app_process = run_app()

    # Check if the process is running
    assert app_process.poll() is None

    # Ensure the application process is still running
    assert app_process.poll() is None

    time.sleep(2)
    # Terminate the process
    app_process.terminate()
    app_process.wait(timeout=5)

    # Ensure the process has terminated
    assert app_process.poll() is not None

    cleanup()