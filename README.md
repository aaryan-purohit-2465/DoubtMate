# 🤖 DoubtMate — Real-Time Classroom Doubt Solver (ML-Based)

DoubtMate is an intelligent, teacher-independent system that provides instant answers to student doubts using Natural Language Processing (NLP). Students can type a question, and the model returns the most relevant answer based on similarity search.

This project is developed collaboratively by a 5-member team and will be deployed on **18 December 2025** using Streamlit Cloud.

---

## 🎯 Objectives

- Provide real-time doubt clarification without teacher involvement  
- Reduce hesitation in classrooms and allow continuous learning  
- Match student queries with the closest pre-existing answer using NLP  
- Build a simple, fast, and deployable ML pipeline  
- Deliver a clean user interface for easy usage  

---

## 🧠 How the Model Works

### 1️⃣ Preprocessing  
- Lowercase text  
- Remove unnecessary characters  
- Clean and normalize questions for consistent processing  

### 2️⃣ Vectorization  
- Convert cleaned questions into numerical vectors using **TF-IDF**

### 3️⃣ Similarity Search  
- Compute **cosine similarity** between the student's question and dataset questions  
- Select the highest similarity score  

### 4️⃣ Output  
- Return the answer corresponding to the most relevant matched question  

This ensures that even if two questions are worded differently, the system can still identify the closest match.

---

## 👥 Team

- **Aaryan (Lead)**  
- **Abhinav**  
- **Atharv**  
- **Sharath**  
- **Sidhant**

Each team member contributes through dedicated branches merged via Pull Requests.

---

## 🚀 Deployment

The final app will be deployed on **Streamlit Community Cloud**, directly connected to this GitHub repository. Users will be able to type doubts and receive instant answers through a clean and interactive UI.

---

## 🏁 Goal

To build a fast, accurate, and accessible doubt-solving tool that enhances learning and supports students in real time.

