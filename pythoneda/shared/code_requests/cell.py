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
import json
from pythoneda import primary_key_attribute, ValueObject
from typing import Dict, List

class Cell(ValueObject, abc.ABC):
    """
    A piece of the code request.

    Class name: Cell

    Responsibilities:
        - Represents any fragment inside a CodeRequest.

    Collaborators:
        - None
    """
    def __init__(self, contents:str):
        """
        Creates a new Cell instance.
        :param contents: The cell contents.
        :type contents: str
        """
        super().__init__()
        self._contents = contents

    @property
    @primary_key_attribute
    def contents(self) -> str:
        """
        Retrieves the cell contents.
        :return: Such information.
        :rtype: str
        """
        return self._contents

    def to_dict(self) -> Dict:
        """
        Converts this instance into a dictionary.
        :return: Such dictionary.
        :rtype: Dict
        """
        return {
            "class": self.__class__.full_class_name(),
            "contents": self.contents
        }

    @classmethod
    def from_dict(cls, dict:Dict): # Cell
        """
        Creates a new instance with the contents of given dictionary.
        :param dict: The dictionary.
        :type dict: Dict
        :return: A Cell instance.
        :rtype: pythoneda.shared.code_requests.Cell
        """
        return dict["class"](dict["contents"])

    def to_json(self) -> str:
        """
        Serializes this instance as json.
        :return: The json text.
        :rtype: str
        """
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, jsonText: str): # -> Cell
        """
        Reconstructs a CodeRequest instance from given json text.
        :param jsonText: The json text.
        :type jsonText: str
        :return: The Cell instance.
        :rtype: pythoneda.shared.code_requests.Cell
        """
        return cls.from_dict(json.loads(jsonText))

    @property
    def dependencies(self) -> List:
        """
        Retrieves the dependencies needed to run the cell.
        :return: The dependencies.
        :rtype: List[pythoneda.shared.code_requests.Dependency]
        """
        return []
