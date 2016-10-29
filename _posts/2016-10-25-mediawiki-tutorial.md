---
layout: post
title: Installing MediaWiki on a DigitalOcean droplet (including Wikipedia navbars)
image:
  feature: sample-image-9.jpg
  credit: Cascade Mountains, Oregon, United States, 2013

---

This post will explain from scratch how to install MediaWiki on a DigitalOcean droplet, including how to set up Wikipedia-style navigation bars. It's something I needed to do for a project I'm working on in a volunteer capacity and I had a tough time finding resources so decided to write up a detailed explanation myself. Here I'm assuming you're using MacOS or Unix (i.e. some OS with a Unix-based terminal). 

1. Start up a DigitalOcean droplet
2. Install Apache webserver
3. Install MediaWiki
4. Edit LocalSettings.php to allow file uploads and change the logo
5. Install that package
6. Export Navbox, Navbar and HtmlModules

## 1. Start up a DigitalOcean droplet

DigitalOcean is a fantastic provider of VPC (virtual private cloud) services; it's basically a simplified version of AWS which has some great entry-level options for prototyping projects and playing with web services. We're going to use a very basic droplet for this tutorial: the 512MB RAM, single CPU option, which is enough for prototyping. Anything more serious and you'll need to scale up the droplet, which is very easy to do later. Notice we're picking **Ubuntu 14.04.5 x64** as our OS. 

![Choose droplet](https://github.com/clintonboys/clintonboys.github.io/blob/master/_posts/mediawiki1.png?raw=true)

You don't need to add an SSH key (unless you're really worried about security on your wiki), and you should choose whichever datacenter region is relevant to you. Click Create droplet and you should see the instance spinning up in your list:

![New instance](https://github.com/clintonboys/clintonboys.github.io/blob/master/_posts/mediawiki2.png?raw=true)

DigitalOcean have just sent you an email with the root password to your instance: so go to your terminal and 

`ssh root@XXX.XXX.XXX.XXX`

where the XXXs represent the IP of your new instance. You'll need to type / copy the password from the email, and be prompted to change passwords.

## 2. Install Apache webserver

Now you're inside your new instance, we need to install Apache 
