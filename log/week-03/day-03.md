# Week 3 · Day 3 · My first server on AWS 🚀

This one took a few sessions, but I finally have a real server running in the cloud.

## Launching it
I followed Stephane Maarek's EC2 videos and launched an Amazon Linux instance in Stockholm,
with a user data script that installs Apache (httpd) and writes my own page on first boot.
It's the same steps I did on my laptop with Nginx, just different names: yum instead of apt,
httpd instead of nginx.

First problem: the launch page said "no VPC found." Turns out the default VPC was missing
its subnets after my Day 2 teardown. No street, no house. Fixed that and it launched.

## Getting in
SSH failed the first time. I'd typed `.EC2Tutorial.pem` with an extra dot, and the key was
still sitting in my Windows Downloads folder. Copied it into `~/.ssh`, ran `chmod 400`, and
I was in. Logging into a server in Sweden from my laptop in Abuja felt unreal.

Also learned there are two keys in SSH: the server's host key (proves it's the right server)
and mine (proves it's me).

## The internet found my server
Apache said "Total requests: 543" after 2 days. That wasn't me. The access log was full of
bots: scanners like zgrab, someone looking for `/.env` (where people accidentally leave
passwords), probes for random apps. All 404s, nothing to find. Lesson: every public server
gets poked at within hours, so lock SSH to your own IP and never leave secrets lying around.

## Breaking it on purpose
Removed the port 80 rule from the security group, and the site just spun until it timed out.
But `curl localhost` on the server still worked. The app was fine; the firewall was blocking it.

**Timeout = security group. Connection refused = the app isn't running.**

Added the rule back, then terminated the instance. (I'd left it running since Monday, which is
a habit I'm fixing: always terminate after a lab.)

**Next:** Bash scripting + Git from the terminal.
