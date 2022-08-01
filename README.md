# Neuro Journal 🧠 📖



## Inspiration 	💡
The biggest barrier to crisis response is feeling helpless even if you open up and say something it's not going to do anything. The person on the other side might not say anything and actually, help you because they don’t understand you. If an individual is under stress, it is harder to communicate with words. However, if we have brain wave data that indicates stress, we can have healthcare professionals make a prognosis or diagnosis early on and this could be done using the muse to check for elevated stress.



## What does our project do? 💻
NeuroJournal has been working on an AI chatbot to detect stress while collecting patient brainwaves. So even when they are not talking, we have a nonverbal way of telling the waveform that is associated with stress and can further Incorporate clinician or therapist expertise. The individual would journal a stressful event and natural language processing would be used to detect the words and assign them a rating score.



## Running Neuro Journal 🏃

download Anaconda
* https://www.anaconda.com/products/distribution 

create a conda environment 
```conda create --name myenv```

runn streamlit 
```streamlit run index.py```



# How we built it 🧩
We mostly programmed in VS Code while utilizing Python as the main language. PyQt5 boilerplates were used to record EEG data from Muse and openBCI hardware, which was further processed using the EEGrunt library. Our web app was built on Streamlit. It includes a journaling (user input) page, an About Us page, and an embedded Chatterbot. The libraries used for NLP were tensorflow, pandas, numpy, sklearn, nltk, tensorflow-bert, matplotlib, seaborn, Re, string, logging. We trained the BERT sentiment analysis model using logistic regression, SVM, random forest and neural networks techniques on the Dreaddit dataset. To train the model in BERT, we predicted 15% of the tokens in the training data, which were randomly picked.



# What we built it with 🛠️
* Streamlit.io
* python
* sklearn
* tensorflow
* tensorflow-bert
* pyqt5
* chatterbot
