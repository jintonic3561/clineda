from lib.tools import load_data

df = load_data()
# Don't edit anything above this line!
#################

#############
# Your code here
stats = df.describe()
#############

# Finally, always call the print_json function on the analyzed data.
print(stats.to_json())
