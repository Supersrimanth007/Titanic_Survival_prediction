import streamlit as st
import pickle
import base64

st.sidebar.title("Titanic 🚢 Survival Prediction")

# Pclass
Pclass = st.sidebar.selectbox("Passenger Class (Pclass)", (1, 2, 3))

# Sex
Sex = st.sidebar.selectbox("Sex", ("Male", "Female"))
Sex_dict = {'Male': 0, 'Female': 1}

# Age
Age = st.sidebar.number_input("Age", min_value=0, max_value=100, value=25)

# SibSp
SibSp = st.sidebar.selectbox("Siblings or Spouses Aboard (SibSp)", ("No", "Yes"))
SibSp_dict = {'No': 0, 'Yes': 1}

# Parch
Parch = st.sidebar.number_input("Parents or Children Aboard (Parch)", min_value=0, max_value=10, value=0)

# Fare
Fare = st.sidebar.number_input("Ticket Fare", min_value=0.0, max_value=500.0, value=32.2)

# Embarked
Embarked = st.sidebar.selectbox("Port of Embarkation (Embarked)", ("Cherbourg (C)", "Queenstown (Q)", "Southampton (S)"))

# Load the saved model
predict_button = st.sidebar.button("Predict Survival")
back_button = st.sidebar.button("Make Another Prediction")

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

if predict_button:
    # Create the feature vector
    Features = [
        Pclass,
        Sex_dict[Sex],
        Age,
        SibSp_dict[SibSp],
        Parch,
        Fare,
    ]
    
    if Embarked == "Cherbourg (C)":
        Features += [0, 0]
    elif Embarked == "Queenstown (Q)":
        Features += [1, 0]
    else:  # Southampton (S)
        Features += [0, 1]
    
    # Load model
    Model = pickle.load(open('LogModel.pkl', 'rb'))
    
    # Make prediction
    prediction = Model.predict([Features])[0]
    
    if prediction == 1:
        result = "Survived"
        color = "#4CAF50"
    else:
        result = "Did Not Survive"
        color = "#FF5722"
    
    gif = get_img_as_base64("titanic.gif")
    page_bg_gif = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/gif;base64,{gif}");
    background-size: cover;
    background-position: center;
    margin-top: -100px;
    }}
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    .animated-text {{
        font-size: 3rem;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        animation: colorchange 2s infinite;
        text-align: center;
    }}
    @keyframes colorchange {{
        0% {{ color: #FF5722; }}
        25% {{ color: #4CAF50; }}
        50% {{ color: #FFC107; }}
        75% {{ color: #00BCD4; }}
        100% {{ color: #FF5722; }}
    }}
    </style>
    """
    st.markdown(page_bg_gif, unsafe_allow_html=True)
    st.markdown(f"<h2 class='animated-text'>Prediction: {result}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 class='animated-text'>According to our prediction model, you would have {'survived' if prediction == 1 else 'not survived'} the Titanic disaster.</h2>", unsafe_allow_html=True)
    
    if back_button:
        st.experimental_rerun()
else:
    st.markdown(f"<h2 style='text-align: center; color: white;'>Enter all the values to get your survival prediction</h2>", unsafe_allow_html=True)
    img = get_img_as_base64("titanic.jpg")
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/jpeg;base64,{img}");
    background-size: cover;
    background-position: center;
    }}
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    .animated-text {{
        font-size: 3rem;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        animation: colorchange 2s infinite;
        text-align: center;
    }}
    @keyframes colorchange {{
        0% {{ color: #FF5722; }}
        25% {{ color: #4CAF50; }}
        50% {{ color: #FFC107; }}
        75% {{ color: #00BCD4; }}
        100% {{ color: #FF5722; }}
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown(f"<h2 class='animated-text'>Welcome to the Titanic Survival Prediction App</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 class='animated-text'>Please fill out the details on the left sidebar to see if you would have survived the Titanic disaster.</h2>", unsafe_allow_html=True)
import streamlit as st
import pickle
import base64

st.sidebar.title("Titanic 🚢 Survival Prediction")

# Pclass
Pclass = st.sidebar.selectbox("Passenger Class (Pclass)", (1, 2, 3))

# Sex
Sex = st.sidebar.selectbox("Sex", ("Male", "Female"))
Sex_dict = {'Male': 0, 'Female': 1}

# Age
Age = st.sidebar.number_input("Age", min_value=0, max_value=100, value=25)

# SibSp
SibSp = st.sidebar.selectbox("Siblings or Spouses Aboard (SibSp)", ("No", "Yes"))
SibSp_dict = {'No': 0, 'Yes': 1}

# Parch
Parch = st.sidebar.number_input("Parents or Children Aboard (Parch)", min_value=0, max_value=10, value=0)

# Fare
Fare = st.sidebar.number_input("Ticket Fare", min_value=0.0, max_value=500.0, value=32.2)

# Embarked
Embarked = st.sidebar.selectbox("Port of Embarkation (Embarked)", ("Cherbourg (C)", "Queenstown (Q)", "Southampton (S)"))

# Load the saved model
predict_button = st.sidebar.button("Predict Survival")
back_button = st.sidebar.button("Make Another Prediction")

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

if predict_button:
    # Create the feature vector
    Features = [
        Pclass,
        Sex_dict[Sex],
        Age,
        SibSp_dict[SibSp],
        Parch,
        Fare,
    ]
    
    if Embarked == "Cherbourg (C)":
        Features += [0, 0]
    elif Embarked == "Queenstown (Q)":
        Features += [1, 0]
    else:  # Southampton (S)
        Features += [0, 1]
    
    # Load model
    Model = pickle.load(open('TitanicModel.pkl', 'rb'))
    
    # Make prediction
    prediction = Model.predict([Features])[0]
    
    if prediction == 1:
        result = "Survived"
        color = "#4CAF50"
    else:
        result = "Did Not Survive"
        color = "#FF5722"
    
    gif = get_img_as_base64("/mnt/data/titanic.gif")
    page_bg_gif = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/gif;base64,{gif}");
    background-size: cover;
    background-position: center;
    margin-top: -100px;
    }}
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    .animated-text {{
        font-size: 3rem;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        animation: colorchange 2s infinite;
        text-align: center;
    }}
    @keyframes colorchange {{
        0% {{ color: #FF5722; }}
        25% {{ color: #4CAF50; }}
        50% {{ color: #FFC107; }}
        75% {{ color: #00BCD4; }}
        100% {{ color: #FF5722; }}
    }}
    </style>
    """
    st.markdown(page_bg_gif, unsafe_allow_html=True)
    st.markdown(f"<h2 class='animated-text'>Prediction: {result}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 class='animated-text'>According to our prediction model, you would have {'survived' if prediction == 1 else 'not survived'} the Titanic disaster.</h2>", unsafe_allow_html=True)
    
    if back_button:
        st.experimental_rerun()
else:
    st.markdown(f"<h2 style='text-align: center; color: white;'>Enter all the values to get your survival prediction</h2>", unsafe_allow_html=True)
    img = get_img_as_base64("/mnt/data/titanic.jpg")
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/jpeg;base64,{img}");
    background-size: cover;
    background-position: center;
    }}
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    .animated-text {{
        font-size: 3rem;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        animation: colorchange 2s infinite;
        text-align: center;
    }}
    @keyframes colorchange {{
        0% {{ color: #FF5722; }}
        25% {{ color: #4CAF50; }}
        50% {{ color: #FFC107; }}
        75% {{ color: #00BCD4; }}
        100% {{ color: #FF5722; }}
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown(f"<h2 class='animated-text'>Welcome to the Titanic Survival Prediction App</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 class='animated-text'>Please fill out the details on the left sidebar to see if you would have survived the Titanic disaster.</h2>", unsafe_allow_html=True)
import streamlit as st
import pickle
import base64

st.sidebar.title("Titanic 🚢 Survival Prediction")

# Pclass
Pclass = st.sidebar.selectbox("Passenger Class (Pclass)", (1, 2, 3))

# Sex
Sex = st.sidebar.selectbox("Sex", ("Male", "Female"))
Sex_dict = {'Male': 0, 'Female': 1}

# Age
Age = st.sidebar.number_input("Age", min_value=0, max_value=100, value=25)

# SibSp
SibSp = st.sidebar.selectbox("Siblings or Spouses Aboard (SibSp)", ("No", "Yes"))
SibSp_dict = {'No': 0, 'Yes': 1}

# Parch
Parch = st.sidebar.number_input("Parents or Children Aboard (Parch)", min_value=0, max_value=10, value=0)

# Fare
Fare = st.sidebar.number_input("Ticket Fare", min_value=0.0, max_value=500.0, value=32.2)

# Embarked
Embarked = st.sidebar.selectbox("Port of Embarkation (Embarked)", ("Cherbourg (C)", "Queenstown (Q)", "Southampton (S)"))

# Load the saved model
predict_button = st.sidebar.button("Predict Survival")
back_button = st.sidebar.button("Make Another Prediction")

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

if predict_button:
    # Create the feature vector
    Features = [
        Pclass,
        Sex_dict[Sex],
        Age,
        SibSp_dict[SibSp],
        Parch,
        Fare,
    ]
    
    if Embarked == "Cherbourg (C)":
        Features += [0, 0]
    elif Embarked == "Queenstown (Q)":
        Features += [1, 0]
    else:  # Southampton (S)
        Features += [0, 1]
    
    # Load model
    Model = pickle.load(open('TitanicModel.pkl', 'rb'))
    
    # Make prediction
    prediction = Model.predict([Features])[0]
    
    if prediction == 1:
        result = "Survived"
        color = "#4CAF50"
    else:
        result = "Did Not Survive"
        color = "#FF5722"
    
    gif = get_img_as_base64("/mnt/data/titanic.gif")
    page_bg_gif = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/gif;base64,{gif}");
    background-size: cover;
    background-position: center;
    margin-top: -100px;
    }}
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    .animated-text {{
        font-size: 3rem;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        animation: colorchange 2s infinite;
        text-align: center;
    }}
    @keyframes colorchange {{
        0% {{ color: #FF5722; }}
        25% {{ color: #4CAF50; }}
        50% {{ color: #FFC107; }}
        75% {{ color: #00BCD4; }}
        100% {{ color: #FF5722; }}
    }}
    </style>
    """
    st.markdown(page_bg_gif, unsafe_allow_html=True)
    st.markdown(f"<h2 class='animated-text'>Prediction: {result}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 class='animated-text'>According to our prediction model, you would have {'survived' if prediction == 1 else 'not survived'} the Titanic disaster.</h2>", unsafe_allow_html=True)
    
    if back_button:
        st.experimental_rerun()
else:
    st.markdown(f"<h2 style='text-align: center; color: white;'>Enter all the values to get your survival prediction</h2>", unsafe_allow_html=True)
    img = get_img_as_base64("/mnt/data/titanic.jpg")
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/jpeg;base64,{img}");
    background-size: cover;
    background-position: center;
    }}
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    .animated-text {{
        font-size: 3rem;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        animation: colorchange 2s infinite;
        text-align: center;
    }}
    @keyframes colorchange {{
        0% {{ color: #FF5722; }}
        25% {{ color: #4CAF50; }}
        50% {{ color: #FFC107; }}
        75% {{ color: #00BCD4; }}
        100% {{ color: #FF5722; }}
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown(f"<h2 class='animated-text'>Welcome to the Titanic Survival Prediction App</h2>", unsafe_allow_html=True)
    
