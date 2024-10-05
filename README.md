# AgriData Team Documentation: NASA Space Apps Challenge

## Project Overview

AgriData is participating in the NASA Space Apps competition to develop an intelligent system that assists farmers and agricultural engineers in managing their farms and crops more efficiently. The system leverages artificial intelligence and machine learning to monitor the health of plants, detect diseases, and provide tailored recommendations for farm management. The system focuses on the following key functionalities:

1. **Disease Detection Models for Plants**: 
   - **Crops Supported**: Rice, Corn, Potato, Tomato
   - **Objective**: Identify plant diseases early to prevent crop damage and reduce yield loss.
  
2. **Recommendation System (LLM)**:
   - **Objective**: Provide guidance and suggestions to farmers based on weather conditions, geographic location, the type of plants being cultivated, and land type.
   - **Languages Supported**: Arabic and English
- Screenshot:
   ![Recommendation System]([./images/recommendation_system.png](https://github.com/Ahmedtronic/NasaSpaceApps2024/blob/main/testing%20recommnder%20en.png))

## Key Features

1. **Plant Disease Detection**:
   - **Model Architecture**: Each plant disease detection model is built using **TensorFlow**. These models are trained on a variety of plant diseases specific to Rice, Corn, Potato, and Tomato. The models can accurately classify and identify common diseases based on image inputs from farmers.
   
   - **Process**:
     1. Farmers or agricultural engineers capture images of affected plants.
     2. The images are fed into the disease detection models.
     3. The models return a diagnosis, identifying the disease and suggesting possible remedies.

2. **LLM-Based Recommendation System**:
   - **Objective**: Generate personalized recommendations based on weather conditions, land type, location, and the types of crops planted.
   
   - **Input Parameters**:
     - Weather data (temperature, humidity, etc.)
     - Location (latitude, longitude)
     - Land type (sandy, clay, loam, etc.)
     - Plant type (crop species being grown)

   - **Output**:
     - The model suggests procedures such as irrigation techniques, fertilizer application, pest control, and harvest timing. 
     - Recommendations are provided in **both Arabic and English**, making the system accessible to a wider range of users.

## Tools and Technologies

### 1. **Google Colab**:
   - **Purpose**: The primary development environment used to train, evaluate, and deploy our models. Google Colab provided the computational resources (GPUs) needed to handle the heavy lifting of training machine learning models.
   
### 2. **TensorFlow**:
   - **Purpose**: TensorFlow was used to build and train the plant disease detection models. The library’s deep learning capabilities allowed us to develop robust convolutional neural networks (CNNs) for image classification.

### 3. **Streamlit**:
   - **Purpose**: Streamlit was used to build the user interface of the application, allowing farmers to upload images, input location, and land type, and receive disease diagnoses and farm management recommendations. The simplicity of Streamlit enabled us to rapidly prototype the user interface and deliver results in real-time.

### 4. **Hugging Face**:
   - **Purpose**: Hugging Face was leveraged to create the language models for the recommendation system. Pre-trained models were fine-tuned to generate context-aware suggestions in both English and Arabic, based on the input parameters (weather, land type, etc.).

### 5. **Python**:
   - **Purpose**: Python was the main programming language used for all components of the project. Its extensive ecosystem of libraries, including TensorFlow, Pandas, and Hugging Face transformers, made it ideal for developing both the machine learning models and the web application.

## How It Works

1. **Disease Detection**:
   - The farmer uploads an image of a plant with suspected disease into the Streamlit web interface.
   - The image is processed using one of the pre-trained TensorFlow models to classify the disease.
   - The diagnosis is displayed along with suggestions for treatment.

2. **Recommendation System**:
   - The farmer inputs key details such as location, plant type, and land type.
   - Weather data is either manually provided or fetched through external APIs.
   - The Hugging Face-based LLM generates recommendations in real-time, advising the farmer on necessary procedures (irrigation, fertilization, etc.).
   - The recommendations are presented in both Arabic and English.


## Models Accuracies:
- Corn : Train : 99% , Test : 96%
- Rice : Train : 99% , Test : 99%
- Tomato: Train: 94% , Test : 94%
- Potato: Train: 98% , Test : 97%
all models accuricies are detailed in the notebooks.
  

## Conclusion

AgriData's system provides a comprehensive and user-friendly solution to help farmers and agricultural engineers manage their crops more effectively. By combining machine learning for plant disease detection with an LLM-based recommendation system, we enable more informed decision-making and reduce the risks associated with crop failure. Our solution is scalable, multilingual, and designed to support farmers across diverse regions and crop types.

## Future Improvements

- **Expand Crop Support**: Integrate additional crops beyond Rice, Corn, Potato, and Tomato.
- **Enhanced Localization**: Incorporate more localized weather data and agricultural best practices specific to different regions.
- **Mobile Application**: Develop a mobile app version of the system for even easier access by farmers in remote areas.
