noisy_strings = ["python..,,##.%", "?bad##.%,.", "is,,.,#%.", "!not%.,,,,", "powerful##,,..,,"]

# First remove the noise which is after the letters
cleaned_strings = list(map(lambda s : s.strip(",.%#"), noisy_strings))

# Then remove strings that start with "!""
filtered_cleaned_strings = list(filter(lambda s: (s[0] != "!") and (s[0] != "?"), cleaned_strings))

# Printing the clean and filtered strings
print(filtered_cleaned_strings)

# Or on one line:
print(list(filter(lambda s: (s[0] != "!") and (s[0] != "?"), list(map(lambda s : s.strip(",.%#"), noisy_strings)))))