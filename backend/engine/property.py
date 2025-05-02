import subprocess
import tempfile
import os
import ast
import textwrap

def extract_functions(filepath):
    """Parses the file and returns a list of function names."""
    with open(filepath, "r") as f:
        tree = ast.parse(f.read())
    return [node.name for node in tree.body if isinstance(node, ast.FunctionDef)]

def generate_property_tests(filepath, functions):
    module = os.path.splitext(os.path.basename(filepath))[0]
    props = []

    # Integer operations
    if "add" in functions:
        props.append(f"""
@given(st.integers(), st.integers())
def test_add_commutative(x, y):
    assert {module}.add(x, y) == {module}.add(y, x)
""")
    if "subtract" in functions:
        props.append(f"""
@given(st.integers())
def test_subtract_identity(x):
    assert {module}.subtract(x, x) == 0
""")
    if "multiply" in functions:
        props.append(f"""
@given(st.integers())
def test_multiply_zero(x):
    assert {module}.multiply(x, 0) == 0
""")

    # String operations
    if "concat" in functions:
        props.append(f"""
@given(st.text())
def test_concat_identity(s):
    assert {module}.concat(s, "") == s
""")

    # List operations
    if "reverse" in functions:
        props.append(f"""
@given(st.lists(st.integers()))
def test_reverse_involution(lst):
    assert {module}.reverse({module}.reverse(lst)) == lst
""")
    if "sort" in functions:
        props.append(f"""
@given(st.lists(st.integers()))
def test_sort_order(lst):
    sorted_lst = {module}.sort(lst)
    assert sorted_lst == sorted(lst)
""")

    return "\n".join(props)

def run_property_tests(filepath: str):
    module = os.path.splitext(os.path.basename(filepath))[0]
    functions = extract_functions(filepath)
    if not functions:
        return False, "No functions found to test."

    header = f"""
from hypothesis import given, strategies as st
import {module}
"""

    body = generate_property_tests(filepath, functions)
    full_code = header + "\n" + textwrap.dedent(body)

    with tempfile.NamedTemporaryFile(delete=False, suffix="_property_test.py", mode="w") as tf:
        tf.write(full_code)
        test_file = tf.name

    try:
        result = subprocess.run(
            ["pytest", "-v", "--tb=short", test_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=15,
            text=True
        )
        output = result.stdout
        success = result.returncode == 0

        test_lines = [line for line in output.splitlines() if "::" in line]
        falsified = any("Falsifying" in line for line in output.splitlines())

        summary = [
            "=== PROPERTY TEST RESULT ===",
            f"Functions found: {', '.join(functions)}",
            f"Total tests generated: {len(test_lines)}",
            f"Failures: {'Yes' if not success else 'No'}",
            f"Falsifying case detected: {'Yes' if falsified else 'No'}",
            "",
            "Full Output:",
            output
        ]

        return success, "\n".join(summary)

    except Exception as e:
        return False, f"Property test error: {str(e)}"
    finally:
        os.remove(test_file)
