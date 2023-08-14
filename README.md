# Discord Rich Presence Automation

Automate your Discord Rich Presence status based on whether Visual Studio is running or not.

## Overview

This script allows you to automatically update your Discord Rich Presence status based on whether Visual Studio is running on your computer. If Visual Studio is detected, the script will display your current project details; otherwise, it will show your CPU and RAM usage.
<p align="center">
  <img src="Preview/VS_closed.png" alt="preview" title="VS_closed"/>
  <img src="Preview/VS_running.png" alt="preview" title="VS_running"/>
</p>

## Prerequisites

- Python 3.x
- Discord client installed and running
- Visual Studio (optional, for project detection)

## Installation

1. Clone this repository to your local machine.
2. Install the required Python packages using the following command:
```
pip install pypresence psutil python-decouple
```
4. Create a `.env` file in the project directory and add your Discord client ID as follows:
```
CLIENT_ID=your_client_id_here
```
5. Adjust the script as needed (e.g., project names, images, buttons).
6. Run the script:
7. The script will automatically update your Discord Rich Presence based on the presence of Visual Studio.

## Autostart (Optional)

If you want the script to run automatically at system startup, you can create a shortcut to the `.exe` created with the:
```
pyinstaller --onefile --noconsole DiscordRichPresence.py
```
Then place the file in the `shell:startup` folder.
## Troubleshooting

If you encounter any issues, such as Discord not being found, make sure Discord is running before executing the script.

## Contributions

Feel free to contribute to this project by creating pull requests or reporting issues.
