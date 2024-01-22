# vim: set fileencoding=utf-8
"""
pythoneda/shared/code_requests/code_request_nix_flake_spec.py

This file declares the CodeRequestNixFlakeSpec class.

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
from pythoneda.shared import attribute
from pythoneda.shared.nix.flake import NixFlakeSpec
from typing import List


class CodeRequestNixFlakeSpec(NixFlakeSpec):
    """
    Specifies Nix flakes wrapping a code request.

    Class name: CodeRequestNixFlakeSpec

    Responsibilities:
        - Provides conditions on Nix flakes wrapping code requests.

    Collaborators:
        - pythoneda.shared.nix.flake.NixFlakeSpec
    """

    def __init__(
        self,
        codeRequest: CodeRequest,
        name: str,
        versionSpec: str = None,
        url: str = None,
        inputSpecs: List = [],
    ):
        """
        Creates a new CodeRequestNixFlakeSpec instance.
        :param codeRequest: The code request.
        :type codeRequest: pythoneda.shared.code_requests.CodeRequest
        :param name: The name of the flake.
        :type name: str
        :param versionSpec: The version of the flake.
        :type versionSpec: str
        :param url: The url.
        :type url: str
        :param inputSpecs: The flake specs.
        :type inputSpecs: List[pythoneda.shared.nix.flake.NixFlakeSpec]
        """
        super().__init__(name, versionSpec, url, inputSpecs)
        self._code_request = codeRequest

    @classmethod
    def empty(cls):
        """
        Builds an empty instance. Required for unmarshalling.
        :return: An empty instance.
        :rtype: pythoneda.shared.code_requests.CodeRequestNixFlake
        """
        return cls(None, None)

    @property
    @attribute
    def code_request(self) -> CodeRequest:
        """
        Retrieves the code request.
        :return: Such instance.
        :rtype: pythoneda.shared.code_requests.CodeRequest
        """
        return self._code_request

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
        if varName == "code_request":
            result = self._code_request.to_dict()
        else:
            result = super()._get_attribute_to_json(varName)
        return result


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
