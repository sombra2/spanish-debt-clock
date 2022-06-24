import datetime
import os
import tweepy
import credentials

now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
cwd = os.path.dirname(os.path.realpath(__file__))

inhabitants = 47432805 # https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176951&menu=ultiDatos&idp=1254735572981
gdp = 1202994 * 10**6 # https://datosmacro.expansion.com/pib/espana

# input down here the data corresponding to the real debt published for the previous quarters
# data extracted from: https://datosmacro.expansion.com/deuda/espana

previous_quarter = datetime.datetime(2022, 3, 31) # the date in YYYYMMDD format corresponding to the last quarter the information is provided
previous_quarter_debt = 1453853 * 10**6 
previous_quarter_minus_one_debt = 1427235 * 10**6
previous_quarter_minus_two_debt = 1432339 * 10**6

hours_per_quarter = int(91.25 * 24)
average_variation_per_hour = (((previous_quarter_debt - previous_quarter_minus_one_debt) / hours_per_quarter) + ((previous_quarter_minus_one_debt - previous_quarter_minus_two_debt) / hours_per_quarter)) / 2
average_variation_per_second = average_variation_per_hour / 3600

debt = (((datetime.datetime.now() - previous_quarter).total_seconds()) * average_variation_per_second) + previous_quarter_debt
debt_readable = '{0:,}'.format(int(debt)).replace(',', '.') # adding the thousands separators for better readability
percentage = round((int(debt) * 100) / gdp, 2)
percentage_readable = '{0:,}'.format(percentage).replace('.', ',') # adding the thousands separators for better readability
debt_per_inhabitant = round(int((debt / inhabitants)),2)
debt_per_inhabitant_readable = '{0:,}'.format(debt_per_inhabitant).replace(',', '.') # adding the thousands separators for better readability

# Now the part where we send the tweet

consumer_key = credentials.consumer_key
consumer_secret = credentials.consumer_secret
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api.update_status(status = '{} € total | '
                           '{} € por habitante | '
                           '{}% del PIB | '
                           '{} #DeudaPublica'.format(debt_readable, debt_per_inhabitant_readable, percentage_readable, now))
