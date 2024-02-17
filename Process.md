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

Realise I need the Linux Kernel udpates