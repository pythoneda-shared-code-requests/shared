"""
pythoneda/shared/code_requests/code_request_nix_flake.py

This file declares the CodeRequestNixFlake class.

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
from pathlib import Path
from pythoneda import attribute
from pythoneda.shared.nix_flake import NixFlake
from typing import List

class CodeRequestNixFlake(NixFlake):
    """
    A nix flake wrapping a code request.

    Class name: CodeRequestNixFlake

    Responsibilities:
        - Provides a way to run a code request by wrapping it in a Nix flake.

    Collaborators:
        - pythoneda.shared.nix_flake.NixFlake
    """

    def __init__(
            self,
            codeRequest:CodeRequest,
            name:str,
            version:str,
            url:str,
            inputs:List,
            description:str,
            homepage:str,
            licenseId:str,
            maintainers:List,
            copyrightYear:int,
            copyrightHolder:str,
            templateGroup:str="code_requests"):
        """
        Creates a new CodeRequestNixFlake instance.
        :param codeRequest: The code request.
        :type codeRequest: pythoneda.shared.code_requests.CodeRequest
        :param name: The name of the flake.
        :type name: str
        :param version: The version of the flake.
        :type version: str
        :param url: The url.
        :type url: str
        :param inputs: The flake inputs.
        :type inputs: List[pythoneda.shared.nix_flake.NixFlakeInput]
        :param description: The flake description.
        :type description: str
        :param templateGroup: The template group.
        :type templateGroup: str
        :param homepage: The project's homepage.
        :type homepage: str
        :param licenseId: The id of the license of the project.
        :type licenseId: str
        :param maintainers: The maintainers of the project.
        :type maintainers: List[str]
        :param copyrightYear: The copyright year.
        :type copyrightYear: year
        :param copyrightHolder: The copyright holder.
        :type copyrightHolder: str
        """
        super().__init__(
            name,
            version,
            url,
            inputs,
            templateGroup,
            description,
            homepage,
            licenseId,
            maintainers,
            copyrightYear,
            copyrightHolder)
        self._code_request = codeRequest

    @classmethod
    def empty(cls):
        """
        Builds an empty instance. Required for unmarshalling.
        :return: An empty instance.
        :rtype: pythoneda.shared.code_requests.CodeRequest
        """
        return cls(None, None, None, None, [], None, None, None, [], None, None)

    @property
    @attribute
    def code_request(self) -> CodeRequest:
        """
        Retrieves the code request.
        :return: Such instance.
        :rtype: pythoneda.shared.code_requests.CodeRequest
        """
        return self._code_request

    @property
    @attribute
    def package_inputs(self) -> List[NixFlake]:
        """
        Retrieves the list of package inputs, i.e., inputs besides NixOS and FlakeUtils.
        :return: Such inputs.
        :rtype: List[pythoneda.shared.nix_flake.NixFlake]
        """
        return [ input for input in self.inputs if input.name != "nixos" and input.name != "flake-utils" ]

    def generate_files(self, flakeFolder:str):
        """
        Generates the files.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        """
        self.generate_flake(flakeFolder)
        self.generate_pyprojecttoml_template(flakeFolder)

    def generate_pyprojecttoml_template(self, flakeFolder:str):
        """
        Generates the pyprojecttoml.template from a template.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        """
        self.process_template(flakeFolder, "PyprojecttomlTemplate", Path(self.templates_folder()) / self.template_subfolder, "root", "pyprojecttoml.template")

    def git_add_files(self, gitAdd):
        """
        Adds the generated files to git.
        :param gitAdd: The GitAdd instance.
        :type gitAdd: pythoneda.shared.git.GitAdd
        """
        self.git_add_flake(gitAdd)
        self.git_add_pyprojecttoml_template(gitAdd)

    def git_add_pyprojecttoml_template(self, gitAdd):
        """
        Adds the generated pyprojecttoml.template file to git.
        :param gitAdd: The GitAdd instance.
        :type gitAdd: pythoneda.shared.git.GitAdd
        """
        gitAdd.add("pyprojecttoml.template")

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
