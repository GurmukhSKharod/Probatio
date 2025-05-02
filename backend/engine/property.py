import subprocess
import tempfile
import os

def run_property_tests(filepath: str):
    test_code = f"""
from hypothesis import given, strategies as st
import {os.path.splitext(os.path.basename(filepath))[0]}

@given(st.integers(), st.integers())
def test_addition_commutes(x, y):
    assert x + y == y + x
"""

    with tempfile.NamedTemporaryFile(delete=False, suffix="_property_test.py", mode="w") as tf:
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
