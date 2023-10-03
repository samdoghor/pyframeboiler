# tools.py

"""
This module defines all functions and classes to create the boilerplate.
"""

import inquirer
from rich import print as mprint
from rich.prompt import Prompt


class CreateProject:
    """ This class defines the project creation """

    @staticmethod
    def create_project():
        """ This function defines the project creation """

        project_name = Prompt.ask(
            "Project Name", default="myte-project")

        mprint(f"✅ Project name: {project_name}")

        frameworks_choice = ["Flask", "Bottle", "Web2py"]

        frameworks = [

            inquirer.List(
                "framework",
                message="Select a framework",
                choices=frameworks_choice,
                carousel=True,  # Enables arrow key navigation
            )
        ]

        selected_framework = inquirer.prompt(frameworks)

        mprint(f"✅ {selected_framework['framework']},  selected")

        if selected_framework == "Flask":
            FlaskFramework.create_project()
