# shared

Shared kernel for code requests.

## How to declare it in your flake

Check the latest tag of the artifact repository: https://github.com/pythoneda-shared-code-requests/shared-artifact/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-shared-artifact-artifact-events = {
      [optional follows]
      url =
        "github:pythoneda-shared-code-requests/shared-artifact/[version]?dir=artifact-events";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [https://nixos/nixpkgs](nixpkgs "nixpkgs") and [https://github.com/numtide/flake-utils](flake-utils "flake-utils").

The Nix flake is under the [https://github.com/pythoneda-shared-code-requests/shared-artifact/tree/main/artifact-events](artifact-events "artifact-events") folder of <https://github.com/pythoneda-shared-code-requests/shared-artifact>.

