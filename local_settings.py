'''
Local Settings for a altright_ebooks account.
'''

#configuration
MY_CONSUMER_KEY = '5um9FIOCKYob2HAWtTeScYFkN'
MY_CONSUMER_SECRET = '09oVcQNTbfmc7rjyjJhWlDJBIJMYYZLBvcD51I1oxswvzKIs0t'
MY_ACCESS_TOKEN_KEY = '800928726556868608-qvyrYGOyhjXepOdQ4B0HnEO623u8OsR'
MY_ACCESS_TOKEN_SECRET = 'WtxUwKl8Fj3U6cz5PRYkZkQxMIHUZbi1Kvi3YKxc169EJ'

SOURCE_ACCOUNTS = [line.rstrip('\n') for line in open('secretsources.txt')]


ODDS = 32 #How often do you want this to run? 
ORDER = 2 #Markov order. 1 = nonsense 3 = coherent 
DEBUG = False #If false, tweets live
STATIC_TEST = False #If True, doesn't use API - pulls from static file
TEST_SOURCE = "test_output.txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "altright_ebooks" #The name of the twitter account of this ebook
