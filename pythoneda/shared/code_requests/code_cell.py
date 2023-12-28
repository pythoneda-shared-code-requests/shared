"""
pythoneda/shared/code_requests/code_cell.py

This file declares the CodeCell class.

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
from .cell import Cell
from .dependency import Dependency
from pythoneda import attribute
from typing import List


class CodeCell(Cell):
    """
    A code cell in a code request.

    Class name: CodeCell

    Responsibilities:
        - Represents any code fragment inside a CodeRequest.

    Collaborators:
        - pythoneda.shared.code_requests.Cell
        - pythoneda.shared.code_requests.Dependency
    """

    def __init__(self, contents: str, dependencies: List):
        """
        Creates a new CodeCell instance.
        :param contents: The cell contents.
        :type contents: str
        :param dependencies: The dependencies.
        :type dependencies: List[pythoneda.shared.code_requests.Dependency]
        """
        super().__init__(contents)
        self._dependencies = dependencies

    @classmethod
    def empty(cls):
        """
        Builds an empty instance. Required for unmarshalling.
        :return: An empty instance.
        :rtype: pythoneda.shared.code_requests.CodeCell
        """
        return cls(None, [])

    @property
    @attribute
    def dependencies(self) -> List:
        """
        Retrieves the dependencies needed to run the cell.
        :return: The dependencies.
        :rtype: List[pythoneda.shared.code_requests.Dependency]
        """
        return self._dependencies

    def _set_attribute_from_json(self, varName, varValue):
        """
        Changes the value of an attribute of this instance.
        :param varName: The name of the attribute.
        :type varName: str
        :param varValue: The value of the attribute.
        :type varValue: int, bool, str, type
        """
        if varName == 'dependencies':
            self._dependencies = [Dependency.from_dict(value) for value in varValue]
        else:
            super()._set_attribute_from_json(varName, varValue)

    def _get_attribute_to_json(self, varName) -> str:
        """
        Retrieves the value of an attribute of this instance, as Json.
        :param varName: The name of the attribute.
        :type varName: str
        :return: The attribute value in json format.
        :rtype: str
        """
        if varName == 'dependencies':
            result = [dependency.to_dict() for dependency in self._dependencies]
        else:
            result = super()._get_attribute_to_json(varName)
        return result
