import tweepy
import wordcloud
from Credentialstwitter import *
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
api = tweepy.API(auth)
text = " "

tweets = api.user_timeline(screen_name ="maiconkusterkkk", count=1000, include_rts = False, tweet_mode = "extended")
for tweet in tweets:
    #print(tweet.full_text)
    text = text + " " + tweet.full_text

wordcloud = WordCloud(width=1920, height=1200)
STOPWORDS.update(["hppt", "https", "co", "da","de","em","na","se","às","como","que", "para", "os", "dos", "das", "assim", "quais","feira","um", "uma", "mais", "ao", "por","pelo","pela",\
    "como", "nosso", "nossa", "zu", "das", "zu","die","der","dem","und","auf","ein","nicht","von","wie","wird", "daß", "dass","mit","für", "Sie","sie","er","noch","vor","ist", "bei",\
    "wenn", "sich", "den", "hat", "des", "diese", "diesen", "dieses", "dieser", "über", "eine", "einer", "einen", "eines", "auch", "es", "werden", "auch", "im", "als", "uns", "sehr",\
    "aber", "einem", "zur", "nun", "mehr", "zum", "durch", "sind", "kann", "man", "aus", "nur", "haben", "will", "é" ])
wordcloud.generate(text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
