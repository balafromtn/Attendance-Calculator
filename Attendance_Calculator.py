import streamlit as st

def calculate_attendance_percentage(total_hours, present_hours):
    return round((present_hours / total_hours) * 100, 2)

# Streamlit App
st.set_page_config(
    page_title="Student Attendance Calculator",  # Tab heading
    page_icon="📊",  # Emoji as favicon or use an image URL/file
    layout="centered",  # Other options: 'wide'
)

st.title("Student Attendance Calculator")

def line():
    st.markdown(
        "<hr style='border: 2px solid red;'>",  # Adjust thickness and color here
        unsafe_allow_html=True
    )

# Input: Total number of days and students
total_days = st.number_input("Enter the total number of days:", min_value=1, step=1, value=30)
hours_per_day = 5  # Total hours in a day, can be modified if needed
total_hours = total_days * hours_per_day

num_students = st.number_input("Enter the number of students:", min_value=1, step=1, value=36)
st.spinner("working on it...")
# Collect student data
students_data = []

st.write("### Enter details for each student:")
for i in range(1, num_students + 1):
    st.subheader(f"Roll number: {i}")
    present_hours = st.number_input(f"Present hours for Student {i} (out of {total_hours}):", 
                                    min_value=0, max_value=int(total_hours), step=1)
    absent_hours = total_hours - present_hours
    
    # Calculate attendance percentage for each student
    percentage = calculate_attendance_percentage(total_hours, present_hours)
    students_data.append({
        "name": f"Roll number {i}",
        "present_hours": present_hours,
        "absent_hours": absent_hours,
        "percentage": percentage
    })

# Display attendance percentages in the sidebar
st.sidebar.title("Student Present Percentage")

st.sidebar.markdown(
        "<hr style='border: 2px Solid red;'>",  # Adjust thickness and color here
        unsafe_allow_html=True
    )

for student in students_data:
    st.sidebar.write(f"{student['name']}: {student['percentage']}%")

st.sidebar.markdown(
        "<hr style='border: 2px solid red;'>",  # Adjust thickness and color here
        unsafe_allow_html=True
    )

# Calculate and display the class average attendance percentage
total_present_hours = sum(student['present_hours'] for student in students_data)
total_class_hours = total_hours * num_students

line()

class_attendance_percentage = (total_present_hours / total_class_hours) * 100
st.write(f"### Class Average Attendance Percentage: {round(class_attendance_percentage, 2)}%")

line()
st.markdown("________")