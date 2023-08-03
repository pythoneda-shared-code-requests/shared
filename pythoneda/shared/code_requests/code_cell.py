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
from pythoneda.shared.code_requests.cell import Cell


class CodeCell(Cell):
    """
    A code cell in a code request.

    Class name: Cell

    Responsibilities:
        - Represents any code fragment inside a CodeRequest.

    Collaborators:
        - pythoneda.shared.code_requests.cell.Cell
    """

    def __init__(self, contents:str):
        """
        Creates a new CodeCell instance.
        :param contents: The cell contents.
        :type contents: str
        """
        super().__init__(contents)
