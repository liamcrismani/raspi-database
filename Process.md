
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

I chose the desktop version or Raspberry Pi OS over the headless version, because I have a second monitor, and it gives me the option to work right on the Pi if I struggle with `SSH` as I did first time around.
## Preparing VS Code

Since I wanted to use VS code to manage some of the project, I was pleasantly surprised to find [this guide](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode) on how to open a WSL project in VS code. I followed the steps to:
- open VS code inside the local project directory
- install the WSL extension
- install the remote development pack

Next I updated Ubuntu
```Bash
sudo apt-get update
```

And the wget (not sure if needed, but installed just in case)
```Shell
sudo apt-get install wget ca-certificates
```

and then installed Python and configured git with my personal settings, and cloned this repo in the Ubuntu project folder.

## Accessing the Pi with SSH

This was the major sticking point of the project first time round. Thankfully, it was more pain-free this time. I followed the steps [here](https://www.raspberrypi.com/documentation/computers/remote-access.html#introduction-to-remote-access).

After getting a little bit stuck, I reset all my SSH settings and started fresh. I consulted with ChatGPT here: https://chat.openai.com/share/040fcdf4-51b3-4f1d-bbdc-b7b1298f5a9a

That still didn't quite resolve it, but after leaving it for a few days and coming back, I tried again and was able to connect first time. May have just needed to turn it off again.


## Installing SQLite

I then installed SQLite3 to host the first database. I followed [this guide](https://pimylifeup.com/raspberry-pi-sqlite/).

First update the Raspberry Pi's OS
```Terminal
sudo apt update
sudo apt full-upgrade
```

And then install SQLite
```Terminal
sudo apt install sqlite3
```


## Creating the a database

I downloaded the Chinook dataset from [this tutorial](https://www.sqlitetutorial.net/sqlite-sample-database/). 

Save the file to local repo (in WSL), and secure-copy to the Raspberry Pi over SSH

learned [here](https://www.raspberrypi.com/documentation/computers/remote-access.html#secure-shell-from-linux-or-mac-os).

Copy the chinook directory
```Shell
scp -r chinook/ liamc@192.168.0.21:
```

Open the connect to the Raspberry Pi
```Shell
ssh liamc@192.168.0.21
```

Start SQLIite by navigating to the correct directory
```

```