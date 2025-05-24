from sqlalchemy import text

def get_product_line_data(db):
    return db.session.execute(text("""
        SELECT product_line, COUNT(*) as adet
        FROM sales_data
        GROUP BY product_line
    """)).fetchall()

def get_quantity_sales_data(db):
    return db.session.execute(text("""
        SELECT to_date(date, 'MM/DD/YYYY') AS tarih,
               SUM(quantity) AS toplam_quantity
        FROM sales_data
        GROUP BY tarih
        ORDER BY tarih
    """)).fetchall()

def get_payment_data(db):
    return db.session.execute(text("""
        SELECT payment, COUNT(*) as value
        FROM sales_data
        GROUP BY payment
    """)).fetchall()

def get_sales_data(db):
    return db.session.execute(text("""
        SELECT to_date(date, 'MM/DD/YYYY') AS tarih,
               SUM(tax_5) as vergi,
               SUM(cogs) as maliyet,
               SUM(sales) as satış
        FROM sales_data 
        GROUP BY tarih 
        ORDER BY tarih
    """)).fetchall()

def get_table_data(db):
    return db.session.execute(text("""
        SELECT * FROM sales_data LIMIT 20
    """))
    
def general_total(db):
    return round(db.session.execute(text("""
        SELECT SUM(sales) FROM sales_data
    """)).fetchall()[0][0], 2)

def general_product_sale(db):
    return db.session.execute(text(f"""
        SELECT SUM(quantity) FROM sales_data
    """)).fetchall()[0][0]
    
def general_tax(db):
    return round(db.session.execute(text("""
        SELECT SUM(tax_5) FROM sales_data
    """)).fetchall()[0][0], 2)