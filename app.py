import streamlit as st

# --- Logic Classes ---
class Employee:
    per_hour_salary = 1538.50

    @staticmethod
    def calculate_salary(hours):
        if hours < 0:
            return None, "Hours cannot be negative."
        salary = hours * Employee.per_hour_salary
        return salary, None

class Room:
    @staticmethod
    def calculate_area(length, width):
        return length * width

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

# --- Streamlit UI ---
def main():
    st.set_page_config(page_title="Multi-Utility Calculator", page_icon="🧮")
    
    st.title("🧮 Multi-Utility Calculator")
    st.markdown("---")

    # Initialize session state for total payroll to persist between re-runs
    if 'total_payroll' not in st.session_state:
        st.session_state.total_payroll = 0.0

    # Sidebar Navigation
    menu = ["Room Area", "Room Perimeter", "Employee Salary"]
    choice = st.sidebar.selectbox("Select a Utility", menu)

    if choice == "Room Area":
        st.header("📏 Calculate Room Area")
        col1, col2 = st.columns(2)
        with col1:
            length = st.number_input("Enter Room's Length (m)", min_value=0.0, step=0.1)
        with col2:
            width = st.number_input("Enter Room's Width (m)", min_value=0.0, step=0.1)
        
        if st.button("Calculate Area"):
            area = Room.calculate_area(length, width)
            st.success(f"**Result:** The Area of the Room is **{area:,.2f} sq. m.**")

    elif choice == "Room Perimeter":
        st.header("📐 Calculate Room Perimeter")
        col1, col2 = st.columns(2)
        with col1:
            length = st.number_input("Enter Room's Length (m)", min_value=0.0, step=0.1)
        with col2:
            width = st.number_input("Enter Room's Width (m)", min_value=0.0, step=0.1)
            
        if st.button("Calculate Perimeter"):
            perimeter = Room.calculate_perimeter(length, width)
            st.info(f"**Result:** The Perimeter of the Room is **{perimeter:,.2f} m.**")

    elif choice == "Employee Salary":
        st.header("💰 Employee Salary System")
        st.metric("Hourly Rate", f"₹{Employee.per_hour_salary:,.2f}")
        
        hours = st.number_input("Enter total working hours", min_value=0.0, step=0.5)
        
        if st.button("Process Salary"):
            salary, error = Employee.calculate_salary(hours)
            if error:
                st.error(error)
            else:
                st.session_state.total_payroll += salary
                st.write(f"**Calculated Salary:** ₹{salary:,.2f}")
                st.balloons()

        st.markdown("---")
        st.subheader("Company Stats")
        st.metric("Total Payroll Managed", f"₹{st.session_state.total_payroll:,.2f}")

if __name__ == "__main__":
    main()
