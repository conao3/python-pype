{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    treefmt-nix.url = "github:numtide/treefmt-nix";
  };

  outputs =
    inputs:
    inputs.flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [
        "x86_64-linux"
        "aarch64-darwin"
      ];

      imports = [
        inputs.treefmt-nix.flakeModule
      ];

      perSystem =
        {
          pkgs,
          system,
          ...
        }:
        let
          overlay =
            final: prev:
            let
              python = prev.python312;
            in
            {
              inherit python;
            };
          pkgs = import inputs.nixpkgs {
            inherit system;
            overlays = [ overlay ];
          };
          pype = pkgs.python.pkgs.buildPythonApplication {
            pname = "pype-bin";
            version = "0.1.2";
            pyproject = true;
            src = ./.;
            build-system = [ pkgs.python.pkgs.poetry-core ];
            dependencies = [ pkgs.python.pkgs.jinja2 ];
            meta.mainProgram = "pype";
          };
        in
        {
          packages = {
            inherit pype;
            default = pype;
          };

          devShells.default = pkgs.mkShell {
            packages = [
              pkgs.python
              pkgs.uv
            ];
          };

          treefmt = {
            projectRootFile = "flake.nix";
            programs.nixfmt.enable = true;
            programs.ruff-check.enable = true;
            programs.ruff-format.enable = true;
          };
        };
    };
}
