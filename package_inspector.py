import ast
import os
import re

# A property setter validates the value every time the attribute is assigned.
# An __init__-only check validates the value only when the object is created.
# If the attribute is changed later, an __init__-only check does not run again.

class SourceAuditor:

    def __init__(self, target_path: str, /) -> None:
        self.target_path = target_path

    @property
    def target_path(self) -> str:
        return self._target_path

    @target_path.setter
    def target_path(self, value: str) -> None:
        if not os.path.exists(value):
            raise FileNotFoundError(
                f"Target path '{value}' does not exist."
            )
        self._target_path = value

    def audit_module_structure(
        self, file_contents: str, /, *, max_line_length: int = 79
    ) -> dict:
        tree = ast.parse(file_contents)

        spacing_violations = []
        line_length_violations = []
        trailing_whitespace_violations = []
        colon_spacing_violations = []

        functions = []

        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                functions.append(node)

        for i in range(len(functions) - 1):
            current = functions[i]
            next_function = functions[i + 1]

            start_line = next_function.lineno

            if next_function.decorator_list:
                start_line = next_function.decorator_list[0].lineno

            blank_lines = start_line - current.end_lineno - 1

            if blank_lines < 2:
                spacing_violations.append(next_function.name)

        lines = file_contents.splitlines()

        for number, line in enumerate(lines, start=1):

            if len(line) > max_line_length:
                line_length_violations.append(number)

            if line.strip() and line != line.rstrip():
                trailing_whitespace_violations.append(number)

            if re.search(r"\w:\S", line):
                colon_spacing_violations.append(number)

        return {
            "spacing_violations": spacing_violations,
            "line_length_violations": line_length_violations,
            "trailing_whitespace_violations": trailing_whitespace_violations,
            "colon_spacing_violations": colon_spacing_violations
        }

    def verify_sdist_layout(self, /) -> bool:
        setup_path = os.path.join(self.target_path, "setup.py")
        readme_path = os.path.join(self.target_path, "README.txt")

        if not os.path.isfile(setup_path):
            return False

        if not os.path.isfile(readme_path):
            return False

        with open(setup_path, "r") as file:
            setup_contents = file.read()

        match = re.search(
            r"py_modules\s*=\s*\[(.*?)\]",
            setup_contents,
            re.DOTALL
        )

        if not match:
            return False

        modules = re.findall(
            r"['\"]([^'\"]+)['\"]",
            match.group(1)
        )

        for module in modules:
            module_path = os.path.join(
                self.target_path,
                module + ".py"
            )

            if os.path.isfile(module_path):
                return True

        return False


if __name__ == "__main__":

    auditor = SourceAuditor(".")

    test_code = """def first_function():
    return 1


def second_function():
    return 2
"""

    result = auditor.audit_module_structure(test_code)

    print(result)

    assert result["spacing_violations"] == []

    print("Self-test passed")

    test_code = """def first_function():
    return 1

def second_function():
    return 2
"""

    result = auditor.audit_module_structure(test_code)

    print("Edge Case 1:", result["spacing_violations"])

    assert result["spacing_violations"] == ["second_function"]

    print("Edge Case 1 passed")

    test_code = """def first_function():
    return 1

@decorator
def second_function():
    return 2
"""

    result = auditor.audit_module_structure(test_code)

    print("Edge Case 2:", result["spacing_violations"])

    assert result["spacing_violations"] == ["second_function"]

    print("Edge Case 2 passed")

    test_code = """def first_function():
    return 1


def second_function():
    return 2
"""

    temp_path = "test_package"
    os.makedirs(temp_path, exist_ok=True)

    setup_file = os.path.join(temp_path, "setup.py")
    module_file = os.path.join(temp_path, "sample.py")

    with open(setup_file, "w") as file:
        file.write("py_modules=['sample']")

    with open(module_file, "w") as file:
        file.write("")

    test_auditor = SourceAuditor(temp_path)

    result = test_auditor.verify_sdist_layout()

    print("Edge Case 3 before removing README:", result)

    readme_file = os.path.join(temp_path, "README.txt")

    with open(readme_file, "w") as file:
        file.write("")

    result = test_auditor.verify_sdist_layout()

    print("Edge Case 3 with README:", result)

    os.remove(readme_file)

    result = test_auditor.verify_sdist_layout()

    assert result is False

    print("Edge Case 3 passed")

    test_code = """def first_function():
    return 1
    
 
def second_function():
    return 2
"""

    result = auditor.audit_module_structure(test_code)

    print("Edge Case 4:", result["trailing_whitespace_violations"])

    assert result["trailing_whitespace_violations"] == []

    print("Edge Case 4 passed")

    os.remove(setup_file)
    os.remove(module_file)
    os.rmdir(temp_path)
