import subprocess
import os
import platform

def run_mutation_tests(filepath: str):
    if platform.system() == "Windows":
        return False, "Mutation testing is not supported on Windows."

    try:
        result = subprocess.run(
            ["mutmut", "run", "--paths-to-mutate", filepath],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=30,
            text=True
        )
        output = result.stdout
        success = "THE END" in output or "No surviving mutants" in output
        return success, output
    except Exception as e:
        return False, str(e)
