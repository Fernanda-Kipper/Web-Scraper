# Web-Scraper
Built using [Python](https://docs.python.org/3/), this Web Scraper has the aim of follow up the prices of an airline ticket in two different websites. 


## :warning: Prerequisites

-[Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

-[Selenium](https://www.selenium.dev/)

-[Time module](https://docs.python.org/3/library/time.html) 

-[Matplotlib](https://matplotlib.org/)

-[Numpy](https://numpy.org/doc/)

In order to use this bot on your computer, you should already have Python installed in your computer, the libraries mentioned above, [Geckodriver](https://github.com/mozilla/geckodriver/releases) and the [Firefox](https://www.mozilla.org/pt-BR/firefox/new/) web browser as well.

## :information_source: How it works

<img src="/images/initial.png" width="60%">
After start running the programm directly, the Scraping function will be called, this functionality will open the browser and after getting the html source from the first website to search the tag that holds the price-text and saving it into a variable, she will switch to the another web page for the same process. Then, the Writing_Down function will be called , the name speaks for it self, this one will write on the .txt file the results (formatted) founded on at the scraping. Last but not least, the Ploting_Results function (imported from the ploting_data file), will read all the information contained at the .txt file and plot it -I add some bonus at this plot, like the mean and standart deviation to improve the visualization of the results.
<img src="/images/plot_example.png" width="60%">







