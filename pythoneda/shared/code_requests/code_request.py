"""
pythoneda/shared/code_requests/code_request.py

This file declares the CodeRequest class.

Copyright (C) 2023-today rydnr's pythoneda-shared-code-requests/shared

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import abc
import json
from pythoneda.shared.code_requests import CodeCell
from pythoneda.shared.code_requests import MarkdownCell
from pythoneda import ValueObject
from typing import Dict, List

class CodeRequest(ValueObject, abc.ABC):
    """
    Request to review and execute code.

    Class name: CodeRequest

    Responsibilities:
        - Represents a cohesive piece of code.

    Collaborators:
        - None
    """
    def __init__(self):
        """
        Creates a new CodeRequest instance.
        """
        super().__init__()
        self._cells = []

    @property
    def cells(self) -> List:
        """
        Retrieves the request cells.
        :return: Such cells.
        :rtype: List[pythoneda.shared.code_requests.Cell]
        """
        return self._cells

    @abc.abstractmethod
    def write(self, file):
        """
        Writes the code request to a file.
        :param file: The file to write.
        :type file: File
        """
        raise Error("write(file) should be implemented in subclasses")

    def append_markdown(self, txt: str):
        """
        Appends a new markdown cell.
        :param txt: The text to add.
        :type txt: str
        """
        self.cells.append(MarkdownCell(txt))

    def append_code(self, code: str):
        """
        Appends a new code cell.
        :param code: The code to add.
        :type code: str
        """
        self.cells.append(CodeCell(code))

    def to_dict(self) -> Dict:
        """
        Converts this instance into a dictionary.
        :return: Such dictionary.
        :rtype: Dict
        """
        return {
            "cells": self.cells
        }

    @classmethod
    def from_dict(cls, dict:Dict): # Change
        """
        Creates a new instance with the contents of given dictionary.
        :param dict: The dictionary.
        :type dict: Dict
        :return: A CodeRequest instance.
        :rtype: pythoneda.shared.code_requests.CodeRequest
        """
        return cls(dict["cells"])

    def to_json(self) -> str:
        """
        Serializes this instance as json.
        :return: The json text.
        :rtype: str
        """
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, jsonText: str): # -> Change
        """
        Reconstructs a CodeRequest instance from given json text.
        :param jsonText: The json text.
        :type jsonText: str
        :return: The CodeRequest instance.
        :rtype: pythoneda.shared.code_requests.CodeRequest
        """
        return cls.from_dict(json.loads(jsonText))
