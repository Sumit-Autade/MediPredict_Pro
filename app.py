
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          [ 'Home',
                            'Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'
                           ],

                          icons=['house','activity','heart','person'],
                          default_index=0)

if (selected == 'Home'):

    st.title("Your Health Companion")
    st.write("Empowering you with advanced technology for early disease detection.")

    # Features Section
    st.header("Detect:")
    st.subheader("1. Diabetes Detection:")
   
    st.write("- Our state-of-the-art algorithm analyzes key health indicators to assess your risk of diabetes.")
    st.write("- Early detection means proactive management and a healthier life.")
    st.subheader("2. Heart Disease Prediction:")
    st.write("- Get personalized insights into your cardiovascular health.")
    st.write("- Identify potential risks early to make informed lifestyle choices.")
    st.subheader("3. Parkinson's Prediction:")
    st.write("- Cutting-edge assessment tools for early Parkinson's detection.")
    st.write("- Timely interventions can lead to better outcomes.")

    # Additional Features
    st.header("Features You'll Love:")
    st.write("- **User-Friendly Interface:** Simple, intuitive design for easy navigation and quick access to results.")
    st.write("- **Secure Data Protection:** Your health data is encrypted and stored securely, ensuring complete privacy.")


    st.header("Disclaimer:")
    st.write("While our app is designed to provide valuable insights into your health, it's important to remember that the results generated are based on algorithms and statistical models. They are not a replacement for professional medical advice or diagnosis.")
    st.write("Always consult a qualified healthcare professional for accurate and personalized medical guidance. Your doctor is the best source of information regarding your health, and their expertise should always be prioritized.")
    st.write("Use this app as a tool for early awareness and as a complement to regular check-ups. Your health is our priority, and we encourage you to be proactive in seeking professional medical care.")

        
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction')

    st.subheader("Data Information:")
    st.write("- Pregnancies: Number of times pregnant")
    st.write("- Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test")
    st.write("- Blood Pressure: Diastolic blood pressure (mm Hg)")
    st.write("- Skin Thickness: Triceps skin fold thickness (mm)")
    st.write("- Insulin: 2-Hour serum insulin (mu U/ml)")
    st.write("- BMI: Body mass index (weight in kg/(height in m)^2)")
    st.write("- Diabetes Pedigree Function: Diabetes pedigree function")
    st.write("- Age: Age (years)")
    

    st.write('##')
        
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies',min_value=0,max_value=20,step = 1)

    with col2:
        Glucose = st.number_input('Glucose Level',min_value=0,max_value=500,step = 1)

    with col3:
        BloodPressure = st.number_input('Blood Pressure value',min_value=0,max_value=200,step = 1)

    with col1:
        SkinThickness = st.number_input('Skin Thickness value',min_value=0,max_value=200,step = 1)

    with col2:
        Insulin = st.number_input('Insulin Level',min_value=0,max_value=1000,step = 1)

    with col3:
        BMI = st.number_input('BMI value',min_value=0.0,step=0.1)

    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.number_input('Age of the Person',min_value=0,max_value=150,step = 1)

    
    
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        if Pregnancies and Glucose and BloodPressure and SkinThickness and Insulin and BMI and DiabetesPedigreeFunction and Age:
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

            if (diab_prediction[0] == 1):
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        else:
            diab_diagnosis = 'Please enter all the required values'
    else:
        diab_diagnosis = ''

    st.success(diab_diagnosis)


        
   




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction ')

    st.write("### Patient Information")
    st.write("- Age")
    st.write("- Sex")
    st.write("- Chest Pain Type (4 values) in range of 0 to 3")
    st.write("- Resting Blood Pressure")
    st.write("- Serum Cholestoral in mg/dl")
    st.write("- Fasting Blood Sugar > 120 mg/dl (0 = No and 1 = Yes)")
    st.write("- Resting Electrocardiographic Results (values 0, 1, 2)")
    st.write("- Maximum Heart Rate Achieved")
    st.write("- Exercise Induced Angina (0 or 1)")
    st.write("- Oldpeak (ST depression induced by exercise relative to rest)")
    st.write("- Slope of the Peak Exercise ST Segment (0-2)")
    st.write("- Number of Major Vessels (0-3) Colored by Flourosopy")
    st.write("- Thal: 0 = Normal; 1 = Fixed Defect; 2 = Reversable Defect")
    
    st.write('##')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age',min_value=0,max_value=150, step= 1)
            
    with col2:
        sex = st.number_input('Sex',min_value=0,max_value=1, step= 1)
            
    with col3:
        cp = st.number_input('Chest Pain types',min_value=0,max_value=3, step= 1)
            
    with col1:
        trestbps = st.number_input('Resting Blood Pressure',min_value=0,max_value=300, step= 1)
            
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl',min_value=0,max_value=1000, step= 1)
            
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl',min_value=0,max_value=1, step= 1)
            
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results',min_value=0,max_value=2, step= 1)
            
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved',min_value=0,max_value=300, step= 1)
            
    with col3:
        exang = st.number_input('Exercise Induced Angina',min_value=0,max_value=1, step= 1)
            
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise',min_value=0.0,max_value=10.0, step= 0.1)
            
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment',min_value=0,max_value=2, step= 1)
            
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy',min_value=0,max_value=4, step= 1)
            
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',min_value=0,max_value=3, step= 1)

        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        if age and sex and cp and trestbps and chol and fbs and restecg and thalach and exang and oldpeak and slope and ca and thal:
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])                          
            
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        else:
            heart_diagnosis = 'Please enter all the required values'
    else:
        heart_diagnosis = ''
        
    st.success(heart_diagnosis)

    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction ")

    
    st.write('MDVP (Hz) - Average vocal fundamental frequency')
    st.write('MDVP: Fhi (Hz) - Maximum vocal fundamental frequency')
    st.write('MDVP: Flo (Hz) - Minimum vocal fundamental frequency')
    st.write('MDVP: Jitter (%) - Several measures of variation in fundamental frequency')
    st.write('MDVP: Jitter (Abs) - Several measures of variation in fundamental frequency')
    st.write('MDVP: RAP - Several measures of variation in fundamental frequency')
    st.write('MDVP: PPQ - Several measures of variation in fundamental frequency')
    st.write('Jitter: DDP - Several measures of variation in fundamental frequency')
    st.write('MDVP: Shimmer - Several measures of variation in amplitude')
    st.write('MDVP: Shimmer (dB) - Several measures of variation in amplitude')
    st.write('Shimmer: APQ3 - Several measures of variation in amplitude')
    st.write('Shimmer: APQ5 - Several measures of variation in amplitude')
    st.write('MDVP: APQ - Several measures of variation in amplitude')
    st.write('Shimmer: DDA - Several measures of variation in amplitude')
    st.write('NHR - Two measures of ratio of noise to tonal components in the voice')
    st.write('HNR - Two measures of ratio of noise to tonal components in the voice')
    st.write('Status - Health status of the subject (1 - Parkinson\'s, 0 - Healthy)')
    st.write('RPDE - Two nonlinear dynamical complexity measures')
    st.write('D2 - Two nonlinear dynamical complexity measures')
    st.write('DFA - Signal fractal scaling exponent')
    st.write('Spread1 - Three nonlinear measures of fundamental frequency variation')
    st.write('Spread2 - Three nonlinear measures of fundamental frequency variation')
    st.write('PPE - Three nonlinear measures of fundamental frequency variation')

    st.write("##")

    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0, max_value=349.259, step=0.001)

    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0, max_value=349.259, step=0.001)

    with col3:
        flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0, max_value=349.259, step=0.001)

    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0, max_value=0.01284, step=0.00001)

    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0, max_value=0.00011, step=0.00001)

    with col1:
        RAP = st.number_input('MDVP:RAP', min_value=0.0, max_value=0.00655, step=0.00001)

    with col2:
        PPQ = st.number_input('MDVP:PPQ', min_value=0.0, max_value=0.00908, step=0.00001)

    with col3:
        DDP = st.number_input('Jitter:DDP', min_value=0.0, max_value=0.01966, step=0.00001)

    with col4:
        Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0, max_value=0.06425, step=0.00001)

    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0, max_value=0.62600, step=0.00001)

    with col1:
        APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0, max_value=0.03490, step=0.00001)

    with col2:
        APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0, max_value=0.04825, step=0.00001)

    with col3:
        APQ = st.number_input('MDVP:APQ', min_value=0.0, max_value=0.05767, step=0.00001)

    with col4:
        DDA = st.number_input('Shimmer:DDA', min_value=0.0, max_value=0.10470, step=0.00001)

    with col5:
        NHR = st.number_input('NHR', min_value=0.0, max_value=0.02919, step=0.00001)

    with col1:
        HNR = st.number_input('HNR', min_value=0.0, max_value=33.047, step=0.001)

    with col2:
        RPDE = st.number_input('RPDE', min_value=0.0, max_value=0.792520, step=0.00001)

    with col3:
        DFA = st.number_input('DFA', min_value=0.0, max_value=0.792520, step=0.00001)

    with col4:
        spread1 = st.number_input('spread1', min_value=0.0, max_value=2.931070, step=0.00001)

    with col5:
        spread2 = st.number_input('spread2', min_value=0.0, max_value=0.434326, step=0.00001)

    with col1:
        D2 = st.number_input('D2', min_value=0.0, max_value=3.109010, step=0.00001)

    with col2:
        PPE = st.number_input('PPE', min_value=0.0, max_value=0.430788, step=0.00001)
            
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        if fo and fhi and flo and Jitter_percent and Jitter_Abs and RAP and PPQ and DDP and Shimmer and Shimmer_dB and APQ3 and APQ5 and APQ and DDA and NHR and HNR and RPDE and DFA and spread1 and spread2 and D2 and PPE:
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])                          
            
            if parkinsons_prediction[0] == 0:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "Please enter all the required values"
    else:
        parkinsons_diagnosis = ""
        
    st.success(parkinsons_diagnosis)
