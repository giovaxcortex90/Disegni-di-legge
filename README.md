# Disegni-di-legge #

**Automated Clustering of Similar Amendments in the Italian Senate**

## The problem ##

The Italian Senate is under a Denial-of-Service attack.
Software is being used to generate millions of amendments to block the passing of certain laws.
The amendments are generated using a black-hat technique that produces several variations of a given text.
This puts a huge strain on the Senate, which has to discuss and vote on the individual amendments, effectively bringing proceedings to a standstill.

## The solution ##

The Italian Senate makes its data available publicly.
An automated clustering analysis can be performed on these data to eliminate what are essentially duplicate amendments and reduce the total number of amendments that have to be considered.

![clusters.png](images/figuraCirinna.png)

## Installation and Usage ##

1. Clone this repository: `git clone https://github.com/giovaxcortex90/Disegni-di-legge.git`
2. Install the dependencies: `cd senato.py && pip install -r requirements.txt`
3. Fetch the amendments by running the scraper: `scrapy crawl cirinna`
4. Examine the analysis by running the notebook: `jupyter notebook cirinna.ipynb`

Autor Giovanni Battista Cortese
## License ##
