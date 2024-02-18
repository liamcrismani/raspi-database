
## Installing WSL

I learned how to do this [here](https://learn.microsoft.com/en-us/windows/wsl/install)
1. Enter windows features, enable WSL
2. Restart your computer
3. Open PowerShell, run the following commands
To install WSL
```PowerShell
wsl --install
```

To install Ubuntu (other distros are available for istall w/ WSL)
```PowerShell
wsl --install -d Ubuntu-22.04
```

Realise I need the Linux Kernel updates
```Powershell
wsl.exe --update
```

Set WSL 2 as the default version
```Powershell
wsl --set-default-version 2
```

## Adding a gitignore

I used Obsidian as my markdown editor, and was committing the obsidian source files to this GitHub repo, so needed to add a `gitignore` file to remove these files from future commits.

Having never used a `gitignore` file, this was the perfect chance to learn. I used [this freecodecamp tutorial](https://www.freecodecamp.org/news/gitignore-file-how-to-ignore-files-and-folders-in-git/) as a reference.

To create the `.gitignore` file:
```bash
touch .gitignore
```

Then to tell git to ignore the obsidian source files:
```shell
echo ".obsidian/" >> .gitignore
```

Then to remove the obsidian files from the repo without deleting them locally:
```shell
git rm -r --cached .obsidian/
```

Stage the new gitignore file:
```shell
git add .gitignore
```

And finally commit the changes:
```shell
git commit -m "update ignored files"
```

## Setting up the Raspberry Pi

I already had Raspbian installed on the microSD I was using in the Pi, but had forgotten the login details, so formatted the card and put a fresh install of Raspberry Pi OS (64-bit) desktop with Raspberry Pi imager.

With the fresh OS installed, it was a simple process of:
- Insert the new SD card
- Plug in the monitor and power supply
- Create a new log in

and we're in. I chose the desktop version or Raspberry Pi OS over the headless version, because I have a second monitor, and it gives me the option to work right on the Pi if I struggle with `SSH` as I did first time around.

## Opening a new branch in WSL Ubuntu

With Ubuntu installed with WSL, I added a new folder and cloned this GitHub repo. I want a seperate branch for the SSH management.

## Preparing VS Code

Since I wanted to use VS code for the code writing, I was pleasantly surprised to find [this guide](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode) on how to open a WSL project in VS code. I followed the steps to prep VS code.
- Opened VS code
- Installed WSL extension
- Instal remote development pack
- Restarted VS code to update
- Closed VS code

### Updating Ubuntu
```Bash
sudo apt-get update
```

And the wget (not sure if needed, but installed just in case)
```Shell
sudo apt-get install wget ca-certificates
```

I then installed Python
- withing VS code useing the extensions tool
and git
in the ubuntu terminal
configured username, email, and defaultbranch

cloned the repo in the ubuntu directory

## Enabling SSH to the Pi

learned [here](https://www.raspberrypi.com/documentation/computers/remote-access.html#introduction-to-remote-access)

### Grab the Pi IP address
I accessed through the desktop 'Connection Information' window, but could also run `ping raspberrypi.local` on the ubuntu terminal.  

Then
- set up the ssh server