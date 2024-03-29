# vim: set fileencoding=utf-8
"""
pythoneda/shared/code_requests/markdown_cell.py

This file declares the MarkdownCell class.

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


class MarkdownCell(Cell):
    """
    A Markdown cell in a code request.

    Class name: MarkdownCell

    Responsibilities:
        - Represents any Markdown fragment inside a CodeRequest.

    Collaborators:
        - pythoneda.shared.code_requests.Cell
    """

    def __init__(self, contents: str):
        """
        Creates a new MarkdownCell instance.
        :param contents: The cell contents.
        :type contents: str
        """
        super().__init__(contents)

    @classmethod
    def empty(cls):
        """
        Builds an empty instance. Required for unmarshalling.
        :return: An empty instance.
        :rtype: pythoneda.shared.code_requests.MarkdownCell
        """
        return cls(None)
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
