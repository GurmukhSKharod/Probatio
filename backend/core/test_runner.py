import os
from engine.unit import run_unit_tests
from engine.property import run_property_tests
from engine.mutation import run_mutation_tests
from models.schemas import TestResult

def run_test_strategy(filepath: str, strategy: str) -> TestResult:
    if strategy == "unit":
        success, output = run_unit_tests(filepath)
    elif strategy == "property":
        success, output = run_property_tests(filepath)
    elif strategy == "mutation":
        success, output = run_mutation_tests(filepath)
    else:
        return TestResult(strategy=strategy, success=False, output="Invalid strategy.")

    return TestResult(strategy=strategy, success=success, output=output)
