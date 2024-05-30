{
  description = "A Python environment.";

  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs/nixos-unstable;
    flake-utils.url = github:numtide/flake-utils;
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        pythonPackages = pkgs.python311Packages;
      in
      {
        devShells.default = pkgs.mkShell {

          buildInputs = with pkgs; [
            # Python
            pythonPackages.python
            pythonPackages.matplotlib
            pythonPackages.numpy
            #pythonPackages.venvShellHook
          ];
        };
      }
    );
  
}