import pandas as pd
import sqlite3

# Connect to the Chinook database
conn = sqlite3.connect("chinook.db")

# Load all relevant tables into pandas DataFrames
customers = pd.read_sql_query("SELECT * FROM customers", conn)
invoices = pd.read_sql_query("SELECT * FROM invoices", conn)
invoice_items = pd.read_sql_query("SELECT * FROM invoice_items", conn)
tracks = pd.read_sql_query("SELECT * FROM tracks", conn)
albums = pd.read_sql_query("SELECT * FROM albums", conn)

# ======================================================
# 1️⃣ CUSTOMER PURCHASES ANALYSIS
# ======================================================

# Calculate total amount spent by each customer (sum of all invoices)
customer_spending = invoices.groupby("CustomerId")["Total"].sum().reset_index()

# Add customer names
customer_spending = customer_spending.merge(
    customers[["CustomerId", "FirstName", "LastName"]],
    on="CustomerId"
)
customer_spending["CustomerName"] = customer_spending["FirstName"] + " " + customer_spending["LastName"]

# Select and sort columns
customer_spending = customer_spending[["CustomerId", "CustomerName", "Total"]].sort_values(
    by="Total", ascending=False
)

# Top 5 customers by total spending
top5_customers = customer_spending.head(5)

print("=== Top 5 Customers by Total Spending ===")
print(top5_customers)
print("\n")

# ======================================================
# 2️⃣ ALBUM VS. INDIVIDUAL TRACK PURCHASES
# ======================================================

# Merge invoice_items with tracks to get AlbumId for each purchased track
invoice_tracks = invoice_items.merge(tracks[["TrackId", "AlbumId"]], on="TrackId")

# Add customer info by merging with invoices
invoice_tracks = invoice_tracks.merge(invoices[["InvoiceId", "CustomerId"]], on="InvoiceId")

# Count tracks purchased per customer per album
customer_album_purchases = invoice_tracks.groupby(["CustomerId", "AlbumId"])["TrackId"].nunique().reset_index(name="PurchasedTracks")

# Count total tracks available in each album
album_track_counts = tracks.groupby("AlbumId")["TrackId"].nunique().reset_index(name="TotalTracks")

# Merge to compare purchased tracks with total available
comparison = customer_album_purchases.merge(album_track_counts, on="AlbumId")

# Determine if a customer bought the full album
comparison["BoughtFullAlbum"] = comparison["PurchasedTracks"] == comparison["TotalTracks"]

# Determine each customer's general preference
customer_preferences = comparison.groupby("CustomerId")["BoughtFullAlbum"].any().reset_index()
customer_preferences["Preference"] = customer_preferences["BoughtFullAlbum"].apply(
    lambda x: "Full Album" if x else "Individual Tracks"
)

# Calculate percentages of each preference
preference_percentages = customer_preferences["Preference"].value_counts(normalize=True) * 100
preference_summary = preference_percentages.reset_index()
preference_summary.columns = ["Preference", "Percentage"]

print("=== Customer Purchase Preferences ===")
print(preference_summary)

# Close the database connection
conn.close()
