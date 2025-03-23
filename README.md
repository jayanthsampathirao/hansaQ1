There are two major Files in the solution
1.data

2.src

data should be potentially having all the csv files to proceed to the further operations

src is having 4 files namely 
1.calculations.opy
2.database.py
3.main.py
4.models.py

Each of the file performs diffrent operations 
1.calculations.opy -> calculates the expected earnings over remaining months with inflation adjustment 
2.database.py -> create tables , create connection 
3.main.py -> reads csv file , calculate each person earnings ,  store result in database 
4.models.py -> schema

5.where as cofig.py does store values which are imported across the code 

6.libraries used  : 
psycopg2       # PostgreSQL database adapter for Python -> database.py
pandas         # For handling CSV data -> main.py
numpy          # For numerical calculations -> calculation.py 
