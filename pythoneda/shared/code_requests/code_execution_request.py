"""
pythoneda/shared/code_requests/code_execution_request.py

This file declares the CodeExecutionRequest class.

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
from .code_request import CodeRequest
from .code_request_nix_flake_spec import CodeRequestNixFlakeSpec
from pythoneda import primary_key_attribute

class CodeExecutionRequest(CodeRequest):
    """
    Request to execute code.

    Class name: CodeExecutionRequest

    Responsibilities:
        - Represents a cohesive piece of code.

    Collaborators:
        - None
    """

    def __init__(self, codeRequest: CodeRequest):
        """
        Creates a new CodeExecutionRequest instance.
        :param codeRequest: The original code request.
        :type codeRequest: pythoneda.shared.code_requests.CodeRequest
        """
        super().__init__()
        self._code_request = codeRequest

    @classmethod
    def empty(cls):
        """
        Builds an empty instance. Required for unmarshalling.
        :return: An empty instance.
        :rtype: pythoneda.shared.code_requests.CodeRequest
        """
        return cls(None)

    @property
    @primary_key_attribute
    def code_request(self) -> CodeRequest:
        """
        Retrieves the code request.
        :return: The original code request.
        :rtype: pythoneda.shared.code_requests.CodeRequest
        """
        return self._code_request

    @property
    def nix_flake_spec(self):
        """
        Retrieves the specification for the Nix flake.
        :return: Such specification.
        :rtype: pythoneda.shared.nix_flake.NixFlakeSpec
        """
        return CodeRequestNixFlakeSpec(self.code_request, "code-request")

    def write(self, file):
        """
        Writes the code request to a file.
        :param file: The file to write.
        :type file: File
        """
        self.code_request.write(file)

    def _set_attribute_from_json(self, varName, varValue):
        """
        Changes the value of an attribute of this instance.
        :param varName: The name of the attribute.
        :type varName: str
        :param varValue: The value of the attribute.
        :type varValue: int, bool, str, type
        """
        if varName == "code_request":
            self._code_request = CodeRequest.from_dict(varValue)
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
        result = None
        if varName == "code_request":
            result = self.code_request.to_dict()
        else:
            result = super()._get_attribute_to_json(varName)
        return result

    async def run(self):
        """
        Runs this code request.
        """
        await self.code_request.run()
