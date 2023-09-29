import datetime
import os
import tweepy
import credentials

now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
cwd = os.path.dirname(os.path.realpath(__file__))

inhabitants = 47615034 # https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176951&menu=ultiDatos&idp=1254735572981
gdp = 1328922 * 10**6 # https://datosmacro.expansion.com/pib/espana

# input down here the data corresponding to the real debt published for the previous quarters
# data extracted from: https://datosmacro.expansion.com/deuda/espana

previous_quarter = datetime.datetime(2023, 6, 30) # the date in YYYYMMDD format (leading zeroes not allowed) corresponding to the last quarter the information is provided
previous_quarter_debt = 1568743 * 10**6 
previous_quarter_minus_one_debt = 1535385 * 10**6
previous_quarter_minus_two_debt = 1502804 * 10**6

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

# authentication
client = tweepy.Client(
                    bearer_token=credentials.bearer_token,
                    consumer_key=credentials.consumer_key,
                    consumer_secret=credentials.consumer_secret,
                    access_token=credentials.access_token,
                    access_token_secret=credentials.access_token_secret
                    )

client.create_tweet(text = '{} € total | '
                           '{} € por habitante | '
                           '{}% del PIB | '
                           '{} #DeudaPublica'.format(debt_readable, debt_per_inhabitant_readable, percentage_readable, now))
