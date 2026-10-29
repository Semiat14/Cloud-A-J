# Week 3 · Day 1 · Processes, systemd & my first web server

Today Linux started feeling less like a list of commands and more like a system.

## Processes
A process is basically a program that's running right now. Every one gets its own number (a PID).
I think of it like a kitchen: the program is the recipe, the process is the dish being cooked,
and the PID is the order number.

I ran `ps aux` to see everything running on my machine. PID 1 is `init`, the first process,
which starts everything else. Then I started `sleep 500 &` in the background, found it with
`ps aux | grep sleep`, and killed it with `kill 1300`. Seeing "Terminated" was weirdly satisfying.

## systemd
Some programs need to run all the time, like web servers. Those are services, and systemd is
the manager that keeps them alive. I control them with `systemctl`:
start, stop, restart, status. `enable` just means "start this automatically when the machine boots."

## My first web server 🎉
Installed Nginx with `sudo apt install nginx`, opened http://localhost, and there it was:
"Welcome to nginx!" Stopped it, refreshed, gone. Started it, back again. Like a light switch.

Then I replaced the default page with my own. That took a few tries, honestly. I typed a backtick
instead of an apostrophe, forgot a closing quote, and used `?` instead of `|`. Every time, bash just
sat there showing `>`, waiting for me to finish. Ctrl+C got me out each time.

What finally worked:
`echo "<h1>Hi, I am Semiat...</h1>" | sudo tee /var/www/html/index.html`

I needed `tee` because that folder belongs to root, and a normal `>` would have run as me.

**Takeaway:** a website is really just a web server pointing at a folder of files.
Next week I'm doing this on a real server in AWS. 🚀
