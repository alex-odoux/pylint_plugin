from typing import TYPE_CHECKING

from pylint_plugins.sonar_issues_reporter import SonarIssuesReporter

from pylint_plugins.deprecated_classes import DeprecatedClassesChecker
from pylint_plugins.deprecated_modules import DeprecatedModulesChecker


if TYPE_CHECKING:
    from pylint.lint import PyLinter


def register(linter: "PyLinter") -> None:
    linter.register_reporter(SonarIssuesReporter)

    linter.register_checker(DeprecatedClassesChecker(linter))
    linter.register_checker(DeprecatedModulesChecker(linter))