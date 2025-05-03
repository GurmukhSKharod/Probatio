import ast
import itertools
from typing import Tuple

def run_combinatorial_tests(filepath: str) -> Tuple[bool, str]:
    try:
        with open(filepath, 'r') as file:
            source_code = file.read()

        tree = ast.parse(source_code)
        functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]

        if not functions:
            return False, "No functions found for combinatorial testing."

        output = ""
        total_tests = 0
        pass_count = 0
        fail_count = 0

        for func in functions:
            func_name = func.name
            args = [arg.arg for arg in func.args.args]
            output += f"\nFunction: {func_name} | Args: {args}\n"

            sample_values = [get_sample_values() for _ in args]
            combinations = list(itertools.product(*sample_values))
            output += f"  Generated {len(combinations)} combinations.\n"

            for i, combo in enumerate(combinations, 1):
                total_tests += 1
                output += f"  Test {i}: {func_name}({', '.join(map(repr, combo))}) => "

                try:
                    namespace = {}
                    exec(source_code, namespace)
                    result = namespace[func_name](*combo)
                    pass_count += 1
                    output += f"PASS (Result: {result})\n"
                except Exception as e:
                    fail_count += 1
                    output += f"FAIL (Error: {e})\n"

        pass_rate = pass_count / total_tests
        success = pass_rate >= 0.9
        output += f"\nCombinatorial Testing Completed: {total_tests} cases run. "
        output += f"{pass_count} passed, {fail_count} failed.\n"
        return success, output

    except Exception as e:
        return False, f"Combinatorial test error: {e}"

def get_sample_values():
    return [0, 1, -1, True, False, "", "test", [], {}, 3.14]
