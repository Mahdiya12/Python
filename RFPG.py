import random

# --- Data Lists ---
fname = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth']
lname = ['Elizabeth', 'Laura', 'Jennifer', 'Kimberly', 'Adam', 'Stuart', 'Nikola', 'Thor', 'Hulk', 'Ruskin', 'Thor', 'Rocky', 'David', 'David', 'Harris', 'Elon', 'Elon', 'Mark', 'Will', 'Chris', 'Brown', 'Wilson', 'Jukerberg', 'Anderson']
street_name = ['Main', 'Potter', 'Jukerberg', 'Smith', 'Nebula', 'Dowty', 'Down', 'Jr', 'High', 'Washington']
city_name = ['Miami', 'Hialeah', 'Doral', 'Temple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill', 'Winterfell', 'Oldtown']
states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

class Name:
    def __init__(self, num=1):
        self.num = num 

    def first_name(self):
        for i in range(self.num):
            print(random.choice(fname))

    def last_name(self):
        for i in range(self.num):
            print(random.choice(lname))

    def full_name(self):
        for i in range(self.num):
            first = random.choice(fname)
            # The image output combines a first name with a *last* name/surname/place name
            # So I'll combine fname and lname lists here for simplicity.
            surname = random.choice(lname) 
            print(f"{first} {surname}")

    def full_profile(self):
        for i in range(self.num):
            first = random.choice(fname)
            last = random.choice(lname)
            
            # --- Address Components ---
            street_num = random.randint(100, 999)
            street = random.choice(street_name)
            city = random.choice(city_name)
            state = random.choice(states)
            zip_code = random.randint(10000, 99999)
            
            # Formatted address string to match the output style
            address = f"{street_num} {street} St., {city} {state} {zip_code}- Us"
            
            # --- Phone Number ---
            # Adjusted generation to match the 11-digit structure starting with +91-
            phone_suffix = random.randint(1000000000, 9999999999) 
            phone = f"+91-{phone_suffix}"
            
            # --- Email ---
            email = f'{first.lower()}{last.lower()}@bogusemail.com'
            
            # --- Print Output to Match Image Style ---
            print(f"\n{first} {last}")
            print(address)
            print(phone)
            print(email)
            print("---------------------------------------") # Using a consistent separator

# --- Execution Block ---
# Get user input and handle potential errors
try:
    num_input = input("Number of Profiles you want to create :")
    num = int(num_input)
except ValueError:
    print("Invalid input. Defaulting to 1 profile.")
    num = 1

ob = Name(num)

print("\nRandom First Names :")
ob.first_name()

print("\nRandom Last Names :")
ob.last_name()

print("\nRandom Full Names :")
ob.full_name()

print("\nRandom Profiles :")
ob.full_profile()

print("\n***********************************")