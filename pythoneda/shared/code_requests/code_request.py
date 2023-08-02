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
from pythoneda.value_object import ValueObject

class CodeRequest(ValueObject):
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
        super().__init__(None)
