"""deprecated modules checker"""
from typing import TYPE_CHECKING, Optional
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

if TYPE_CHECKING:
    from pylint.lint import PyLinter


class DeprecatedModulesChecker(BaseChecker):

    __implements__ = IAstroidChecker

    name = "deprecated-modules"
    priority = -1
    msgs = {
        "W8801": (
            "'%s' module is deprecated please use '%s' instead",
            "deprecated-modules",
            "Refactor!",
        ),
    }

    # A pair of deprecated and target modules
    deprecated_modules = {"antigravity": "progravity"}

    def __init__(self, linter: Optional["PyLinter"] = None) -> None:
        super().__init__(linter)

    def visit_importfrom(self, node: nodes.ImportFrom) -> None:
        """Checks the from abc import def, ghi construct"""
        if node.modname in self.deprecated_modules:
            self.add_message(
                msgid="deprecated-modules",
                node=node,
                args=(node.modname, self.deprecated_modules[node.modname], )
            )

    def visit_import(self, node: nodes.Import) -> None:
        """Checks the import a,b,c construct"""
        for child_node in node.names:
            if child_node[0] in self.deprecated_modules:
                self.add_message(
                    msgid="deprecated-modules",
                    node=node,
                    args=(child_node[0], self.deprecated_modules[child_node[0]], )
                )
