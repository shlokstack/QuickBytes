import streamlit as st
import json
from fpdf import FPDF
import datetime
st.set_page_config(
    page_title="QuickBytes",
    page_icon="🍴",
    layout="wide"    
)
st.title("Restaurant Ordering System")
st.caption("Order your favorite food online")
# Load Menu made by restaurant using JSON
with open("menu.json", "r") as f:
    menu_data = json.load(f)
    
name = st.text_input("Write user name ", placeholder="Name, Surname" )

dob = st.date_input("Enter you Date of Birth",value=datetime.date(2006,1,31) ,max_value=datetime.date.today())
city = st.selectbox("Enter your city", options=["Vadodara", "Vapi", "Ahmedabad", "Rajkot", "Surat", "Gandhinagar"],accept_new_options=True)
gender = st.radio("Select your gender ", options=["Male", "Female","None of the above", "Prefer not to say"])
food_type = st.radio("Food type", options=["Veg", "Non-veg"])
st.subheader("Menu Card")
# Menu Card
for item, price in menu_data.items():
    st.write(f"🍽️ {item} - ₹{price}")
food_menu = st.multiselect("Food menu", options=list(menu_data.keys()))
budget = st.slider("Enter your budget range in INR", min_value=100, max_value=1200,value=500)
comments =st.text_area("Add comments", placeholder="Write your comment here")

if st.button("Submit"):
    if not name:
        st.error("Please enter your name")
        st.stop()
    if not food_menu:
        st.error("Please select the food menu")
        st.stop()
    
    total_cost = sum(menu_data[item] for item in food_menu)
    if (total_cost>budget):
        st.warning(f"The total cost is ₹{total_cost} which is more than the budget of ₹{budget}")
        st.stop()
    
    st.subheader("Order Summary")
    st.write(f"Name: {name}")
    st.write(f"City: {city}")
    st.write(f"Gender: {gender}")
    st.write(f"Food type: {food_type}")
    st.write(f"Items:",", ".join(food_menu))
    st.write("Selected Items:", food_menu)
    st.write("Total amount: ₹", total_cost)
    st.success("Order Submitted!")
    # Let the user download the bill
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Restaurant Bill", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Customer: {name}", ln=True)
    pdf.cell(200, 10, txt=f"City: {city}", ln=True)
    pdf.cell(200, 10, txt=f"Food Ordered: {', '.join(food_menu)}", ln=True)
    pdf.cell(200, 10, txt=f"Total Cost: Rs. {total_cost}", ln=True)

    pdf_file = "bill.pdf"
    pdf.output(pdf_file)

    with open(pdf_file, "rb") as file:
        st.download_button(
            "📄 Download PDF Bill",
            file,
            file_name="bill.pdf",
            mime="application/pdf"
        )
    # Store orders in CSV file for restaurant
    selected_food = "|".join(food_menu)
    with open("orders.csv", "a") as f:
        f.write(f"{name},{city},{food_type},{selected_food},{total_cost}\n")
    st.snow()