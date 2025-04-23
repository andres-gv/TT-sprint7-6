import streamlit as st
import plotly.express as px
import yfinance as yf


tab1, tab2 = st.tabs(["Tab 1: Yahoo: información de stocks", "Tab 2: Mercados"])

with tab1:
    st.title("Yahoo info market")

    # Section 2: About
    st.header("Stocks price")    
    url = "https://finance.yahoo.com/markets/"
    st.write("Info de stocks [link](%s)" % url)
    # Divider
    st.markdown("---")
    st.markdown("Info de stocks [link](%s)" % url)


with tab2:
    st.title("Stock Price Tracker")    
    nombre_del_activo = st.text_input("Ingresa el symbol (e.g., NVDA, BTC-USD)", "NVDA")
    
    if nombre_del_activo:
        stock = yf.Ticker(nombre_del_activo)
        df_stocks = stock.history(period="1y")
        
        #st.write("graficando con streamlit.line_chart")
        #st.line_chart(df_stocks['Close'])
        
        st.write("graficando con Plotly")        
        fig = px.line(df_stocks)
        st.plotly_chart(fig)
        
        
        st.write("mostrar la tabla con write()")
        st.write(df_stocks)
        
                
        st.write("mostrar la tabla con dataframe()")        
        st.dataframe(df_stocks.style.highlight_max(axis=0))
        
        