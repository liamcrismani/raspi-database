# Raspberry Pi Database

## Project Overview

Connect to a Raspberry Pi over SSH, migrate the Chinook database from SQLite to PostgreSQL, and slice and dice your data.

## Project goals

 - Set up a Raspberry Pi (doesn't have to be headless) 
 - Load the [Chinook database](https://www.sqlitetutorial.net/sqlite-sample-database/) on SQLite  
 - Migrate the data to a PostgreSQL database
 - Bonus: plot some data  

To see how these goals have changed, check [the blog](https://github.com/liamcrismani/raspi-database/blob/main/blog.md#original-goals)
## Motivation

This project originated as prep for a job interview. I was tasked with preparing a presentation for the interview. The presentation topic was set as:

> A key part of this role will be to support the development and implementation of new data management systems and procedures.
> Please tell us why this interests you and give us an example of a time when you used skills that will support you in this aspect of the role.

So I had the bright idea of creating a database project to talk about in my interview. Ultimately, the project failed in most aspects as I hit multiple sticking points. 7 months older and wiser, I am revisiting the project.

This project seeks to explore remote computing, Linux and WSL, SQL databases, Git and GitHub for project management, Bash, and Markdown editing.

## Limitations and challenges

A full list of personal struggles with this project can be found [here](https://github.com/liamcrismani/raspi-database/blob/main/blog.md#sticking-points) TLDR;
- SHH connection to Raspberry Pi can be tricky if you add unnecessary layers of complexity
- Trying to create a database from unrelated datasets will make your life difficult

## Intended use

Good if you want to get your feet wet with WSL, SSH to a remote computer, and SQL databases from the command line.

## Repo contents  

- [/chinook](/chinook): database file
- [blog.md](blog.md): markdown blog documenting project progress. Awkward blend of narrative and instructions.
- [data_visualisation.ipynb](data_visualisation.ipynb): notebook that connects to and visualises data from the database

## Credits
**WSL tutorials**
[Get started with WSL](https://learn.microsoft.com/en-us/windows/wsl/). Install distros, set up development environments, and get started with git in WSL.

**Raspberry Pi tutorials**
[Raspberry Pi documentation](https://www.raspberrypi.com/documentation/): Set up a Raspberry Pi, connect over SSH, and use secure copy.

**Other repos viewed but not used**
https://github.com/lerocha/chinook-database

**SQLite tutorials**
Install and start SQLite, set up a database, and use basic SQL commands: https://www.sqlitetutorial.net/
