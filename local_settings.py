'''
Local Settings for a altright_ebooks account.
'''

#configuration
MY_CONSUMER_KEY = '5um9FIOCKYob2HAWtTeScYFkN'
MY_CONSUMER_SECRET = '09oVcQNTbfmc7rjyjJhWlDJBIJMYYZLBvcD51I1oxswvzKIs0t'
MY_ACCESS_TOKEN_KEY = '800928726556868608-qvyrYGOyhjXepOdQ4B0HnEO623u8OsR'
MY_ACCESS_TOKEN_SECRET = 'WtxUwKl8Fj3U6cz5PRYkZkQxMIHUZbi1Kvi3YKxc169EJ'

SOURCE_ACCOUNTS = [line.rstrip('\n') for line in open('secretsources.txt')]


ODDS = 1 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = "test_output.txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "altright_ebooks" #The name of the account you're tweeting to.
