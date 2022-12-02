"""deprecated modules checker"""
from typing import TYPE_CHECKING, Optional
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

if TYPE_CHECKING:
    from pylint.lint import PyLinter


class DeprecatedClassesChecker(BaseChecker):

    __implements__ = IAstroidChecker

    name = "deprecated-classes"
    priority = -1
    msgs = {
        "W8802": (
            "'%s' class is deprecated please use '%s' instead",
            "deprecated-classes",
            "Refactor!",
        ),
    }

    # A pair of deprecated and target modules
    deprecated_classes = {"MyClass": "MyClassV2"}

    def __init__(self, linter: Optional["PyLinter"] = None) -> None:
        super().__init__(linter)

    def visit_call(self, node: nodes.Call):
        if type(node.func) == nodes.Name:
            if node.func.name in self.deprecated_classes:
                self.add_message(
                    msgid="deprecated-classes",
                    node=node,
                    args=(node.func.name, self.deprecated_classes[node.func.name]),
                )
