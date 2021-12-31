import datetime
import os

now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
cwd = os.path.dirname(os.path.realpath(__file__))

inhabitants = 47326687 # https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176951&menu=ultiDatos&idp=1254735572981

# input down here the data corresponding to the real debt published for the previous quarters
# data extracted from: https://datosmacro.expansion.com/deuda/espana

if datetime.datetime.now() > datetime.datetime(datetime.datetime.now().year, 3, 31):
    year = datetime.datetime.now().year
else:
    year = datetime.datetime.now().year - 1

q1 = datetime.datetime(year, 3, 31)
q2 = datetime.datetime(year, 6, 30)
q3 = datetime.datetime(year, 9, 30)
q4 = datetime.datetime(year, 12, 31)

print(q1,q2,q3,q4)

previous_quarter_debt = 1432228 * 10**6
previous_quarter_minus_one_debt = 1424691 * 10**6
previous_quarter_minus_two_debt = 1393075 * 10**6

hours_per_quarter = int(91.25 * 24)
average_variation = (((previous_quarter_debt - previous_quarter_minus_one_debt) / hours_per_quarter) + ((previous_quarter_minus_one_debt - previous_quarter_minus_two_debt) / hours_per_quarter)) / 2

print(average_variation)



quarters = {(datetime.datetime(year, *args) - datetime.datetime.now()).days + 1: datetime.datetime(year, *args) for args in ((3, 31), (6, 30), (9, 30), (12, 31))}

days_since_last_quarter_closure = abs(max(list(quarters.keys())))
hours_since_last_quarter_closure = datetime.datetime.now().hour + days_since_last_quarter_closure*24


print(year)
print(days_since_last_quarter_closure)
print(hours_since_last_quarter_closure)