# Various Python Projects

This repository contains a collection of different Python projects, ranging from small scripts to more complex applications. Each project is organized in its own directory with a README file explaining its purpose and usage.

## Documentation & Links

- [Python Official Documentation](https://docs.python.org/3/)
- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [Multi Root Workspaces] (https://devblogs.microsoft.com/ise/multi_root_workspaces_in_visual_studio_code/)
## Projects

- [common](./common) - Common custom library
- [fundamentals](./fundamentals) - fundamental project workspace root

## Configuring for VSCode Multi root workspace
- root need to have a .code-workspace file with a  **"folders": [ ... ]** section
- need to have a .env file in the main workspace root with content:   **PYTHONPATH=.**
- In the workspace root .vscode/settings.json,  add:  **"python.envFile": "${workspaceFolder}/.env"**
- In VSCode's user settings, add :  **"python.terminal.useEnvFile": true,**
- Run in a terminal the command :   **python fundamentals/auto_clean_archive.py** from the workspace root
- Alternatively you can also select the VSCode option : **Add as Python Project** and select the option run as task