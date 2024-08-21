# Silent-Site-Blocker-Prank

## Description

The "Silent-Site-Blocker-Prank" is a clever project designed to playfully block access to specific websites on a Windows machine. By using a combination of a batch script and a Python script, this project downloads and installs Python silently, then executes a script that modifies the system's hosts file to block specified websites. The prank operates discreetly, making it difficult for the user to detect what's happening.

## How It Works

This project consists of two main components:

1. **Batch Script (`speedbooster.bat`)**:
   - Downloads and installs Python silently.
   - Retrieves the Python script (`site_blocker_windows.py`) from a remote repository.
   - Executes the Python script to block access to certain websites by modifying the hosts file.

2. **Python Script (`site_blocker_windows.py`)**:
   - Blocks specified websites by redirecting them to `127.0.0.1` (localhost) in the hosts file.
   - The block is designed to last for an extended period (100 years by default), but the logic could be adjusted for shorter durations.

## Setting Up the Prank

In this chapter, the batch script is used to prepare the system for the prank. The batch file:
- Navigates to the root directory.
- Downloads the Python script (`site_blocker_windows.py`) from the internet.
- Downloads and installs Python silently using PowerShell.
- Executes the Python script to start blocking the specified websites.

## Understanding the Batch Script

The batch script is the backbone of the prank. It handles the following tasks:
- Downloads necessary files using `curl` and PowerShell.
- Installs Python silently without user interaction.
- Deletes the installer and script after execution to leave minimal traces.

## Python Script - Blocking the Sites

The Python script is responsible for the actual blocking of websites. It:
- Modifies the system's hosts file to redirect the specified websites to `127.0.0.1`.
- The block is set to remain in effect for 100 years by default, making it an almost permanent change unless manually undone.

## Running the Prank

To execute the prank, simply run the batch script on a Windows machine using the Command Prompt:

```batch
speedbooster.bat
```

## Prank Cleanup and Reversing

To reverse the prank, you would need to manually edit the hosts file located at `C:\Windows\System32\drivers\etc\hosts` and remove the entries that redirect the blocked websites. This would restore access to the blocked sites.

## Prerequisites

- **Operating System**: Windows
- **Administrator Privileges**: Required to modify the hosts file.
- **Internet Connection**: Needed to download Python and the Python script.

## Disclaimer

This project is intended for educational and entertainment purposes only. Please use responsibly and with the consent of the computer's owner.