"""
pythoneda/shared/code_requests/pythoneda_dependency.py

This file declares the PythonedaDependency class.

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
from .dependency import Dependency

class PythonedaDependency(Dependency):
    """
    A PythonEDA dependency.

    Class name: PythonedaDependency

    Responsibilities:
        - Used to label PythonEDA dependencies.

    Collaborators:
        - None
    """

    def __init__(self, name: str, version: str, url: str):
        """
        Creates a new PythonedaDependency instance.
        :param name: The name of the dependency.
        :type name: str
        :param version: The version of the dependency.
        :type version: str
        :param url: The url of the dependency.
        :type url: str
        """
        super().__init__(name, version, url)

    @classmethod
    def empty(cls):
        """
        Builds an empty instance. Required for unmarshalling.
        :return: An empty instance.
        :rtype: pythoneda.shared.code_requests.PythonedaDependency
        """
        return cls(None, None, None)
