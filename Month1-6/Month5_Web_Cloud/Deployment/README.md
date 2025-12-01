
### **🗓️ Week 19 – Deployment**

#### **Day 1: Introduction to Deployment + Free Platforms Overview**

**Focus:**

* Understanding the deployment process for ML models and web apps.
* Exploring free platforms like **HuggingFace Spaces**, **Render**, and **Railway** that don't require a credit card.

**Platforms to Learn:**

1. **HuggingFace Spaces**

   * A platform to host machine learning models and demos.
   * **Free tier**: Ideal for serving ML models and demos directly.
2. **Render**

   * Free hosting for web apps, FastAPI, and ML apps.
   * **Free tier**: Provides a static web page, backend servers, and databases (without the need for credit card).
3. **Railway**

   * Free tier for hosting web apps and ML models.
   * Can deploy FastAPI or Flask apps with machine learning integration.

---

#### **Day 2: Deploying Simple Web Apps**

**Focus:**

* Learn the basics of deploying static websites.
* Deploy a simple HTML, CSS, and JavaScript front end.

**Steps:**

1. **Use Render or Railway** to deploy a simple static website (HTML, CSS, and JS).
2. **Deploying with Render:**

   * Use GitHub repository to link and deploy static content (HTML).
   * Link your project to GitHub and deploy it directly from there (free tier).
3. **Deploying with Railway:**

   * Set up a new project and deploy static websites directly.
   * Can be done without any credit card info.

---

#### **Day 3: Deploying FastAPI or Flask Web Apps**

**Focus:**

* Deploy a Python backend (FastAPI or Flask) to serve your ML models.

**Steps:**

1. **Set up your FastAPI or Flask app** with a model (like your diabetes prediction model).
2. **Deploy with Render:**

   * You can deploy FastAPI or Flask backends on Render’s free tier.
   * Make sure your app runs with `gunicorn` for production.
3. **Deploy with Railway:**

   * Create a new backend app using FastAPI or Flask.
   * Integrate the model and deploy it using Railway's free tier.
4. **Test deployment** by sending API requests.

---

#### **Day 4: Integrating Frontend with Backend (API Fetching)**

**Focus:**

* Connect your frontend (HTML + JS) to the backend (FastAPI/Flask) using API calls.

**Steps:**

1. **Frontend:**

   * Create an HTML form for user input (like BMI, diabetes, etc.).
   * Use JavaScript to handle API requests (fetch API).
2. **Backend:**

   * Create an endpoint on your FastAPI or Flask app to process inputs and return the model's predictions.
3. **Deploy:**

   * Use the same deployment platforms (Render or Railway) to deploy both backend and frontend.
   * **Free tier:** Works well for small apps, no credit card needed.

---

#### **Day 5: Deploying ML Model with HuggingFace Spaces**

**Focus:**

* Deploy your ML models directly on **HuggingFace Spaces**.

**Steps:**

1. **Create a HuggingFace account** (no credit card required).
2. **Build a model demo:**

   * You can upload a pre-trained ML model (e.g., diabetes prediction model).
   * Use Gradio or Streamlit for the user interface.
3. **Deploy the app:**

   * Push the app to a HuggingFace space and deploy it.
   * **No credit card required** for the free tier.

---

#### **Day 6: Using GitHub for Deployment (Linking Repositories)**

**Focus:**

* Learn how to link your **GitHub repositories** with deployment platforms.

**Steps:**

1. **GitHub and Render:**

   * Push your project to GitHub.
   * Connect the GitHub repository to Render or Railway and deploy it.
2. **GitHub Actions for CI/CD:**

   * Set up **CI/CD pipelines** to automate deployments (optional).

---

#### **Day 7: Final Project Deployment**

**Focus:**

* Deploy the **full-stack ML application** (both frontend and backend).
* **Test your deployment on Render, Railway, or HuggingFace Spaces**.

**Steps:**

1. **Deploy your ML web app** end-to-end (both backend + frontend).
2. **Ensure that both the frontend and backend are connected properly**.
3. **Test everything**:

   * Ensure that the model works and is served correctly from the backend.
   * Test frontend input and backend predictions using API calls.

---

### **Free Deployment Platform Overview**

Here’s a summary of the free tiers available on the platforms:

| Platform        | Free Tier Limits                                | No Credit Card |
| --------------- | ----------------------------------------------- | -------------- |
| **Render**      | Free hosting for web apps, databases, and APIs. | ✅              |
| **Railway**     | Free hosting for web apps, ML models, APIs.     | ✅              |
| **HuggingFace** | Free for ML demos, Gradio/Streamlit interfaces. | ✅              |

---
