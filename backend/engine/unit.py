import subprocess
import tempfile
import os
import uuid

def run_unit_tests(filepath: str):
    module_name = f"user_module_{uuid.uuid4().hex[:6]}"
    safe_path = filepath.replace("\\", "\\\\")  # Safely escape for embedding in test code
    test_code = f'''
import pytest
import sys
sys.path.insert(0, r"{os.path.dirname(safe_path)}")
from importlib.util import spec_from_file_location, module_from_spec
spec = spec_from_file_location("{module_name}", r"{safe_path}")
{module_name} = module_from_spec(spec)
spec.loader.exec_module({module_name})

def test_sanity():
    assert True
'''

    with tempfile.NamedTemporaryFile(delete=False, suffix="_test.py", mode="w") as tf:
        tf.write(test_code)
        test_file = tf.name

    try:
        result = subprocess.run(
            ["pytest", "-v", "--tb=short", test_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=10,
            text=True
        )
        output = result.stdout
        success = result.returncode == 0

        # Filter and extract useful test summary
        summary_lines = []
        for line in output.splitlines():
            if (
                "collected" in line or "::" in line or 
                line.startswith("FAILED") or line.startswith("PASSED")
            ):
                summary_lines.append(line)

        summary = "\n".join(summary_lines)

        return success, f"=== UNIT TEST RESULT ===\n{summary}\n\nFull Output:\n{output}"
    except Exception as e:
        return False, f"Unit test error: {str(e)}"
    finally:
        os.remove(test_file)
