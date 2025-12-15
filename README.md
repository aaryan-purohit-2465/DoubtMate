# 🤖 DoubtMate — Real-Time Classroom Doubt Solver

DoubtMate is a machine learning–based, teacher-independent classroom doubt solver that provides instant answers to student queries.  
Students can type their doubts, and the system responds with the most relevant answer using Natural Language Processing (NLP).

---

## 🎯 Objectives

- Provide instant doubt resolution without teacher intervention  
- Reduce hesitation among students in asking questions  
- Support continuous and self-paced learning  
- Use NLP techniques to match student queries with relevant answers  
- Build a simple, fast, and deployable ML-based solution  

---

## 🧠 How the Model Works

1. **Text Preprocessing**  
   Student questions are cleaned by removing unnecessary characters and normalizing text.

2. **Vectorization**  
   Questions are converted into numerical form using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

3. **Similarity Matching**  
   The student query is compared with stored questions using **cosine similarity**.

4. **Answer Retrieval**  
   The answer corresponding to the most similar question is returned in real time.

---

## 👥 Team

- Aaryan (Team Lead)  
- Abhinav  
- Atharv  
- Sharath  
- Sidhant  

---

## 🚀 Deployment

The application will be deployed using **Streamlit Community Cloud** with a public URL for access.

---

## 🏁 Goal

To build a reliable, real-time doubt-solving system that enhances learning efficiency and promotes independent problem-solving among students.