### Part 7 - Questions (and your Answers)

Acme Corporation isn't just a few `.py` files. If you want to grow in your
career here, you'll have to answer the following:

- What, in your opinion, is an important part of code reviews? That is, what is
  something you pay attention to when you review code, and that you appreciate
  when others do the same for your code?

  Answer
  -----

  The most important part of well written code, and therefore thing to be taken into consideration 
  during code review should be readability. There is a lot of talk about finding clever coding solutions 
  to problems and while they should be appreciated when appropriate, they become irrellevant if they 
  severely increase the amount of time needed to understand what is going on in the code. Infact you cannot 
  even begin a serious code review without that condition being fulfilled at least in a basic sense.
  If you cannot understand the flow of a program then it is impossible to give a serious critique of it
  since you would have no idea whats going on. Further, considerations like future iterations of a programs
  sans the original coder can become unnecessarily difficult if the code is not clean, legible and thouroughly
  documented

  
- We have an awful lot of computers here, and it gets pretty confusing with
  slightly different things running on all of them. How could containers help us
  improve this situation?

  Answer
  -----

  Containers provide a solution to the problem of conflicting local environments. When migrating programs
  from one environment to another whether from developer to developer, or developer to testing or testing to 
  production, differences in environments can prove fatal. Even those as simple as different network topologies.
  A container which consists of a portable runtime environemnt, eliminates the aforementioned issues and native
  OS issues become a thing of the past. Compared with virtual machines, containers also provide increases in 
  efficiency thanks to their smaller relative size, allowing a single server to host more containers than it could individual virtual machines. With increased efficiency comes and increase in production and possibilities since the containers are leaner they can be instantiated in an as needed basis and eliminated once they have fulfilled their role which allows the resources to be dedicated to other aspects of the program. Another large benefit of containers in an enterprise setting is that it will result in a more sanitized work enviornment for developers, because as code migrates throughout the enterprise the container
  poses no risk of damage to the local environments in which it is hosted.

Answer both of these questions (baseline ~5 sentences) here in text.