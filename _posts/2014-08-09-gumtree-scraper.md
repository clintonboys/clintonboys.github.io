---
layout: post
title: Scraping Gumtree
image:
  feature: sample-image-9.jpg
  credit: Cascade Mountains, Oregon, 2013

---

Gumtree.com.au is a trading post website, largely used by private sellers interacting with each other off-site to sell used goods. One particularly common use for Gumtree is concert tickets: this is one of the main uses I have for it. 

The site is however fairly lightweight, and doesn't have any sort of notifications system for a particular search. So when looking for tickets to a particular concert, say, you have to search the site constantly and see if there are any new results.

I decided to learn some basic web-scraping techniques to write a script that did all this work for me. I wanted the following features:

1. To specify a keyword (e.g. "arctic monkeys"). 
2. To have the script crawl Gumtree every x minutes. 
3. To email me with any new results (within particular geographic areas or price brackets). 

## 1. Scraping Gumtree

I'd not done much web scraping before but I'd heard good things about BeautifulSoup in Python to parse the scraped html, together with the requests package to actually scrape the pages. Since I was looking for tickets to a particular show, I used the following parameters, which could of course be altered depending on the user's requirements:

    artist="arctic+monkeys"
    city="sydney"
    URL_START='http://www.gumtree.com.au'
    OFFER_CHOICE=['k0?ad=offering','k0?ad=wanted']
    ARTIST_URL="arctic+monkeys"#re.sub("\s",+,artist)

I then used the requests package to scrape a gumtree results page and dump the JSON output; this scrapes the nth result page (Gumtree limits to 10 results per pagee). 

    def scrape_gumtree_page_n(n):
        current_time=int(time.time())
        pageURL='{0}/s-{1}+{2}/page-{3}/{4}'.format(URL_START,ARTIST_URL,city,n,OFFER_CHOICE[0])
        savePath=os.path.join(scrapings_dir,"{0}.html".format(current_time))
        results=requests.get(pageURL)
        results_file=open(savePath,'w')
        with results_file:
            results_file.write(results.text.encode('utf-8',errors='ignore'))
        return savePath

There was then a simple while loop to run this over all results pages. 

## 2. Parsing JSON using BeautifulSoup

Having obtained a whole bunch of messy output from the scraper, I used the following code to parse using BeautifulSoup:

    def html_parser(filename):
        gumtree_file=open(filename)
        gumtree_contents=gumtree_file.read()
        gtsoup=BeautifulSoup(gumtree_contents)
	    master_list=[]
	    gt_li=gtsoup.findAll('li', attrs={'class': 'js-click-block'})
	    for node in gt_li:
	        if len(node.contents) > 0:
	            post_dict={}
	            if node.findAll('a') is not None:
	                post_dict['title']=node.findAll('a')[0].string
	            if node.find('div',attrs={"class":"h-elips"}) is not None:
	                post_dict['price']=node.find('div',attrs={"class":"h-elips"}).string
	            if node.findAll('span') is not None:
	                post_dict['description']=node.findAll('span')[0].contents[0]
	            if node.find('h3',attrs={"class":"rs-ad-location"}) is not None:
	                post_dict['location1']=node.find('h3',attrs={"class":"rs-ad-location-area"}).contents[0]
	            if node.find('span',attrs={"class":"rs-ad-location-suburb"}) is not None:
	                post_dict['location2']=node.find('span',attrs={"class":"rs-ad-location-suburb"}).contents[0]
	            if node.find('div',attrs={"class":"rs-ad-date"}) is not None:
	                post_dict['date']=node.find('div',attrs={"class":"rs-ad-date"}).contents[0]
	            anchors=node.findAll('a')
	            for node in anchors:
	                if node.get("data-adid") is not None:
	                    post_dict['ad_id']=node.get('data-adid')
	            master_list.append(post_dict)
	    return master_list


This returned things like

	{"ad_id": "1048303295", 
	 "description": "Selling: 2 Coldplay Tickets - Sydney 19 June ",
	 "title": null, 
	 "price": "\n500", 
	 "location2": "St Ives Chase", 
	 "date": "\n04/06/2014"}

which contains all the relevant information. This took me a while to write as I'd not dealt with JSON much before, so I had to figure everything out from scratch. It was very satisfying to run the parser successfully and have big page-sized chunks of horrible JSON condensed into little search result nuggets like the above.

## 3. Mandrill email automation

I wanted to run the scraper constantly in the background, preferably on an Amazon Web Server instance, and have it send automated emails every time it found a new result. 












