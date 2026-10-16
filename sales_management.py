import mysql.connector
from datetime import date

# ---------- DATABASE CONNECTION ----------
def connect_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="sales_management"
    )
# ---------- ADD PRODUCT ----------
def add_product():
    conn = connect_database()
    cursor = conn.cursor()
    try:
        name = input("Enter product name: ").strip()
        category = input("Enter category: ").strip()
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))

        if price < 0 or stock < 0:
            print("Price and stock cannot be negative.")
            return

        query = """
            INSERT INTO products (product_name, category, price, stock)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (name, category, price, stock))
        conn.commit()
        print("\nProduct added successfully!")

    except ValueError:
        print("\nPlease enter valid numbers for price and stock.")
    finally:
        cursor.close()
        conn.close()
        # ---------- VIEW PRODUCTS ----------
def view_products():
    conn = connect_database()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM products ORDER BY product_id")
        products = cursor.fetchall()

        print("\n========== PRODUCTS ==========")
        print("ID | Product | Category | Price | Stock")
        print("------------------------------------------")
        for product in products:
            print(
                product[0], "|",
                product[1], "|",
                product[2], "|",
                f"{product[3]:.2f}", "|",
                product[4]
            )
    finally:
        cursor.close()
        conn.close()
# ---------- MAKE SALE ----------
def make_sale():
    conn = connect_database()
    cursor = conn.cursor()
    try:
        product_id = int(input("Enter product ID: "))

        cursor.execute(
            "SELECT product_name, price, stock FROM products WHERE product_id = %s",
            (product_id,)
        )
        product = cursor.fetchone()

        if product is None:
            print("\nProduct not found!")
            return

        product_name, price, stock = product
        print("\nProduct:", product_name)
        print("Price: ₹", price)
        print("Available stock:", stock)

        customer = input("Enter customer name: ").strip()
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("\nQuantity must be greater than zero.")
            return
        if quantity > stock:
            print("\nNot enough stock available!")
            return

        total = price * quantity
        sale_query = """
            INSERT INTO sales
                (product_id, customer_name, quantity, total_amount, sale_date)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(
            sale_query,
            (product_id, customer, quantity, total, date.today())
        )

        update_query = """
            UPDATE products
            SET stock = stock - %s
            WHERE product_id = %s
        """
        cursor.execute(update_query, (quantity, product_id))
        conn.commit()

        print("\n========== SALE SUCCESSFUL ==========")
        print("Product:", product_name)
        print("Customer:", customer)
        print("Quantity:", quantity)
        print(f"Total Amount: ₹{total:.2f}")
        print("Date:", date.today())

    except ValueError:
        conn.rollback()
        print("\nPlease enter valid numbers.")
    except mysql.connector.Error as error:
        conn.rollback()
        print("Database error:", error)
    finally:
        cursor.close()
        conn.close()
        # ---------- VIEW SALES ----------
def view_sales():
    conn = connect_database()
    cursor = conn.cursor()
    try:
        query = """
            SELECT sales.sale_id, products.product_name,
                   sales.customer_name, sales.quantity,
                   sales.total_amount, sales.sale_date
            FROM sales
            JOIN products ON sales.product_id = products.product_id
            ORDER BY sales.sale_id
        """
        cursor.execute(query)
        sales = cursor.fetchall()

        print("\n========== SALES RECORDS ==========")
        print("ID | Product | Customer | Qty | Amount | Date")
        print("------------------------------------------------")
        for sale in sales:
            print(
                sale[0], "|",
                sale[1], "|",
                sale[2], "|",
                sale[3], "|",
                f"{sale[4]:.2f}", "|",
                sale[5]
            )
    finally:
        cursor.close()
        conn.close()
        # ---------- SEARCH PRODUCT ----------
def search_product():
    conn = connect_database()
    cursor = conn.cursor()
    try:
        name = input("Enter product name to search: ").strip()
        cursor.execute(
            "SELECT * FROM products WHERE product_name LIKE %s ORDER BY product_id",
            (f"%{name}%",)
        )
        products = cursor.fetchall()

        print("\n========== SEARCH RESULTS ==========")
        if not products:
            print("No matching product found.")
        else:
            print("ID | Product | Category | Price | Stock")
            for product in products:
                print(
                    product[0], "|",
                    product[1], "|",
                    product[2], "|",
                    f"{product[3]:.2f}", "|",
                    product[4]
                )
    finally:
        cursor.close()
        conn.close()


# ---------- MAIN MENU ----------
def main():
    while True:
        print("\n========== SALES MANAGEMENT SYSTEM ==========")
        print("1. Add Product")
        print("2. View Products")
        print("3. Make Sale")
        print("4. View Sales")
        print("5. Search Product")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                add_product()
            elif choice == "2":
                view_products()
            elif choice == "3":
                make_sale()
            elif choice == "4":
                view_sales()
            elif choice == "5":
                search_product()
            elif choice == "6":
                print("Thank you for using Sales Management System!")
                break
            else:
                print("Invalid choice. Please select 1–6.")
        except mysql.connector.Error as error:
            print("Could not complete the operation. Check your MySQL connection.")
            print("Details:", error)


if __name__ == "__main__":
    main()

