import streamlit as st

st.set_page_config(page_title="Pye-to-eBay Calculator", layout="centered")

st.title("📊 Pye-to-eBay Profit Calc")
st.write("Calculate your 'All-In' costs and eBay margins instantly.")

# --- SIDEBAR / INPUTS ---
st.header("1. Sourcing Costs (John Pye)")
hammer_price = st.number_input("John Pye Hammer Price (£)", min_value=0.0, value=50.0)
buyers_premium = st.slider("Buyer's Premium %", 0, 30, 20)
vat_rate = st.slider("VAT Rate %", 0, 20, 20)

st.header("2. Selling Price & Fees")
target_sale = st.number_input("Target eBay Sale Price (£)", min_value=0.0, value=120.0)
ebay_fee_pct = st.number_input("eBay Fee % (Standard is 12.8%)", value=12.8) / 100
shipping = st.number_input("Shipping Cost to Buyer (£)", value=5.0)
packaging = st.number_input("Packaging & Labels (£)", value=1.5)
other_exp = st.number_input("Other Expenses (Fuel/Dud rate) (£)", value=0.0)

# --- CALCULATIONS ---
# John Pye Math
premium_amount = hammer_price * (buyers_premium / 100)
subtotal = hammer_price + premium_amount
total_vat = subtotal * (vat_rate / 100)
total_pye_cost = subtotal + total_vat

# eBay Math
total_ebay_fees = (target_sale * ebay_fee_pct) + 0.30
total_outgoings = total_pye_cost + total_ebay_fees + shipping + packaging + other_exp
net_profit = target_sale - total_outgoings
roi = (net_profit / total_pye_cost) * 100 if total_pye_cost > 0 else 0

# --- RESULTS DISPLAY ---
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Pye Cost", f"£{total_pye_cost:.2f}")
    st.write(f"*(Incl. £{total_vat:.2f} VAT)*")

with col2:
    color = "normal" if net_profit > 0 else "inverse"
    st.metric("Net Profit", f"£{net_profit:.2f}", delta_color=color)

st.subheader(f"Return on Investment: {roi:.1f}%")

if roi < 20:
    st.warning("⚠️ Low Margin: Be careful with this bid!")
elif roi > 50:
    st.success("🔥 High Margin: Great find!")