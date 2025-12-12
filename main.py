from pyscript import display
# Python Data Types

# String data type
school_name = "BSCD - Bicol School for Children with Disabilities"
owner_name = "Rye Deinla"

# Integer data type
year_since = 2025

# Tuple data type
business_hours = ("7:00 AM", "4:00 PM")

# Displaying school information
display(school_name, target="name1")
display(f"Founder: {owner_name}", target="owner")
display(f"Teaching Since {year_since}", target="since")

# Display additional information
display(f"Business Hours: {business_hours[0]} - {business_hours[1]}", target="openingHours")

