# Process
TODO
- [] Transfer steps to readme
- [ ] Rewrite with consistent language
## Install WSL

I learned how to do this [here](https://learn.microsoft.com/en-us/windows/wsl/install)
1. Enter windows features, enable WSL
2. Restart your computer
3. Or open PowerShell, run the following commands:

Install WSL
```PowerShell
wsl --install
```

To install Ubuntu (other distros are available for install w/ WSL)
```PowerShell
wsl --install -d Ubuntu-22.04
```

Update Linux kernels
```Powershell
wsl.exe --update
```

Set WSL 2 as the default version
```Powershell
wsl --set-default-version 2
```

## Add a gitignore

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

## Set up the Raspberry Pi

I already had Raspbian installed on the microSD I was using in the Pi, but had forgotten the login details, so formatted the card and put a fresh install of Raspberry Pi OS (64-bit) desktop with Raspberry Pi imager.

With the fresh OS installed, it was a simple process of:
- Insert the new SD card
- Plug in the monitor and power supply
- Create a new log in

Download the Raspberry Pi imager [here](https://www.raspberrypi.com/software/).

Write a version of Raspberry Pi OS to an SD card. I chose the desktop version or Raspberry Pi OS over the headless version, because I have a second monitor, and it gave me the option to work right on the Pi if I struggle with `SSH` as I did first time around.
## Preparing VS Code

Since I wanted to use VS code to manage some of the project, I was pleasantly surprised to find [this guide](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode) on how to open a WSL project in VS code. I followed the steps to:
- open VS code inside the local project directory
- install the WSL extension
- install the remote development pack

Open Ubuntu terminal and update the OS
```Bash
sudo apt-get update
```

And then wget (not sure if needed, but installed just in case)
```Shell
sudo apt-get install wget ca-certificates
```

Then install Python via the extensions window, and clone this repo in an new WSL project directory.

## Accessing the Pi with SSH

With the Raspberry Pi connected to your local connect, find the IP address. This can be done via the settings if connected to a monitor, or by running the following command from your main machine:

```Bash
ping raspberrypi.local
```

You'll need to enable SSH in both your Raspberry Pi and main machine, which can be found [here](https://www.raspberrypi.com/documentation/computers/remote-access.html#secure-shell-from-linux-or-mac-os) and [here](https://code.visualstudio.com/docs/remote/troubleshooting#_ssh-tips) respectively.

Then to access your Pi from Ubuntu
```Bash
ssh username@<ipaddress>
```

You'll be prompted to enter the user log in details, after which you should be met by the Raspberry Pi command prompt
![[Pasted image 20240225181858.png]]
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
```Shell
sqlite3 chinook/chinook.db
```

Run some basic commands to explore the database:
So view a catalogue of SQLite commands
```SQL
.help
```

See a list of tables in the database
```SQL
.tables
```

Show the databases SQLite has access to
```SQL
.databases
```

View the first 5 rows of the employees table
```SQL
SELECT * FROM employees LIMIT 5;
```