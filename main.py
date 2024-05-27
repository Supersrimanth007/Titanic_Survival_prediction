import streamlit as st
import pickle
import base64

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def predict_survival(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    Sex_dict = {'Male': 0, 'Female': 1}
    SibSp_dict = {'No': 0, 'Yes': 1}
    
    Features = [Pclass, Sex_dict[Sex], Age, SibSp_dict[SibSp], Parch, Fare]
    
    if Embarked == "Cherbourg (C)":
        Features += [0, 0]
    elif Embarked == "Queenstown (Q)":
        Features += [1, 0]
    else:  # Southampton (S)
        Features += [0, 1]
    
    Model = pickle.load(open('TitanicModel.pkl', 'rb'))
    
    return Model.predict([Features])[0]

st.sidebar.title("Titanic 🚢 Survival Prediction")

Pclass = st.sidebar.selectbox("Passenger Class (Pclass)", (1, 2, 3))
Sex = st.sidebar.selectbox("Sex", ("Male", "Female"))
Age = st.sidebar.number_input("Age", min_value=0, max_value=100, value=25)
SibSp = st.sidebar.selectbox("Siblings or Spouses Aboard (SibSp)", ("No", "Yes"))
Parch = st.sidebar.number_input("Parents or Children Aboard (Parch)", min_value=0, max_value=10, value=0)
Fare = st.sidebar.number_input("Ticket Fare", min_value=0.0, max_value=500.0, value=32.2)
Embarked = st.sidebar.selectbox("Port of Embarkation (Embarked)", ("Cherbourg (C)", "Queenstown (Q)", "Southampton (S)"))

button = st.sidebar.button("Predict Survival")

if button:
    if not all([Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]):
        st.error("Please fill in all the required fields.")
    else:
        prediction = predict_survival(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)
        result = "Survived" if prediction == 1 else "Did Not Survive"
        st.markdown(f"<h2 style='text-align: center;'>Prediction: {result}</h2>", unsafe_allow_html=True)
else:
    st.markdown("<h2 style='text-align: center;'>Enter all the values to get your survival prediction</h2>", unsafe_allow_html=True)
import streamlit as st
import pickle
import base64

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def predict_survival(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    Sex_dict = {'Male': 0, 'Female': 1}
    SibSp_dict = {'No': 0, 'Yes': 1}
    
    Features = [Pclass, Sex_dict[Sex], Age, SibSp_dict[SibSp], Parch, Fare]
    
    if Embarked == "Cherbourg (C)":
        Features += [0, 0]
    elif Embarked == "Queenstown (Q)":
        Features += [1, 0]
    else:  # Southampton (S)
        Features += [0, 1]
    
    Model = pickle.load(open('TitanicModel.pkl', 'rb'))
    
    return Model.predict([Features])[0]

st.sidebar.title("Titanic 🚢 Survival Prediction")

Pclass = st.sidebar.selectbox("Passenger Class (Pclass)", (1, 2, 3))
Sex = st.sidebar.selectbox("Sex", ("Male", "Female"))
Age = st.sidebar.number_input("Age", min_value=0, max_value=100, value=25)
SibSp = st.sidebar.selectbox("Siblings or Spouses Aboard (SibSp)", ("No", "Yes"))
Parch = st.sidebar.number_input("Parents or Children Aboard (Parch)", min_value=0, max_value=10, value=0)
Fare = st.sidebar.number_input("Ticket Fare", min_value=0.0, max_value=500.0, value=32.2)
Embarked = st.sidebar.selectbox("Port of Embarkation (Embarked)", ("Cherbourg (C)", "Queenstown (Q)", "Southampton (S)"))

button = st.sidebar.button("Predict Survival")

if button:
    if not all([Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]):
        st.error("Please fill in all the required fields.")
    else:
        prediction = predict_survival(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)
        result = "Survived" if prediction == 1 else "Did Not Survive"
        st.markdown(f"<h2 style='text-align: center;'>Prediction: {result}</h2>", unsafe_allow_html=True)
else:
    st.markdown("<h2 style='text-align: center;'>Enter all the values to get your survival prediction</h2>", unsafe_allow_html=True)
import streamlit as st
import pickle
import base64

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def predict_survival(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    Sex_dict = {'Male': 0, 'Female': 1}
    SibSp_dict = {'No': 0, 'Yes': 1}
    
    Features = [Pclass, Sex_dict[Sex], Age, SibSp_dict[SibSp], Parch, Fare]
    
    if Embarked == "Cherbourg (C)":
        Features += [0, 0]
    elif Embarked == "Queenstown (Q)":
        Features += [1, 0]
    else:  # Southampton (S)
        Features += [0, 1]
    
    Model = pickle.load(open('TitanicModel.pkl', 'rb'))
    
    return Model.predict([Features])[0]

st.sidebar.title("Titanic 🚢 Survival Prediction")

Pclass = st.sidebar.selectbox("Passenger Class (Pclass)", (1, 2, 3))
Sex = st.sidebar.selectbox("Sex", ("Male", "Female"))
Age = st.sidebar.number_input("Age", min_value=0, max_value=100, value=25)
SibSp = st.sidebar.selectbox("Siblings or Spouses Aboard (SibSp)", ("No", "Yes"))
Parch = st.sidebar.number_input("Parents or Children Aboard (Parch)", min_value=0, max_value=10, value=0)
Fare = st.sidebar.number_input("Ticket Fare", min_value=0.0, max_value=500.0, value=32.2)
Embarked = st.sidebar.selectbox("Port of Embarkation (Embarked)", ("Cherbourg (C)", "Queenstown (Q)", "Southampton (S)"))

button = st.sidebar.button("Predict Survival")

if button:
    if not all([Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]):
        st.error("Please fill in all the required fields.")
    else:
        prediction = predict_survival(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)
        result = "Survived" if prediction == 1 else "Did Not Survive"
        st.markdown(f"<h2 style='text-align: center;'>Prediction: {result}</h2>", unsafe_allow_html=True)
else:
    st.markdown("<h2 style='text-align: center;'>Enter all the values to get your survival prediction</h2>", unsafe_allow_html=True)
