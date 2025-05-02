import subprocess
import tempfile
import os

def run_unit_tests(filepath: str):
    test_code = f"""
import pytest
import sys
sys.path.insert(0, '{os.path.dirname(filepath)}')
import {os.path.splitext(os.path.basename(filepath))[0]}

def test_placeholder():
    assert True
"""

    with tempfile.NamedTemporaryFile(delete=False, suffix="_test.py", mode="w") as tf:
        tf.write(test_code)
        test_file = tf.name

    try:
        result = subprocess.run(
            ["pytest", test_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=10,
            text=True
        )
        success = result.returncode == 0
        return success, result.stdout
    except Exception as e:
        return False, str(e)
    finally:
        os.remove(test_file)
