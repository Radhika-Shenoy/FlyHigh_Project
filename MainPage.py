import streamlit as st 
#st.set_page_config(layout="wide")
def redirect_to_streamline():
    # Run the other Streamlit script for the streamline page
    import subprocess
    subprocess.run(["streamlit", "run", "CMSE_project_passengerSatisfaction.py"])

image1_url = '''
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url('https://images.unsplash.com/photo-1569839333583-7375336cde4b?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTY4Njk2MDQ4Mw&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1080');
    background-size: cover;
    background-repeat: no-repeat;
    }
    </style>
    '''
st.markdown(image1_url, unsafe_allow_html=True)
st.markdown('<h1 style="color:black;font-size:35px;text-align:left;margin-left:20px;">FlyHigh Airlines</h1>', unsafe_allow_html=True)

with st.form(key='login_form'):
    st.subheader('Login Credentials')
    username = st.text_input('**Enter your FlyHigh userID:**')
    password = st.text_input('**Enter your FlyHigh password:**', type='password')
    
    st.markdown('Disclaimer!:')
    st.markdown('Certain sections of the web app contain sensitive FlyHigh brand data and passenger survey information. Kindly refrain from accessing this information if you are not an authorized FlyHigh team member. Unauthorized access will be subject to penalties.')
    #a_click = st.checkbox('Agree')
    checkbox_val = st.checkbox("**I am an employed FlyHigh member**") 
    login_button = st.form_submit_button('Login')
    #if not a_click:
        #st.warning('Please accept agree')
    #if a_click:  
    if login_button:
        if not username or not password:
            st.error("Please enter the credentials to login")
    if login_button:
        if username and password:
            if not (username == 'user' and password == 'password'):
                st.error("Invalid username/ password")
            if (username == 'user' and password == 'password'):
                if not checkbox_val:
                    st.error('Please accept that you are an employeed FlyHigh member')
                if checkbox_val:
                    if login_button:
                        redirect_to_streamline()  
                        st.success("Login successful!")
                                



                
