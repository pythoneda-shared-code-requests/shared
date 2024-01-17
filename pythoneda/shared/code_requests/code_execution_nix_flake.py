# vim: set fileencoding=utf-8
"""
pythoneda/shared/code_requests/jupyterlab/code_execution_nix_flake.py

This file defines the CodeExecutionNixFlake class.

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
from .code_cell import CodeCell
from .code_request import CodeRequest
from .code_request_nix_flake import CodeRequestNixFlake
from pathlib import Path
from pythoneda.shared.git import GitAdd
from pythoneda.shared.nix_flake.licenses import Gpl3
from typing import List


class CodeExecutionNixFlake(CodeRequestNixFlake):

    """
    Nix flake for executing code requests.

    Class name: CodeExecutionNixFlake

    Responsibilities:
        - Create a Nix flake that executes code described in a CodeRequest.

    Collaborators:
        - None
    """

    def __init__(self, codeRequest: CodeRequest, inputs: List):
        """
        Creates a new CodeRequestNixFlake instance.
        :param codeRequest: The code request.
        :type codeRequest: pythoneda.shared.code_requests.CodeRequest
        :param inputs: The resolved dependencies as NixFlakes.
        :type inputs: List
        """
        super().__init__(
            codeRequest,
            "code-execution",
            "0.0.0",
            "https://github.com/pythoneda-shared-code-requests/shared",
            inputs,
            "Executes a PythonEDA Code Request",
            "https://github.com/pythoneda-shared-code-requests/shared",
            Gpl3.license_type(),
            ["rydnr <github@acm-sl.org>"],
            2023,
            "rydnr",
            "code_execution",
        )

    @classmethod
    def empty(cls):
        """
        Builds an empty instance. Required for unmarshalling.
        :return: An empty instance.
        :rtype: pythoneda.shared.code_requests.CodeExecutionNixFlake
        """
        return cls(None, [])

    def generate_files(self, flakeFolder: str):
        """
        Generates the files.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        """
        super().generate_files(flakeFolder)
        self.generate_code(flakeFolder)
        self.generate_entrypoint(flakeFolder)

    def generate_code(self, flakeFolder: str):
        """
        Generates the code.py file.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        """
        with open(Path(flakeFolder) / "code_request.py", "w") as output_file:
            output_file.write("_pythoneda_no_error_so_far = True\n")
            for cell in self.code_request.cells:
                if isinstance(cell, CodeCell):
                    # TODO: find a non-hardcoded way to prevent the script to continue
                    output_file.write("\nif _pythoneda_no_error_so_far:")
                    output_file.write('\n    print("```")\n')
                    for line in [
                        line for line in cell.contents.splitlines() if line.rstrip()
                    ]:
                        output_file.write(f"    print({repr(line)})\n")
                    output_file.write('    print("```")\n')
                    for line in [
                        line for line in cell.contents.splitlines() if line.rstrip()
                    ]:
                        output_file.write(f"    {line}\n")
                else:
                    first_time = True
                    for line in cell.contents.splitlines():
                        if first_time:
                            output_file.write("\nif _pythoneda_no_error_so_far:")
                            first_time = False
                        output_file.write(f"\n    print({repr(line)})")

    def generate_entrypoint(self, flakeFolder: str):
        """
        Generates the entrypoint.sh file.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        """
        self.process_template(
            flakeFolder,
            "EntrypointSh",
            Path(self.templates_folder()) / self.template_subfolder,
            "root",
            "code-execution.sh",
        )

    def git_add_files(self, gitAdd: GitAdd):
        """
        Adds the generated files to git.
        :param gitAdd: The GitAdd instance.
        :type gitAdd: pythoneda.shared.git.GitAdd
        """
        super().git_add_files(gitAdd)
        self.git_add_code(gitAdd)
        self.git_add_entrypoint(gitAdd)

    def git_add_code(self, gitAdd: GitAdd):
        """
        Adds the generated code_request.py file to git.
        :param gitAdd: The GitAdd instance.
        :type gitAdd: pythoneda.shared.git.GitAdd
        """
        gitAdd.add("code_request.py")

    def git_add_entrypoint(self, gitAdd: GitAdd):
        """
        Adds the generated entrypoint.sh file to git.
        :param gitAdd: The GitAdd instance.
        :type gitAdd: pythoneda.shared.git.GitAdd
        """
        gitAdd.add("code-execution.sh")
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
