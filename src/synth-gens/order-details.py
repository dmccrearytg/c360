import pandas as pd
import random
# Create synthetic OrderDetails data
order_details_data = {
    'orderDetailsID': list(range(1, 301)),  # Generate 300 order details IDs
    'orderID': [random.randint(1, 100) for _ in range(300)],  # Random order ID between 1 and 100
    'quantity': [random.randint(1, 10) for _ in range(300)],  # Random quantity between 1 and 10
    'productID': [random.randint(101, 110) for _ in range(300)]  # Random product ID between 101 and 110
}

# Create a DataFrame to represent the order details
df_order_details = pd.DataFrame(order_details_data)

# Save the order details data to a CSV file
order_details_file_path = "synthetic_order_details.csv"
df_order_details.to_csv(order_details_file_path, index=False)

# Return the path to the CSV file
order_details_file_path  # Output the path to the CSV file
