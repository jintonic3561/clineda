from lib.tools import get_stats, load_data, print_json  # Don't edit this line

df = load_data()
df = get_stats(df)

# Finally, always call the print_json function on the analyzed data.
print_json(df)
