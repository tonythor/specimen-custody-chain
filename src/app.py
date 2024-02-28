import streamlit as st

# Title of the web page
st.title('Customer Support Form')

# Select box for problem type
problem_type = st.selectbox(
    'Select your problem type',
    ('Tech Support', 'Email', 'Phones', 'Other')
)

# Input box for problem description
problem_description = st.text_area("Describe your problem")

# Submit button
if st.button('Submit'):
    # You can process the form data here
    st.success(f"Your problem of type '{problem_type}' has been submitted successfully!")
    st.write(f"Problem Description: {problem_description}")


## from the virtualenv activated directory, run..
# streamlit run ./src/app.py 

