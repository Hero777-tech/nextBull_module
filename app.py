import streamlit as st
import json

st.set_page_config(page_title="NextBull v0", layout="wide")

st.title("NextBull v0 terminal")


@st.cache
def load_symbols():
    with open("indian_stocks_large.json") as f:
        data = json.load(f)
    return data

indian_stocks = load_symbols()
stock_names = [f"{stock['name']} ({stock['symbol']})" for stock in indian_stocks]
symbol_mapping = {f"{stock['name']} ({stock['symbol']})": stock["symbol"] for stock in indian_stocks}

selected_stock = st.selectbox("Select an Indian Stock:", options=stock_names)
symbol = symbol_mapping[selected_stock]

tradingview_widget = f"""
<iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_e2d93&symbol={symbol}&interval=5&hidesidetoolbar=1&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=[]&hideideas=1&theme=light&style=1&timezone=Etc%2FUTC&withdateranges=1&hidevolume=1&hide_legend=1&enabled_features=[]&disabled_features=[]&locale=en" width="100%" height="500px" frameborder="0" allowtransparency="true" scrolling="no"></iframe>
"""

st.markdown(tradingview_widget, unsafe_allow_html=True)
