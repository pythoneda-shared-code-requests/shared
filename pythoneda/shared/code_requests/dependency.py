"""
pythoneda/shared/code_requests/dependency.py

This file declares the Dependency class.

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
from pythoneda import attribute, primary_key_attribute, ValueObject

class Dependency(ValueObject):
    """
    A dependency required to run a code cell in a code request.

    Class name: Dependency

    Responsibilities:
        - Contains metadata about a dependency required by a code cell.

    Collaborators:
        - pythoneda.ValueObject
    """

    def __init__(self, name:str, version:str, url:str):
        """
        Creates a new Dependency instance.
        :param name: The name of the dependency.
        :type name: str
        :param version: The version of the dependency.
        :type version: str
        :param url: The url of the dependency.
        :type url: str
        """
        super().__init__()
        self._name = name
        self._version = version
        self._url = url

    @property
    @primary_key_attribute
    def name(self) -> str:
        """
        Retrieves the name of the dependency.
        :return: The name.
        :rtype: str
        """
        return self._name

    @property
    @primary_key_attribute
    def version(self) -> str:
        """
        Retrieves the version of the dependency.
        :return: The version.
        :rtype: str
        """
        return self._version

    @property
    @attribute
    def url(self) -> str:
        """
        Retrieves the url of the dependency.
        :return: The url.
        :rtype: str
        """
        return self._url
