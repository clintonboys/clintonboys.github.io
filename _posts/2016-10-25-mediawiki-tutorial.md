---
layout: post
title: Installing MediaWiki on a DigitalOcean droplet (including Wikipedia navbars)
image:
  feature: sample-image-9.jpg
  credit: Cascade Mountains, Oregon, United States, 2013

---

This post will explain from scratch how to install MediaWiki on a DigitalOcean droplet, including how to set up Wikipedia-style navigation bars. It's something I needed to do for a project I'm working on in a volunteer capacity and I had a tough time finding resources so decided to write up a detailed explanation myself. 

1. Start up a DigitalOcean droplet
2. Install Apache webserver
3. Install MediaWiki
4. Edit LocalSettings.php to allow file uploads and change the logo
5. Install that package
6. Export Navbox, Navbar and HtmlModules

## 1. Start up a DigitalOcean droplet

DigitalOcean is a fantastic provider of VPC (virtual private cloud) services; it's basically a simplified version of AWS which has some great entry-level options for prototyping projects and playing with web services. We're going to use a very basic droplet for this tutorial:  

![Choose droplet](https://github.com/clintonboys/clintonboys.github.io/blob/master/_posts/mediawiki1.png?raw=true)
