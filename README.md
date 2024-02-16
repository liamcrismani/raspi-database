# Raspberry Pi Database project

## Project overview
This project originated as prep for a job interview. I was tasked with preparing a presentation for the interview, the topic of which was set as:

> A key part of this role will be to support the development and implementation of new data management systems and procedures.
> Please tell us why this interests you and give us an example of a time when you used skills that will support you in this aspect of the role.

My first idea, for better or worse, was to create a database project. Ultimately the project failed in most aspects, but I was fortunate enough to get the job, thanks in part to the fact that I was willing to talk openly about how and why the project failed.
Fast forward 7 months, and I am reviving the project.

## Project goals
### Original goals
The original project definition was:  
 - set up a headless Raspberry Pi  
 - connect to the Pi through SSH from an Ubuntu VM on my Windows machine(I thought this was a good idea as this was how I connected to a bitcoin node I had run on the Pi previously...)  
 - set up a SQLite database
 - pull the data off the SQLite db  
 - perform some data cleaning w/ Python  
 - migrate the clean data onto a PostgreSQL db  
 - Bonus: do a live pull of some data and plot a pretty graph  

I was rapidly overwhelmed, however, and hit a lot of sticking points that made me realise the goals were a little too lofty.  
#### Sticking points
**Couldn't connect to the Raspberry Pi over SSH through the Ubuntu VM**  
I'd managed this before when running a Bitcoin node, but that was over a different ISP where enabling port-forwarding was a bit simpler.  

**Getting data**  
Being fairly new to the world of databases, I was surprised by how difficult I found it to find a dataset. I didn't know where to look.  
I ended up settling for some datasets I pulled off Kaggle, these were [[https://www.kaggle.com/datasets/datascientistanna/customers-dataset|shop customer data]], [[https://www.kaggle.com/datasets/thedevastator/urban-coyote-activity-and-diet-data-during-covid|urban ecology over time]], [[https://www.kaggle.com/datasets/thedevastator/weed-plant-taxonomy-in-france-and-uk|weeds in cultivation fields]].
The idea was that the data would be something akin to what the company I was interviewing for would used, ie.e:  
- Something operational  
- Something ecological  
- Something relational.  
With a key factor of this project being that the database would be relational, it was quite comical how long it took me to realise the data I had gathered wasn't relational.  

**Creating the database**  
At the point of starting the project I had learned some basic Python and SQL, and felt fairly confident that I could, with enough time and resources, create a very simple database connection in Python. That confidence faded quickly. I had already stumbled at the first two hurdles, so it didn't take long for me to struggle with this and decide to revise the project goals.  


### Revised goals  
 - No Raspberry Pi, create the databases and perform the migration locally  
 - Write a Python script to retrieve the datachange it so that it fits an appropriate schema  
 - Use the Holywell style guide for the SQL code  
 - Bonus: perform a quick data pull and plot a graph  

#### More problems  
- Couldn't set up the SQLite database  
- Couldn't set up the PostgreSQL database  
- The data is not relational!  

Despite refreshing the plan and setting more reasonable goals, I continued to struggle. The interview date was moving closer, I was still in a full time job, and my anxiety levels were rising.  
I would say I was wondering why I had set such an ambitious target, but I really did think the original project remit was achievable.  
I also thought that the project based approach would give me exactly what I needed to point to for the presentation topic definition.  

### Where and why I got stuck first time around
Reflecting on the original project, I think the main reasons I met the challenges I did were:  
**Lack of technicall skills**  
If I was a whizz with Python and SQL at the time, the technical work would have been a walk in the park. It's not a particularly difficult task, but I put hurdles in that I didn't need to, and some hurdles I didn't predict.  

**No good project management system**  
The project was spread across Notion, word documents, paper, powerpoint, and my head. I even set the ludicrious goal of creating the presentation with Quarto, which I head never used before.  
As someone who needs simple systems, this was enough to set my head spinning. Thankfully, this time around I have a bit more experience with the wonderfully simple but powerful markdown. And git. Both of which I intend to leverage heavily for version 2.  

**Anxiety**  
This was my first proper, proper job interview. I'd had a few before, but they didn't require this level of preperation, and only really needed my to turn up and be myself. One did include a swim test actually.  
I also really, really wanted this job.

### What I plan to do differently this time
As just mentioned, I'll leverage git and GitHub. I'll use some branches for different aspects of the project.  
I'll also dedicate time to the project in a more stuctured way.

## v2 goals
 - Set up a Raspberry Pi (doesn't have to be headless)  
 - Document the whole process with markdown files and git  
 - Use the [[Chinook database]], so I don't have to worry about schema and getting data  
 - Set the Chinook database up on SQLite  
 - Migrate the data to a PostgreSQL db  
 - Bonus: plot some data  

These goals are very similar to the orignal remit, but 7 months has passed, and I think I have the time and skillset to make it happend this time.  

