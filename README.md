# MathaBotFace

A Python script tweeting about mathematics theorems, lemmas and inequalities extracted from wikipedia

# Requirements

* `python3`, `pip` (for arch, `pacman -S python python-pip`)
* python library `wikipedia` (`sudo pip install wikipedia`)
* To tweet: python library `twython` ( `sudo pip install twython`)
* to add shortened urls: `tinyurl` (`sudo pip install TinyURL3`). Added the TinyURL.py from the TinyURL3 git in case the installation fails. So, this part is unnecessary. However, to use this file, you need `beautifulsoup4`, so install it using `sudo apt-get install python3-bs4` (for ubuntu)
 
* These files:  `git clone http://github.com/debdeepbh/MathBotFace && cd MathBotFace`
* Set up a twitter app account with access key, token, consumer key and consumer secret and update it in the file `tweet.py`.


# Usage
* `python fetchWiki.py` to get the titles from wikipedia (which stores it in .DAT files)
* To print a random article on terminal, `python wikiOut.py` or `python wikOut.py inequalities` (with parameter)
* Available parameters for now: `theorems, lemmas, inequalities`
* The default number of characters for the summary is set to 300. Edit the variable `num` in the file to change it.
* To tweet, fill up the Twitter credentials in `tweet.py` and run it with or without a parameter (e.g. `python tweet.py lemmas`)

