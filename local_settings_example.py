'''
Local Settings for a altright_ebooks account.
'''

#configuration
MY_CONSUMER_KEY = ''
MY_CONSUMER_SECRET = ''
MY_ACCESS_TOKEN_KEY = ''
MY_ACCESS_TOKEN_SECRET = ''

SOURCE_ACCOUNTS = [] #a list of twitter accounts in quotes seperated by commas


ODDS = 1 #How often do you want this to run? 1/ODDS
ORDER = 2 #Markov order. 1 = nonsense 4 = coherent 
DEBUG = True #If false, tweets live
STATIC_TEST = False #If True, doesn't use API - pulls from static file
TEST_SOURCE = "" #a text file of python string lists tweets for testing without hitting twitter API
TWEET_ACCOUNT = "" #The name of the twitter account of this ebook
LOGS = "" #a txt file which the program will "print" to, allowing better debugging when running on the cloud
