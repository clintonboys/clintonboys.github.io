---
layout: post
title: An observed life II - building a basic tracking application
image:
  feature: sample-image-34.jpg
  credit: Panjim, Goa, India, 2015. 
---

In this post I will describe how I put together a very simple application (this word is used in a loose sense that will be clarified below) allowing me to track a number of variables for my observed life [project](http://www.clintonboys.com/observed-life-1/). 

The basic idea is simple: I set up a DigitalOcean server which runs a Python script once a minute to scan my Gmail inbox and look for new emails based on certain keywords. It then parses these emails, extracts the relevant data and inserts it into a MySQL database running on the same server. I then installed [redash](https://github.com/getredash/redash), a great nofrills visualization layer which allows me to view all the data that I have collected. There will also be a simple reminder system which sends me emails when I haven't logged a data point in a while. The final step is writing more code which pulls data from all my non-manual sources (iTunes, Chrome, Nike Plus, Moment, MyFitnessPal, Google Sheets) and stores them in the same database with access to the same visualization layer. 

This is the reason I'm hesitant to call this an application: it's just a very hacky service managed by email. The code is all available on a [Github](https://github.com/clintonboys/life-tracker) repository (**note**: currently private). 

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

**The database**

I ran `create database clinton;` and then created a number of tables for the specific metrics I'm going to want to track manually. Here I'll use the example of the table `mood` which stores measurements of my mood throughout the day on a scale from 1 to 10. 

```
CREATE TABLE clinton.mood
(tsDate DATETIME,
 mood INT, 
 notes VARCHAR(500));
```

I created a number of other tables but I'll focus on this one for the post. We need finally to run 

```
grant all privileges on * . * to root@'%' identified by XXXXX with grant option;
flush privileges;

apt-get install git
apt-get install python-pip
pip install pymysql
```

in order that Python will be able to read and write to the table. The final step is the following Python code, which reads my Gmail inbox, parses relevant emails, and writes them to the MySQL table defined above. 

Metrics are organised into `domain` (in the mood example: self), `subdomain` (mood), `operation` (allows for incremental updates or inserting new values), `update` (the actual value), `note` (any associated text information or metadata) and `time` (the timestamp associated with the data). The emails are caught by being sent to `name+domain@gmail.com`; helpful behaviour that Gmail allows. Mail is deleted from the inbox after being processed. 

The text is parsed by spaces; for example I can send an email to `name+self@gmail.com` with subject `mood set 5 sick-with-cold 2016-09-27 08:00:00`. Parsing can obviously be made more sophisticated without too much effort. 

The script is then scheduled to run every minute using `cron` with `* * * * * cd /root/an-observed-life; /usr/bin/python an-observed-life.py`.

--

```
import pymysql
import datetime
import imaplib
import getpass
import email
from config import mysql_connection_info, gmail_credentials
import logging

logging.basicConfig(filename='service.log', level=logging.INFO)

def gmail_connect():

    ### Connect to Gmail over IMAP4 and return a 
    ### list and count of unread messages

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(gmail_credentials['user'],gmail_credentials['pwd'])
    mail.list()
    resp, no_messages = mail.select('"Inbox"')
    return mail, int(no_messages[0])

def mysql_connect():

    ### Connect to MySQL and return the cursor and
    ### connection objects. 

    conn = pymysql.connect(host = mysql_connection_info['host'],
                           port = mysql_connection_info['port'],
                           user = mysql_connection_info['user'],
                           password = mysql_connection_info['password'])
    cur = conn.cursor()
    cur.execute('use clinton;')
    return cur, conn

def parse_to_dict(string):

    ### Parse an email body string to a Python dict

    dst_hours = 3

    domain = string.split(' ')[0]
    subdomain = string.split(' ')[1]
    operation = string.split(' ')[3]
    update = string.split(' ')[2]
    try:
        note = string.split(' ')[4]
    except:
        note = ''
    time = datetime.datetime.now() + datetime.timedelta(hours = dst_hours)
    # default to now if no timestamp is included
    try:
        if len(' '.join(string.split(' ')[5:])) > 2:
            time = ' '.join(string.split(' ')[5:])
    except:
        pass
    try:
        return {'domain': domain, 'subdomain': subdomain, 'operation': operation, 'update': update, 'note': note, 'time': time}
    except Exception, e:
        logging.warning('{0}:Could not parse string {1}. Error: {2}'.format(datetime.datetime.now(), string, str(e)))
        return None


def main():
    logging.info('{0}:Running service...'.format(datetime.datetime.now()))
    logging.info('{0}:Connecting to Gmail...'.format(datetime.datetime.now()))
    try:
        mail, no_messages = gmail_connect()
        logging.info('{0}:Connection successful!'.format(datetime.datetime.now()))
    except Exception, e:
        logging.warning('{0}:Connection unsuccessful... Error message: {1}'.format(datetime.datetime.now(), str(e)))
        return 'Failure.'
    logging.info('{0}:Connecting to MySQL...'.format(datetime.datetime.now()))
    if no_messages > 0:
        try:
            cur, conn = mysql_connect()
            logging.info('{0}:Connection successful!'.format(datetime.datetime.now()))
        except Exception, e:
            logging.warning('{0}:Connection unsuccessful... Error message: {1}'.format(datetime.datetime.now(), str(e)))
            return 'Failure.'

        found_messages = 0
        for i in range(1,no_messages + 1):
            try:
                domain = mail.fetch(str(i), '(RFC822)')[1][0][1].split('\nTo: ')[1].split('@')[0]
                if domain.split('+')[1] == 'self':
                    found_messages += 1
                    logging.info('{0}:Found new message in domain self'.format(datetime.datetime.now()))
                    input_string = 'self '+ mail.fetch(str(i), '(RFC822)')[1][0][1].split('Subject: ')[1].split('\r\n')[0]  
                    this_dict = parse_to_dict(input_string)
                    print this_dict

                    ## self:mood

                    if this_dict['subdomain'] == 'mood':
                        if this_dict['operation'] == 'set':
                            ## We can insert a new mood value with the set operation
                            query = '''insert into mood values (\'{0}\',{1},\'{2}\');'''.format(this_dict['time'],int(this_dict['update']), this_dict['note'])
                        else:
                            ## We can update the most recent value with the specified increment using the up and down operations. 
                            get_mood_query = '''select mood from mood order by tsDate desc limit 1'''
                            cur.execute(get_mood_query)
                            current_mood = int([row for row in cur][0][0])
                            if this_dict['operation'] == 'up':
                                query = '''insert into mood values (\'{0}\',{1},\'{2}\');'''.format(this_dict['time'],int(this_dict['update'])+current_mood, this_dict['note'])
                            elif this_dict['operation'] == 'down':
                                query = '''insert into mood values (\'{0}\',{1},\'{2}\');'''.format(this_dict['time'],current_mood-int(this_dict['update']), this_dict['note'])

                try:
                    cur.execute(query)
                    logging.info('{0}:Insert successful!'.format(datetime.datetime.now()))
                    result = mail.store(str(i), '+FLAGS', '\\Deleted')
                    mov, data = mail.uid('STORE', str(i), '+FLAGS', '(\Deleted)')
                    mail.expunge()
                    logging.info('{0}:Mail archive successful!'.format(datetime.datetime.now()))
                except Exception, e:
                    logging.warning('{0}:Insert failed... Leaving mail in inbox. Error: {1}'.format(datetime.datetime.now(), str(e)))
                    pass
            except:
                pass

        logging.info('{0}:Successfully inserted {1} new entries!'.format(datetime.datetime.now(), str(found_messages)))
        conn.commit()
        conn.close()
        logging.info('{0}:MySQL connection closed.'.format(datetime.datetime.now()))
        mail.logout()
        logging.info('{0}:Gmail connection closed.'.format(datetime.datetime.now()))
        return 'Success.'
    else:
        logging.info('{0}:No new messages found.'.format(datetime.datetime.now()))
        mail.logout()
        logging.info('{0}:Gmail connection closed.'.format(datetime.datetime.now()))
        return 'Success.'

if __name__ == '__main__':
   main()
```







