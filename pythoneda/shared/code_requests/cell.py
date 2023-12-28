"""
pythoneda/shared/code_requests/cell.py

This file declares the Cell class.

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
from pythoneda import primary_key_attribute, ValueObject
from typing import List


class Cell(ValueObject, abc.ABC):
    """
    A piece of the code request.

    Class name: Cell

    Responsibilities:
        - Represents any fragment inside a CodeRequest.

    Collaborators:
        - None
    """
    def __init__(self, contents: str):
        """
        Creates a new Cell instance.
        :param contents: The cell contents.
        :type contents: str
        """
        super().__init__()
        self._contents = contents

    @classmethod
    def empty(cls):
        """
        Builds an empty instance. Required for unmarshalling.
        :return: An empty instance.
        :rtype: pythoneda.shared.code_requests.Cell
        """
        return cls(None)

    @property
    @primary_key_attribute
    def contents(self) -> str:
        """
        Retrieves the cell contents.
        :return: Such information.
        :rtype: str
        """
        return self._contents

    @property
    def dependencies(self) -> List:
        """
        Retrieves the dependencies needed to run the cell.
        :return: The dependencies.
        :rtype: List[pythoneda.shared.code_requests.Dependency]
        """
        return []
