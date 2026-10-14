import pandas as pd # in case of error, install pnadas using: pip install pandas
# Read the CSV file into a DataFrame
# loop it so there is like 900 fake data
df = pd.read_csv('data.csv')

i = 12 # only (number) ex:10 reading will be taken. Increase it to higher according to you plan.
while i>=0:
    #receive data from client
    new_data = {
        'Temp': 120000,
        'Humd': 600000,
        'Label': 0
        }
    df = df._append(new_data, ignore_index=True)
    #print it
    print(new_data)
    i = i - 1


df = df._append(new_data, ignore_index=True)

# Step 3: Save the DataFrame to a new CSV file
df.to_csv("data.csv", index=False)