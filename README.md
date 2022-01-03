# Spanish Debt Counter 

This is a simple script that calculates the public spanish debt using moving averages ~~and linear regressions~~[^1]. Once the data is compiled and calculated it goes on a twitter bot account. It can be seen working [here](https://twitter.com/deudapublicaes1).

## Data

Until the moment I figure out a public API with the current debt date (please do let me know if you know any), some of the variables have to be updated by hand on a quarterly basis. The inline comments of the code shows details about this.

### Which variables require manual updating?

- `inhabitants`: latest number of inhabitants of Spain, provided by INE ([link](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176951&menu=ultiDatos&idp=1254735572981))

- `gdp`: Spanish GDP updated to the latest year ([link](https://datosmacro.expansion.com/pib/espana))

- `previous_quarter`: the date of the last quarter end from which the latest published real debt figures have been gathered `(YYYY, MM, DD)`

- `previous_quarter_debt`: the actual figure of the published debt for the last quarter

- `previous_quarter_minus_one_debt`: same as above, latest quarter -1

- `previous_quarter_minus_two_debt`: same as above, latest quarter -2



[^1]: I haven't managed yet how to figure it out linear regressions for this little amount of data with Python, I will sort it out once I manage. Alternatively, if you have any suggestions please feel free to open an issue or dm me
