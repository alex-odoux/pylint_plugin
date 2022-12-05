from pylint_plugins.sonar_issues_reporter import SonarIssuesReporter

from pylint_plugins.deprecated_objects import DeprecatedObjectsChecker
from pylint_plugins.do_not_use_modules import DoNotUseModulesChecker


from pylint.lint import PyLinter


def register(linter: PyLinter) -> None:
    linter.register_reporter(SonarIssuesReporter)

    linter.register_checker(DeprecatedObjectsChecker(linter))
    linter.register_checker(DoNotUseModulesChecker(linter))
