import csv

# CSV data
csv_data = [
    ["ID", "Region Name", "States"],
    ["1", "Northeast", "CT ME MA NH RI VT NJ NY PA"],
    ["2", "Midwest", "IL IN MI OH KS MO NE ND"],
    ["3", "Upper Midwest", "MN ND SD IA WI"],
    ["4", "South Atlantic", "DE FL GA MD NC SC VA DC WV"],
    ["5", "South Central", "AL KY MS TN AR LA OK TX"],
    ["6", "Rocky Mountains", "AZ CO ID MT NM NV UT WY"],
    ["7", "Pacific Coast", "AK CA HI OR WA"],
]

# Output CSV file
output_file = "states.csv"

# Open the output CSV file for writing
with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(["ID", "State"])

    # Write each state with its corresponding ID
    for row in csv_data[1:]:
        region_id = row[0]
        states = row[2].split(" ")  # Split the state codes
        for state in states:
            writer.writerow([region_id, state])  # Write ID and state code
