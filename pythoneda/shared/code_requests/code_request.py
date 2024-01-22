# vim: set fileencoding=utf-8
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
from .cell import Cell
from .code_cell import CodeCell
import abc
from pythoneda.shared import attribute, ValueObject
from pythoneda.shared.code_requests import MarkdownCell
from typing import List


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

    @classmethod
    def empty(cls):
        """
        Builds an empty instance. Required for unmarshalling.
        :return: An empty instance.
        :rtype: pythoneda.shared.code_requests.CodeRequest
        """
        return cls()

    @property
    @attribute
    def cells(self) -> List:
        """
        Retrieves the request cells.
        :return: Such cells.
        :rtype: List[pythoneda.shared.code_requests.Cell]
        """
        return self._cells

    @property
    @abc.abstractmethod
    def nix_flake_spec(self):
        """
        Retrieves the specification for the Nix flake.
        :return: Such specification.
        :rtype: pythoneda.shared.nix.flake.NixFlakeSpec
        """
        raise NotImplementedError(
            "nix_flake_spec() property should be implemented in subclasses"
        )

    @abc.abstractmethod
    def write(self, file):
        """
        Writes the code request to a file.
        :param file: The file to write.
        :type file: File
        """
        raise NotImplementedError("write(file) should be implemented in subclasses")

    def append_markdown(self, markdown: str):
        """
        Appends a new markdown cell.
        :param markdown: The text to add.
        :type markdown: str
        """
        self.cells.append(MarkdownCell(markdown))

    def append_code(self, code: str, dependencies: List):
        """
        Appends a new code cell.
        :param code: The code to add.
        :type code: str
        :param dependencies: The code dependencies.
        :type dependencies: List
        """
        self.cells.append(CodeCell(code, dependencies))

    @property
    def dependencies(self) -> List:
        """
        Retrieves the dependencies of this code request.
        :return: Such list.
        :rtype: List[pythoneda.shared.code_requests.Dependency]
        """
        result = set()
        for cell in self.cells:
            for dep in cell.dependencies:
                result.update(dep)

        return list(result)

    def _set_attribute_from_json(self, varName, varValue):
        """
        Changes the value of an attribute of this instance.
        :param varName: The name of the attribute.
        :type varName: str
        :param varValue: The value of the attribute.
        :type varValue: int, bool, str, type
        """
        if varName == "cells":
            self._cells = [Cell.from_dict(value) for value in varValue]
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
        if varName == "cells":
            result = [cell.to_dict() for cell in self._cells]
        else:
            result = super()._get_attribute_to_json(varName)
        return result

    async def run(self):
        """
        Runs this code request.
        """
        pass


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
