---
layout: post
title: An observed life II - building a basic tracking application
image:
  feature: sample-image-34.jpg
  credit: Panjim, Goa, India, 2015. 
---

In this post I will describe how I put together a very simple application (this word is used in a loose sense that will be clarified below) allowing me to track a number of variables for my observed life [project](http://www.clintonboys.com/observed-life-1/). 

The basic idea is simple: I set up a DigitalOcean server which runs a Python script once a minute to scan my Gmail inbox and look for new emails based on certain keywords. It then parses these emails, extracts the relevant data and inserts it into a MySQL database running on the same server. I then installed [redash](https://github.com/getredash/redash), a great nofrills visualization layer which allows me to view all the data that I have collected. The final step is writing more code which pulls data from all my non-manual sources (iTunes, Chrome, Nike Plus, Moment, MyFitnessPal, Google Sheets) and stores them in the same database with access to the same visualization layer. 

The code is all available on a [Github](https://github.com/clintonboys/life-tracker) repository (note: currently private). 

**The server**

DigitalOcean is a fantastically simple VPC service with none of the complexity and ugliness of AWS (worth mentioning it also has far fewer features). I spun up their $5US/month server (what a modern miracle) which has 512MB of RAM, a single core CPU, 1 20GB SSD and offers 1TB/month of data transfer. I chose Ubuntu 14.04 as the operating system as it has the easiest time coping with MySQL. 

Once the instance is created (note that it runs Python 2.7 out of the box), I needed to run the following commands in order to install MySQL (I've collected them here as I couldn't find them all written down in the one place anywhere online).

```
sudo apt-get update
sudo apt-get install mysql-server
sudo mysql_secure_installation
sudo mysql_install_db

sed --in-place '/skip-external-locking/d' /etc/mysql/my.cnf
sed --in-place '/bind-address/d' /etc/mysql/my.cnf

/sbin/iptables -A INPUT -i eth0 -p tcp --destination-port 3306 -j ACCEPT

sudo /etc/init.d/mysql start
```

The server is now running and with `mysql -h localhost -u root -p` we can start to build the database. 





