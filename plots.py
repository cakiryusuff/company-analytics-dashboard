import plotly.io as pio
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Simülasyon veri (gerçek veri gelince kolayca değiştirilebilir)
months = ["January", "February"]
sales = [9372825.14, 9372900.02]
total = sum(sales)

import plotly.express as px
import plotly.io as pio

def pie_chart():
    labels = ["İstanbul", "İzmir Bölge", "Ankara", "Bursa"]
    values = ["50", "20", "15", "15"]

    fig = px.pie(
        names=labels,
        values=values,
        color_discrete_sequence=px.colors.sequential.RdBu
        # hole=0.5,  # Donut tipi
    )

    # Etiketleri dışarı taşı ve font ayarla
    fig.update_traces(
        textinfo='label+percent',
        textposition='inside',
    )

    # Genel layout
    fig.update_layout(
        height=300,
        title="Bölge Dağılımı",
        margin=dict(t=30, b=30, l=30, r=30),
        showlegend=True,
        font=dict(family="Impact")
    )

    return pio.to_html(fig, full_html=False, include_plotlyjs=False)


def create_summary_card(title, value):
    return {"title": title, "value": value}

def candlestick_chart():
    # Veriyi oku
    url = 'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'
    df = pd.read_csv(url)
    print(df["Date"])
    # Tarihi datetime formatına çevir
    # df['Date'] = pd.to_datetime(df['Date'])

    # Grafik oluştur
    fig = go.Figure(data=go.Ohlc(x=df['Date'],
                        open=df['AAPL.Open'],
                        high=df['AAPL.High'],
                        low=df['AAPL.Low'],
                        close=df['AAPL.Close']))

    # Grafik ayarları
    fig.update_layout(
        title='Hisse Fiyatı',
        xaxis_title='Tarih',
        yaxis_title='Fiyat (USD)',
        font_family="Impact",
        # xaxis_rangeslider_visible=False,
        margin=dict(t=30, b=30, l=30, r=30)
    )

    # HTML döndür
    return pio.to_html(fig, full_html=False,  include_plotlyjs=True)

def line_chart(datas):
    months = []
    sales = []
    
    for data in datas:
        months.append(data[0])
        sales.append(data[1])
        
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=months, y=sales, mode='lines+markers', name="Genel Toplam", line_color='red'))
    fig.update_layout(height=300, margin=dict(t=30, b=30, l=30, r=30), title="Gün Başına Mal Satış", font_family="Impact")
    return pio.to_html(fig, full_html=False, include_plotlyjs=False)

def bar_chart(datas):
    labels = []
    values = []
    
    for data in datas:
        labels.append(data[0])
        values.append(data[1])
    
    fig = go.Figure(go.Bar(x=labels, y=values, orientation='v', marker_color='red'))
    fig.update_layout(height=300, margin=dict(t=30, b=30, l=30, r=30), title="Ürün Kategorisine Göre Satış", font_family="Impact")
    return pio.to_html(fig, full_html=False, include_plotlyjs=False)

# def pie_chart():
#     labels = ["İstanbul", "İzmir Bölge", "Ankara", "Bursa"]
#     values = [50, 20, 15, 15]
#     fig = go.Figure(px.pie(labels=labels,
#                            values=values,
#                            hole=0.5,
#                         #    marker=dict(line=dict(color='#000000', width=2)),
#                         #    pull=[0, 0.1, 0, 0],
#                            ))
#     fig.update_layout(height=300, margin=dict(t=30, b=30, l=30, r=30), title="Bölge Dağılımı", font_family="Impact")
#     return pio.to_html(fig, full_html=False, include_plotlyjs=False)

def treemap_chart(datas):
    labels = ["Fıstık Ezmesi", "Kakao Bar", "Nohut Cipsi", "Meyve Bar", "Kremler"]
    values = [5000, 3000, 2000, 4000, 1000]
    fig = go.Figure(go.Treemap(
        labels=labels,
        parents=[""] * len(labels),
        values=values,
        marker=dict(
            colors=values,
            colorscale='Reds',
            colorbar=dict(
                title="Değer",
                thickness=15,
                x=1.0
            )
        ),
        root_color="white"
    ))
    fig.update_layout(height=300, margin=dict(t=30, b=30, l=30, r=30), title="Ürün Dağılımı", font_family="Impact")
    return pio.to_html(fig, full_html=False, include_plotlyjs=False)

# def treemap_chart(datas):
#     labels = ["Fıstık Ezmesi", "Kakao Bar", "Nohut Cipsi", "Meyve Bar", "Kremler"]
#     values = ["5000", "3000", "2000", "4000", "1000"]
    
#     data = {
#         "Ürün": labels,
#         "Değer": values,
#         "Üst": [""] * len(labels)  # tüm öğelerin aynı seviyede olması için
#     }

#     fig = px.treemap(
#         data,
#         hover_data=["Ürün"],
#         names="Ürün",
#         parents="Üst",
#         values="Değer",
#         # color_continuous_midpoint=sum(values) / 2,
#         color_discrete_sequence=px.colors.sequential.Reds
#     )
    
#     fig.update_layout(
#         height=300,
#         margin=dict(t=30, b=30, l=30, r=30),
#         title="Ürün Dağılımı",
#         font_family="Impact",
#         coloraxis_colorbar=dict(
#             title="Değer",
#             thickness=15,
#             len=0.5,
#             x=1.0
#         )
#     )
    
#     return pio.to_html(fig, full_html=False, include_plotlyjs=False)



def sales_table(data):
    # df = pd.DataFrame({
    #     "Ürün": ["Fıstık Ezmesi", "Meyve Bar", "Nohut Cipsi", "Kakao Bar"],
    #     "January": [3000, 5000, 1000, 1200],
    #     "February": [3200, 5200, 1100, 1300],
    # })
    # df["Total"] = df["January"] + df["February"]
    
    # print(data)
    
    df = pd.DataFrame(data, columns=['tarih', 'vergi', 'maliyet', 'satış'])

    # Decimal → float dönüşümü
    df['vergi'] = df['vergi'].astype(float)
    df['maliyet'] = df['maliyet'].astype(float)
    df['satış'] = df['satış'].astype(float)

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns), fill_color='paleturquoise', align='left'),
        cells=dict(values=[df[col] for col in df.columns], fill_color='lavender', align='left')
    )])
    fig.update_layout(height=300, width=500, margin=dict(t=30, b=30, l=30, r=30), title="Aylık Ürün Satışları", font_family="Impact")
    return pio.to_html(fig, full_html=False, include_plotlyjs=False)

def dataset_view(datas):
    # print(list(datas.keys()))
    
    df = pd.DataFrame(datas.fetchall(), columns=list(datas.keys()))
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns), fill_color='thistle', align='left'),
        cells=dict(values=[df[col] for col in df.columns], fill_color='snow', align='left')
    )])
    fig.update_layout(margin=dict(t=30, b=30, l=30, r=30), title="Veri Seti", font_family="Impact")
    return pio.to_html(fig, full_html=True, include_plotlyjs=False)