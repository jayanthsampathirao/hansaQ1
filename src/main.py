import pandas as pd
from datetime import datetime
from src.database import create_table, connect_db
from src.models import Person
from src.calculations import project_earnings

# Load data
df = pd.read_csv("data/sample_population.csv")

create_table()
current_date = datetime(2025, 3, 1) 

total_population_earnings = 0

# Database connection
conn = connect_db()
cursor = conn.cursor()

for _, row in df.iterrows():
    person = Person(row["id"], row["name"], row["gender"], row["dob"], row["salary"])
    work_months = person.get_remaining_work_months(current_date)
    projected_earnings = project_earnings(person.salary, work_months)
    
    print(f"Person: {person.name}, Projected Earnings: {projected_earnings:.2f}")
    total_population_earnings += projected_earnings

    # Insert data into the database
    cursor.execute("""
        INSERT INTO earnings (id, name, gender, dob, salary, projected_earnings)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (person.id, person.name, person.gender, person.dob.strftime("%Y-%m-%d"), person.salary, projected_earnings))
conn.commit()
conn.close()

print(f"\nTotal Projected Earnings for Population: {total_population_earnings:.2f}")
