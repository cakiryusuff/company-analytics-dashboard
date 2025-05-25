from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from datetime import datetime
import os

from plots import *
from data_access import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{os.getenv("DB_PASSWORD")}@localhost:5432/SupermarketSales'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def dashboard():
    current_minute = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    product_line_data = get_product_line_data(db)
    quantity_sales_data = get_quantity_sales_data(db)
    payment_data = get_payment_data(db)
    sales_data = get_sales_data(db)
    table_data = get_table_data(db)
    
    summary_cards = [
        create_summary_card("Genel Toplam", f"{general_total(db)} TL"),
        create_summary_card("Toplam Adet Satış", f"{general_product_sale(db)} Adet"),
        create_summary_card("Toplam Vergi", f"{general_tax(db)} TL"),
        create_summary_card("Toplam Adet", "672K")
    ]
    charts = [
        pie_chart(),
        bar_chart(product_line_data),
        treemap_chart(payment_data),
        line_chart(quantity_sales_data),
        sales_table(sales_data),
        
    ]
    candlestick_chart_graph = candlestick_chart()
    
    table = dataset_view(table_data)
    return render_template("index.html", summary_cards=summary_cards, charts=charts, table=table, current_minute=current_minute, candlestick_chart_graph=candlestick_chart_graph)

if __name__ == "__main__":
    app.run(debug=True)
