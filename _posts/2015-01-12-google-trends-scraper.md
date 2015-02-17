---
layout: post
title: Scraping and joining Google trends searches
image:
  feature: sample-image-13.jpg
  credit: Wellington, New Zealand, 2014

---

If you search Google trends for a term like "taylor+swift", and set your timescale to "2004 to present", you'll get an interesting graph that does demonstrate the meteoric rise to stardom of the pop star. 

![Taylor swift](https://github.com/clintonboys/clintonboys.github.io/blob/master/_posts/taylorswift.png?raw=true)


Google also gives you an option to download the data as a .CSV file; this is a great option if you want to compare trends in a more rigorous way than looking at their graphs side by side.

However there's an issue with the timescales: if you download data from 2004 to present, Google will give you monthly or weekly data, but if you download data from June 2009, Google will give you daily data (unless it's negligable). 

I wrote a small script that searches Google trends for a certain term over a specified time frame, but does so over multiple small time intervals to obtain small time-scale data, and then stitches it all together using the full time scale for consistency. 

Because Google offers the option of downloading the results of a search as a .CSV file, we don't need any nasty scraping tools and can achieve everything in Python using just the webbrowser package.

    import webbrowser
    import time
    import os

The largest timeframe over which Google will return daily data is a quarter (three months). So we start by defining a function to get the data for a particular quarter simply by opening the relevant results.csv page with the webbrowser function; this will store the file in the /Downloads folder by default. 

    def ScrapeQuarter(keyword, year, q):
        print 'Scraping Q'+str(q)+' in '+str(year)
        URL_start = "http://www.google.com/trends/trendsReport?&q="
        URL_end = "&cmpt=q&content=1&export=1"
      
        queries = keyword[0]
        if len(keyword) > 1:
            queries_list = []
            for i in range(0,len(keyword)):
                queries_list.append(keyword[i])
            queries = '%20'.join(queries_list)
        
        quart_starts = [1,4,7,10]  
        
        date = '&date='+str(quart_starts[q-1])+'%2F'+str(year)+'%203m'
        
        URL = URL_start+queries+date+URL_end
            
        webbrowser.open(URL)    

Now we define a function that gets all quarters for a particular timespan and stores all the results files in a single folder (we sleep for two seconds in between each call to ScrapeQuarter or the browser gets very confused). 

    # WARNING: Before you run ScrapeRange, ensure your /Downloads folder
    # does not contain any .csv files. 

    def ScrapeRange(keyword, startq, startyear, endq, endyear):
        
        # First we create a directory to store the scraped .csv 
        # files, if one does not already exist. 
            
        scrapings_dir = 'gt_{0}'.format(keyword[0])
        if not os.path.exists(scrapings_dir):
            os.mkdir(scrapings_dir)

        new_filename_list = []

        for i in range(startq,4):
            ScrapeQuarter(keyword,startyear,i)
            new_filename_list.append('q'+str(i)+'_'+str(startyear))
            time.sleep(2)
        for y in range(startyear + 1, endyear):
            for i in range(1,5):
                ScrapeQuarter(keyword,y,i)
                new_filename_list.append('q'+str(i)+'_'+str(y))
                time.sleep(2)
        for i in range(1,endq+1):
            ScrapeQuarter(keyword,endyear,i)
            new_filename_list.append('q'+str(i)+'_'+str(endyear))
            time.sleep(2)
        
        path = '/Downloads'
        
        quarterly_files = [(os.path.getmtime(fn), os.path.basename(fn)) for fn in os.listdir(path) if fn.lower().endswith('.csv')]
                                    
        for i in range(0,len(quarterly_files)):
            os.rename(quarterly_files[i][1],new_filename_list[i])

