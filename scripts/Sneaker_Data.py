import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Generate fake sneaker data
def generate_sneaker_data(num_rows):
    data = {
        'id': [fake.uuid4() for _ in range(num_rows)],
        'brand': [fake.company() for _ in range(num_rows)],
        'model': [fake.word() for _ in range(num_rows)],
        'size': [fake.random_int(min=6, max=14) for _ in range(num_rows)],
        'price': [round(fake.random_number(digits=4, fix_len=True) / 100, 2) for _ in range(num_rows)],
        'release_date': [fake.date_this_decade() for _ in range(num_rows)],
        'color': [fake.color_name() for _ in range(num_rows)]
    }
    return pd.DataFrame(data)

# Generate 100 rows of data
sneaker_df = generate_sneaker_data(100)
sneaker_df.head()
