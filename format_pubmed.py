import pandas as pd

# Define input file name
input_file = "pubmed_data.txt"
output_file = "formatted_pubmed_data.csv"

# Read input file
try:
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        print(f"File read successfully! Total lines: {len(lines)}")  # Debug print
except FileNotFoundError:
    print(f"Error: {input_file} not found!")
    exit()

# Check if file is empty
if len(lines) <= 1:
    print("Error: No data found in the file!")
    exit()

# Process input
data = []
for i, line in enumerate(lines[1:], start=2):  # Skip header row
    parts = line.strip().split(",")
    if len(parts) >= 5:  # Ensure valid structure
        title, authors, journal, year, doi = parts[0], parts[1], parts[2], parts[3], parts[4]
        data.append([title, authors, journal, year, doi])
    else:
        print(f"Skipping malformed line {i}: {line}")  # Debug print

# Check if data was extracted
if not data:
    print("Error: No valid data extracted!")
    exit()

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Title", "Authors", "Journal", "Year", "DOI"])

# Save as CSV
df.to_csv(output_file, index=False)
print(f"Formatted data saved in {output_file}!")

# Print neatly formatted table
print(df.to_markdown(index=False))

