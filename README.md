# **AI-Driven Mental Health Support System**

## **Project Overview**
This project aims to build an AI-driven platform that offers personalized mental health treatment recommendations based on user-reported concerns.  
Once the user provides their mental health input, the system analyzes it using a fine-tuned Large Language Model (LLM) trained on counseling and treatment data. The user can interact with the model in a therapeutic manner, allowing it to assist with emotional comfort and support.  
Ultimately, the goal is to provide users with meaningful, data-driven suggestions to help manage their mental well-being.

## **Project Scope**

1. **AI Model Training**  
   - Fine-tune LLMs (e.g., GPT or LLaMA) using two key datasets:
     - Mental health symptoms
     - Drug/treatment recommendations

2. **Concern Analysis & Recommendation Generation**  
   - Analyze user input to identify mental health concerns.
   - Provide AI-generated, personalized treatment or support suggestions.

3. **Interactive Response Interface**  
   - Enable users to engage with the AI model for real-time support.
   - Display treatment plans or comforting guidance on a dedicated results page.

## **Technology Stack**

- **Frontend**: React.js  
- **Backend**: Python (Flask or Django)  
- **AI Models**: GPT (fine-tuned with OpenAI), LLaMA (planned for future integration)  
- **Data Sources**:
  - [Mental Health Counsel Chatbot Dataset (Kaggle)](https://www.kaggle.com/code/weiting016/mental-health-counsel-chatbot/notebook)
  - [Counsel Chat Dataset (HuggingFace)](https://huggingface.co/datasets/nbertagnolli/counsel-chat?row=30)

## **Approach with OpenAI Fine-Tuning**

1. **Data Cleaning**  
   - Remove null or empty entries.
   - Extract relevant Q&A pairs from each dataset.

2. **Tokenization Analysis**  
   - Measure and record token lengths for each entry.  
   - Examples:
     - **Maximum token length**: 1138  
     - **Average token length**: ~229  
     - **95th percentile token length**: 557  
   - Drop samples exceeding safe token limits or containing irrelevant information.

3. **Dataset Preparation**  
   - Convert cleaned data into **JSONL** format.
   - Ensure formatting aligns with OpenAI's fine-tuning structure (`{"messages": [{"role": "user", "content": ...}, {"role": "assistant", "content": ...}]}`).

4. **Model Training**  
   - Use OpenAI's `gpt-3.5-turbo` model for fine-tuning.
   - Upload processed dataset and fine-tune using OpenAI CLI or API.

5. **Integration**  
   - Connect the fine-tuned model with the backend for real-time inference.
   - Display results through the React-based frontend UI.

## **LLaMA Dataset Usage (Future Scope)**
- In future phases, LLaMA models will be explored for on-device or open-source deployment.
- Focus will be on expanding language support and fine-tuning using broader mental health datasets.
- Ideal for offline or private AI chatbot scenarios, especially when OpenAI API use is restricted.


## **Risks and Considerations**

- **Data Limitations**: Datasets are synthetic or limited to counseling sessions, which may reduce applicability in complex real-world cases.
- **Overfitting**: Excessively specific data can lead to narrow, repetitive responses — requires validation and testing.
- **Model Scalability**: Additional training data may be necessary to handle broader user concerns.
- **Ethical & Privacy Issues**: The system must clearly state it's not a replacement for professional diagnosis and ensure data confidentiality


### **Backend Setup**
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Create and activate the virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # For Linux/Mac
   myenv\Scripts\activate     # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   flask run
   ```

---

### **Frontend Setup**
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

---

You are now ready to use the backend and frontend services!
