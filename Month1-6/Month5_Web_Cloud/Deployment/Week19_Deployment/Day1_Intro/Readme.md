### **Day 1: Introduction to Deployment + Free Platforms Overview**

#### **Objective:**

* Understand the basic concept of deploying a web application and machine learning models.
* Explore free platforms like **Render**, **Railway**, and **HuggingFace Spaces** that allow you to deploy without needing a credit card.

#### **Steps:**

---

### **1. What is Deployment?**

Deployment refers to the process of making your machine learning models and web applications available for public or private use, typically by hosting them on a server or cloud platform. This allows users to interact with your model or app through APIs or web interfaces.

---

### **2. Deployment Options (Free Platforms Overview)**

**a. HuggingFace Spaces:**

* A platform for sharing and deploying machine learning models.
* Great for hosting models and demos.
* **Free tier**: Allows for hosting demos with no cost (especially with Gradio/Streamlit interfaces).
* **Example Use Case**: You can deploy a trained model (like a sentiment analysis model) and create a web interface for users to interact with it.

**b. Render:**

* Provides free hosting for both **backend services** (APIs) and **static websites**.
* Ideal for deploying FastAPI, Flask, or other backend frameworks.
* **Free tier**: Includes free static web hosting and backend server hosting (with limited compute).
* **Example Use Case**: Deploy a FastAPI or Flask backend to serve a machine learning model.

**c. Railway:**

* A platform that simplifies deploying web apps, APIs, and even databases.
* **Free tier**: Allows you to deploy backend applications without the need for a credit card.
* **Example Use Case**: Deploy a machine learning API with FastAPI or Flask that serves predictions.

---

### **3. Signing Up on Platforms (No Credit Card Required)**

**a. HuggingFace Spaces**:

* **Sign up link**: [HuggingFace Signup](https://huggingface.co/join)
* After signing up, create a new Space (demo environment) and link it to a GitHub repository or upload your model.

**b. Render**:

* **Sign up link**: [Render Signup](https://dashboard.render.com/register)
* After signing up, create a new web service (Static or Web Service) and deploy from your GitHub repository.

**c. Railway**:

* **Sign up link**: [Railway Signup](https://railway.app/signup)
* Once logged in, create a new project, link it to your GitHub repository, and deploy your app (FastAPI, Flask, etc.).

---

### **4. Setting up Your Project for Deployment**

You need to ensure that your code is structured properly for deployment.

* **Backend Code (FastAPI, Flask)**:

  * Your backend application should be ready to handle incoming requests and respond with predictions. This involves making sure that:

    * The model is loaded and ready to serve.
    * The API endpoint is defined and works correctly.
    * Use `gunicorn` for production-ready deployment.
* **Frontend (HTML, CSS, JS)**:

  * Your frontend code should be ready and can be static (for simple forms) or dynamic (using JS or a framework like React).
  * Frontend can be connected to the backend via API calls.

---

### **5. Overview of GitHub Workflow for Deployment**

* **GitHub repository**: All of your code, whether it’s the backend (FastAPI/Flask) or frontend (HTML/JS), should be pushed to a GitHub repository. These platforms will pull from your GitHub repo to deploy.

* **Deployment Pipeline**:

  * After linking your repository, the platform automatically deploys the app. Changes made to the repo trigger automatic redeployment.

---

### **6. Deployment Process on Platforms:**

**a. HuggingFace Spaces**:

1. Create a new Space.
2. Choose a demo app (e.g., Gradio, Streamlit).
3. Upload the model or link the GitHub repo.
4. Test the deployed model demo by interacting with it on the Space.

**b. Render**:

1. Create a new service (choose static for websites or web service for APIs).
2. Link your GitHub repository.
3. Specify the build and start commands for the backend (e.g., `uvicorn app:app` for FastAPI).
4. Configure any environment variables (like `PORT`).

**c. Railway**:

1. Create a new project and link it to GitHub.
2. Deploy the app with an easy configuration.
3. Use the `rails` command to deploy and test.

---

