import streamlit as st

# Sidebar Navigation
def sidebar():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About", "Contact", "Register"])
    return page

# Home Page
def home_page():
    # About Me Title
    st.title("Home Page")

    # Introduction Text
    st.info(
        "Hello, I'm Areeba Saleem, a passionate web developer with expertise in HTML, CSS, JavaScript, and Python. My journey into web development has been driven by a love for creating innovative and user-friendly digital solutions. I specialize in building dynamic and responsive web applications, and I've had the opportunity to work on several exciting projects"
    )

    # Skills Section
    st.header("Skills")

    skills = [
        {"name": "HTML","level":100 },
        {"name": "Tailwind CSS", "level": 90},
        {"name": "Next.js", "level": 90},
        {"name": "Python", "level": 70},
    ]

    for skill in skills:
        st.write(f"**{skill['name']}**")
        st.progress(skill['level'])  # Progress bar
        # st.text(f"{skill['level']}%")

    # Projects Section
    st.header("Projects That I Made:")

    projects = [
        {"name": "Unit Converter", "description": "Converts units from one type to another."},
        {"name": "Password Generator", "description": "Generates strong passwords."},
        {"name": "Madlibs", "description": "A fun word game where you fill in the blanks."},
        {"name": "Hangman", "description": "Classic hangman word game."},
        {"name": "Countdown Timer", "description": "A countdown timer for various tasks."},
        {"name": "Number Guessing Game", "description": "Guess the correct number in limited attempts."},
        {"name": "BMI Calculator", "description": "Calculates Body Mass Index based on height and weight."},
    ]

    for project in projects:
        st.subheader(project["name"])
        st.write(project["description"])


# About Page
# Function to display both Skills and Projects under one 'about_page' function

    # About Me Title
    st.title("About Me")

    # Introduction Text
    st.write(
        "Welcome to my portfolio. Below are my skills and projects I have worked on."
    )

    # Skills Section
    st.header("Skills")

    skills = [
        {"name": "HTML","level":100 },
        {"name": "Tailwind CSS", "level": 90},
        {"name": "Next.js", "level": 90},
        {"name": "Python", "level": 70},
    ]

    for skill in skills:
        st.write(f"**{skill['name']}**")
        st.progress(skill['level'])  # Progress bar
        # st.text(f"{skill['level']}%")

    # Projects Section
    st.header("Projects That I Made:")

    projects = [
        {"name": "Unit Converter", "description": "Converts units from one type to another."},
        {"name": "Password Generator", "description": "Generates strong passwords."},
        {"name": "Madlibs", "description": "A fun word game where you fill in the blanks."},
        {"name": "Hangman", "description": "Classic hangman word game."},
        {"name": "Countdown Timer", "description": "A countdown timer for various tasks."},
        {"name": "Number Guessing Game", "description": "Guess the correct number in limited attempts."},
        {"name": "BMI Calculator", "description": "Calculates Body Mass Index based on height and weight."},
    ]

    for project in projects:
        st.subheader(project["name"])
        st.write(project["description"])

#about page
# Function to display the About Page
def about_page():
    # About Me Title
    st.title("About Me")

    # About Me Section
    st.subheader("Hello, I am Areeba Saleem")
    st.write(
        "I am a dedicated web development student at GIAIC, passionate about crafting innovative digital solutions. "
        "With expertise in HTML, CSS, JavaScript, and cutting-edge frameworks, I strive to create effective web applications."
    )

    st.write(
        "My aim is to become a proficient full-stack web developer, build innovative and user-friendly web applications, "
        "and collaborate with other developers on exciting projects."
    )

     # Education Section (Optional)
    st.header("Education")
    st.write(
        "**Bachelors In Commerce**")
    st.write("**Student Of GIAIC**")
    st.write("**Focusing on web development, problem-solving, and modern technologies**")
    

    # Contact Info Section
    st.header("Contact Info")
    st.write("**Email**: [areebasaleem773@gmail.com](mailto:areebasaleem773@gmail.com)")
    st.write("**Phone**: 0315-2167838")
    st.write("**LinkedIn**: [Linkedin Profile](http://linkedin.com/in/areeba-saleem-67025a2ba)")
    st.write("**GitHub**: [GitHub Profile](https://github.com/areebasaleem456)")

# Contact Page
# Function to display the contact page
def contact_page():
    st.title("Contact Us")

    # Display the map using iframe in an HTML tag
    map_html = """
    <iframe
        width="100%"
        height="200"
        frameBorder="0"
        title="map"
        marginHeight="0"
        marginWidth="0"
        scrolling="no"
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d7240.4750186084175!2d67.01257163073164!3d24.855736461728746!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3eb33e0c3136a60f%3A0x43c145a0d87b66ca!2sBurns%20Road%2C%20Karachi%2C%20Karachi%20City%2C%20Sindh%2C%20Pakistan!5e0!3m2!1sen!2s!4v1731360636420!5m2!1sen!2s"
        style="border:0; filter: contrast(1.2) opacity(0.4);"
    ></iframe>
    """
    st.markdown(map_html, unsafe_allow_html=True)

    # Contact Info Details
    st.write("**ADDRESS**: Sunny Side Building line no.3 burns road Karachi.")
    st.write("**EMAIL**: [areebasaleem773@gmail.com](mailto:areebasaleem773@gmail.com)")
    st.write("**PHONE**: 0315-2167838")

    # Contact Form Section
    st.subheader("Send Us a Message")

    # Contact Form Inputs
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message", height=90)

        # Submit Button
        submit_button = st.form_submit_button("Send")

        if submit_button:
            if name and email and message:
                st.success(f"Thank you {name}! Your message has been sent successfully.")
                st.write(f"Message: {message}")
            else:
                st.error("Please fill out all the fields.")


# Registration Form  
def register_user():
    st.title("Register User")

    # Registration Form Inputs
    with st.form("registration_form"):
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        # Submit Button
        submit_button = st.form_submit_button("Register")

        if submit_button:
            if password == confirm_password:
                st.success(f"User {username} registered successfully!")
            else:
                st.error("Passwords do not match.")

# Main function to control navigation and display pages
def main():
    # Get selected page from the sidebar
    page = sidebar()

    if page == "Home":
        home_page()
    elif page == "About":
        about_page()
    elif page == "Contact":
        contact_page()
    elif page == "Register":
        register_user()

if __name__ == "__main__":
    main()

