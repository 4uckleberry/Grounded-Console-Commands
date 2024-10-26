# Grounded Console Commands

This Python tool was created to make it easier to access and generate console commands for the game [**Grounded**](https://grounded.obsidian.net/) by Obsidian Entertainment.

<img src="https://github.com/user-attachments/assets/a1058b4e-78aa-4fd2-b70d-c6f624e30f97" height="55px" alt="May contain bugs!">

## Overview

Using [**Universal Unreal Unlocker 4 (UUU)**](https://opm.fransbouma.com/uuuv4.htm ), players can hook into the game’s process (Maine) and use certain commands to enhance their character, summon blueprints, or spawn creatures.

> **Note**: This tool is intended to be used alongside UUU, not as a guide for its setup or usage.

## Features

- Includes console commands for all creatures and essential ingredients to make your character stronger.
- Omits certain items like Armor and Weapons by design to keep the tool uncluttered. Some additional items may be added in future updates based on user feedback.

If a particular item is missing, feel free to request it or use Unreal Model Viewer to locate it yourself.

## Installation

1. Ensure you have **Python 3.9+** installed on your system.
2. Clone or download the repository.
3. Navigate to the project’s root directory.
4. (Optional) Install the project to make it available system-wide

```bash
pip install -e .
```

## Usage

To start the tool, run the following command:

```bash
python -m groundedconsole
```

This will open a graphical interface where you can generate commands for the game.

### Using the Tool

1. Make sure **UUU** is already running and properly attached to the game.
2. In the GUI, select the **Category** of the blueprint you’re looking for (e.g., "Normal Creatures" or "Crafting Materials").
3. Choose the **Item** you want from the second dropdown.
4. Enter the desired **Quantity** of items or leave it as `1`.
    - **Note:** Spawning a large quantity of certain items (e.g., bugs) may impact game performance, so proceed with caution.
5. Click **Copy to Clipboard** to copy the commands.
6. In-game, open the console, paste the commands using `CTRL+V`, and press `ENTER`.

Enjoy the loot and have fun smashing bugs, my friends!

### Additional Notes

- If you’d prefer to work directly with the console commands without using the GUI, you can find the raw commands listed in `commands.json` located in the `groundedconsole` directory.

## Project Structure

```plaintext
LICENSE
README.md
pyproject.toml
groundedconsole/
│   ├── __init__.py      # Initialization code and tk gui logic
│   ├── __main__.py      # Main entry point for the application
│   ├── utils.py         # Utility functions for loading data, etc.
│   └── commands.json    # JSON data file containing categories, items, and console commands
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
