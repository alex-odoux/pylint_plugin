from astroid.nodes import Call, ClassDef, FunctionDef, Name
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class DeprecatedObjectsChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = "no-deprecated"
    priority = -1
    msgs = {
        "W8800": (
            "%s %s is deprecated since version %s; reason: %s.",
            "deprecated",
            "Functions that have been marked via annotations as deprecated should not be used.",
        )
    }

    def __init__(self, linter=None):
        super().__init__(linter)

    def visit_decorators(self, node):
        # Check if there are decorators
        if node.nodes is None:
            return

        # Figure out whether its a class or function
        # that is deprecated, and get relevant info
        if isinstance(node.parent, ClassDef):
            parent_type = "Class"
        elif isinstance(node.parent, FunctionDef):
            parent_type = "Function"
        parent_name = node.parent.name

        # Check each decorator to see if its deprecating
        for decorator in node.get_children():
            if isinstance(decorator, Call):
                if decorator.func.name == "deprecated":
                    version = "(not specified)"
                    reason = "not specified"
                    if decorator.keywords is not None:
                        for kw in decorator.keywords:
                            if kw.arg == "version":
                                version = f'"{kw.value.value}"'
                            if kw.arg == "reason":
                                reason = f'"{kw.value.value}"'
                    self.add_message(
                        "deprecated",
                        node=node.parent,
                        args=(parent_type, parent_name, version, reason),
                    )
            elif isinstance(decorator, Name):
                if decorator.name == "deprecated":
                    self.add_message(
                        "deprecated",
                        node=node.parent,
                        args=(
                            parent_type,
                            parent_name,
                            "(not specified)",
                            "not specified",
                        ),
                    )

def register(linter):
    linter.register_checker(DeprecatedChecker(linter))
