# Amazon-Sales-Analysis-Dashboard
This Power BI dashboard provides an in-depth analysis of Amazon sales data, focusing on various aspects such as product quantities, courier status, shipping locations, and product performance metrics.

## Key Insights
Product Quantities: The dashboard displays the sum of quantities sold for different product sizes, revealing that size "M" has the highest sales volume (5,900 units), followed by "L" (5,800 units) and "XL" (5,500 units).

Courier Status: The majority of orders (84.93%) have been shipped, while 13.68% are on the way, and only 1.4% remain unshipped.

Shipping Locations: The dashboard provides a map view of the shipping states in India, allowing users to visualize the distribution of orders across various regions.

Cancellation Rate: The overall cancellation rate for orders is 13.68%.

Product Performance: The dashboard highlights the top-selling product as "T-shirt" with 12,147 units sold (37.33% of total sales), and the lowest-selling product as "Shoes" with only 25 units sold (0.08% of total sales).

Total Income: The dashboard displays the total income generated from sales, which could be a useful metric for tracking revenue.

## Data Insights
Top-Selling Products: "T-shirt" is the top-selling product, accounting for 37.33% of total sales.

Low-Selling Products: "Shoes" is the lowest-selling product, with only 0.08% of total sales.

Popular Product Sizes: The most popular product sizes based on sales volume are "M," "L," and "XL."

High-Volume Shipping States: Users can identify states with high order volumes based on the map visualization.

Courier Performance Analysis: The dashboard provides insights into courier performance by displaying the percentage of orders in different status categories (shipped, on the way, unshipped).

## Data Cleaning
The dataset used in this dashboard was cleaned and preprocessed using Python. The following steps were performed:

Removing Unnecessary Columns: Irrelevant or redundant columns were identified and removed from the dataset to improve efficiency and reduce noise.

Renaming Columns: Column names were renamed to more descriptive and consistent names to improve readability and understanding.

Changing Data Types: The data types of certain columns were changed to ensure compatibility with Power BI and to enable proper data handling and analysis.

Handling Missing Values: Null or missing values were addressed by either imputing appropriate values or dropping rows/columns based on the data quality and requirements.

Data Validation: The cleaned dataset was validated against predefined rules and constraints to ensure data integrity and quality.
