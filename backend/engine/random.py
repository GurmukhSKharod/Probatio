import ast
import random
import string
import tempfile
import subprocess
import os
import shutil

# === Input Generators ===

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_int():
    return random.randint(-1000, 1000)

def random_float():
    return round(random.uniform(-9999, 9999), 2)

def random_list():
    return [random_int() for _ in range(random.randint(2, 5))]

def random_dict():
    return {random_string(4): random_int() for _ in range(random.randint(2, 4))}

def random_bool():
    return random.choice([True, False])

def guess_type_data():
    return random.choice([
        random_string(),
        random_int(),
        random_float(),
        random_list(),
        random_dict(),
        random_bool()
    ])

# === Parse function signatures from uploaded file ===

def extract_function_signatures(filepath):
    with open(filepath, 'r') as f:
        node = ast.parse(f.read())

    func_map = {}
    for item in node.body:
        if isinstance(item, ast.FunctionDef):
            name = item.name
            params = [arg.arg for arg in item.args.args]
            func_map[name] = len(params)
    return func_map

# === Generate test script ===

def create_random_test_script(module_name: str, func_map: dict, module_dir: str):
    script = f"""
import sys
import importlib
sys.path.insert(0, r"{module_dir}")
mod = importlib.import_module("{module_name}")
results = []
stats = {{}}
"""

    for fname, arg_count in func_map.items():
        script += f'stats["{fname}"] = {{"pass": 0, "fail": 0}}\n'
        for _ in range(4):  # Number of trials per function
            inputs = [repr(guess_type_data()) for _ in range(arg_count)]
            script += f"""
try:
    fn = getattr(mod, "{fname}")
    if callable(fn):
        result = fn({", ".join(inputs)})
        results.append(("PASS", "{fname}", {inputs}, result))
        stats["{fname}"]["pass"] += 1
except Exception as e:
    results.append(("FAIL", "{fname}", {inputs}, str(e)))
    stats["{fname}"]["fail"] += 1
"""

    script += """
print("Function Summary:")
for name, s in stats.items():
    print(f"{name}: {s['pass']} PASS, {s['fail']} FAIL")
print("\\nDetails:")
for r in results:
    print(" | ".join(map(str, r)))
"""
    return script

# === Runner ===

def run_random_tests(filepath: str):
    module_name = "testmod"
    temp_dir = tempfile.mkdtemp()
    mod_path = os.path.join(temp_dir, f"{module_name}.py")
    shutil.copy(filepath, mod_path)

    try:
        func_map = extract_function_signatures(filepath)
        if not func_map:
            return False, "No callable functions found for testing."

        script = create_random_test_script(module_name, func_map, temp_dir)

        with tempfile.NamedTemporaryFile(delete=False, suffix="_rtest.py", mode="w") as tf:
            tf.write(script)
            test_file = tf.name

        result = subprocess.run(
            ["python", test_file],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=10,
            text=True
        )

        output = result.stdout
        success = "FAIL" not in output
        return success, "=== RANDOM TEST RESULT ===\n" + output

    except Exception as e:
        return False, f"Random test execution error: {str(e)}"

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
