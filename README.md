Project playing with language replacement using spacy.io.

In the current version original text is Donald Trump's Inauguration speech, replacement text: scripts of ten different sci-fi movies.

**How it works?** After you choose the sci-fi movie below it autogenerates new inauguration speech by adding movie's POS to the original speech's POS. It's like if Frankenstein was giving a speech using the talk structure of Donald Trump.

**Python libraries used:** [BeautifulSoup to](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) scrape text from [IMSDB](http://www.imsdb.com/genre/Sci-Fi) site, [spacy.io POS tagging](https://spacy.io/docs/usage/pos-tagging) to generate new speech, [flask](http://flask.pocoo.org/) for website creation.

Original inauguration address can be found [here](https://www.whitehouse.gov/inaugural-address).
