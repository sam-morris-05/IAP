# Prompt-and-Diff Log

## Prompt 1

### Prompt

What do I need to include in my repository for the first IAP milestone, and what
commands should I run to verify that Python, pip, pytest, and Git are working
correctly?

### Raw Output

The AI suggested creating a small project structure with a README, a basic
Python file, a simple pytest file, a prompt-and-diff log, and a .gitignore.

It also recommended using terminal commands such as:

- python --version
- pip --version
- pytest
- git --version
- git status

It also explained that the repository should be committed and pushed to GitHub
and that the final terminal evidence should show the runtime, test runner, and
Git repository status.

### What I Changed

I used the response as guidance while setting up the project environment.

I created the repository structure, wrote the README and concept brief, created
a basic Python file, added a simple test so pytest could run, and verified the
required tools from the VS Code terminal.

I also used the guidance to organize what evidence I needed to collect for the
milestone.

### Why the Original Was Wrong / Incomplete

Before using the AI guidance, I had not fully organized the repository or
verified all parts of the toolchain.

The AI helped me identify the required setup steps and organize the repository,
but I still had to create and verify the project on my computer.

## Prompt 2 - Requirements Elicitation

### Prompt

Elicit software requirements for a Python application called a Three-Phase
Power Calculator. The application is intended for electrical engineering users.
Provide user stories, acceptance criteria, and non-functional requirements.

### Raw Output

The AI suggested requirements involving three-phase calculations, Wye and
Delta systems, input validation, calculation history, file exporting, saved
settings, cross-platform support, and measurable calculation accuracy.

### What I Changed

I compared the generated requirements with the scope of the application I plan
to build.

I kept requirements that matched the project, revised requirements that needed
more detail, removed features that were outside my intended scope, and added
requirements the AI did not identify.

### Why the Original Was Wrong / Incomplete

The AI output was useful as a starting point, but it made assumptions about
features that were not part of my original concept.

It also did not ask enough questions about the exact scope before generating
the requirements, so the output required review before it accurately represented
the project.