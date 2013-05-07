Twitter-Sentiment-Analysis
==========================

An analysis of the sentiments of tweets using the Twitter API for my data science class

To get started, run <strong>twitterstream.py</strong> for a any specific time (i.e. 10 minutes) and output it into a textfile:

<pre><code>$ python twitterstream.py > output.txt </code></pre>

<strong>Tweet_sentiment.py, term_sentiment.py</strong>, and <strong>happiest_state.py</strong> all have 2 parameters: the predetermined sentiment file and the tweet file. For example:

<pre><code>$ python tweet_sentiment.py AFINN-111.txt output.txt </code></pre>

<strong>Frequency.py</strong>, and <strong>top_ten.py</strong> only require the tweet file:

<pre><code>$ python top_ten.py output.txt </code></pre>
