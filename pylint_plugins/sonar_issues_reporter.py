import json
from typing import Optional, List

from pylint.interfaces import IReporter
from pylint.message import Message
from pylint.reporters.base_reporter import BaseReporter
from pylint.reporters.ureports.nodes import Section


class SonarIssuesReporter(BaseReporter):
    __implements__ = IReporter
    name = "sonar-issues"
    extension = "json"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._messages: List[Message] = []

    def handle_message(self, msg: Message) -> None:
        self._messages.append(msg)

    def display_messages(self, layout: Optional[Section]):
        print(
            json.dumps(
                {"issues": [self._msg_to_sonar_dict(msg) for msg in self._messages]},
                indent=4,
            ),
            file=self.out,
        )

    @staticmethod
    def _msg_to_sonar_dict(msg: Message):
        sonar_dict = {
            "engineId": "PYLINT",
            "ruleId": msg.msg_id,
            "type": "CODE_SMELL",
            "primaryLocation": {
                "message": msg.msg or "",
                "filePath": msg.path,
                "textRange": {
                    "startLine": msg.line,
                    "startColumn": msg.column,
                },
            },
            "severity": "MINOR",
            "effortMinutes": 10,
        }
        if hasattr(msg, "end_line") and msg.end_line:
            sonar_dict["primaryLocation"]["textRange"]["endLine"] = msg.end_line
            if hasattr(msg, "end_column") and msg.end_column:
                sonar_dict["primaryLocation"]["textRange"]["endColumn"] = msg.end_column
        return sonar_dict

    def display_reports(self, layout: Section):
        pass

    def _display(self, layout: Section):
        pass
