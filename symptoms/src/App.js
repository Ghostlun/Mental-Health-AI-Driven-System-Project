import React, { useState } from 'react';
import axios from 'axios';
import './App.css';


function App() {

  const [isSubmitted, setIsSubmitted] = useState(false); // Track form submission
  const [diagnosisGroup, setDiagnosisGroup] = useState(''); // Store diagnosis group
  const [errorMessage, setErrorMessage] = useState(''); // Store error messages
  const [advice, setAdvice] = useState('')
  const [loading, setLoading] = useState(false);


  const handleGetAdvice = async (e) => {
    e.preventDefault();

    setAdvice("It is not uncommon for car accidents to cause PTSD symptoms.  I would recommend seeing a therapist who has experience in treating trauma.  If it was a particularly bad accident you may want to find a therapist who uses EMDR (Eye Movement Desensitization Reprocessing) therapy.  You may also want to read the book ")

    const userInput = document.getElementById('userConcern').value.trim();

    if (!userInput) {
      setErrorMessage('Please enter your concern before requesting advice.');
      return;
    }

    setErrorMessage('');
    setLoading(true);
    setAdvice('');

    try {
      const response = await axios.post('https://pacific-hollows-13335-79599d21d756.herokuapp.com/generate-advice', {
        input: userInput,
        disorder: diagnosisGroup,
      });

      if (response.data.error) {
        setErrorMessage(response.data.error);
      } else {
        setAdvice(response.data.response);

        // Simulating additional results based on the generated advice
        const generatedResults = `Based on the advice provided, consider focusing on the following actions: 
        - Reflect on your priorities.
        - Develop a concrete action plan.
        - Seek additional resources if needed.`;

      }
    } catch (error) {
      console.error('Error fetching advice:', error);
      setErrorMessage('An error occurred while fetching advice. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  // added logic
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Gather form data
    const age = document.getElementById('age').value;
    const gender = document.getElementById('gender').value;
    const symptoms = document.getElementById('symptoms').value;
    const previousDiagnosis = document.getElementById('previousDiagnosis').value;
    const duration = document.getElementById('duration').value;
    const stressLevel = document.getElementById('stressLevel').value;
    const urgencyLevel = document.getElementById('urgencyLevel').value;

    // Validate form inputs
    if (!age || !gender || !symptoms || !previousDiagnosis || !duration || !stressLevel || !urgencyLevel) {
      setErrorMessage('Please fill out all required fields.');
      return;
    }
    
    // Prepare data payload for the API
    const requestData = {
      Age: parseInt(age),
      Symptoms: symptoms,
      Gender: gender,
      Prev_Diagnosis: previousDiagnosis,
      Duration: parseInt(duration),
      Stress_Level: parseInt(stressLevel),
      Urgency_Level: urgencyLevel,
    };

    // ToDo: Delete later
    console.log(requestData)
    // setDiagnosisGroup("Mood Disorder");

    try {
      const response = await axios.post('https://pacific-hollows-13335-79599d21d756.herokuapp.com/predict-diagnosis', requestData);
      
      if (!response || !response.data) {
        setErrorMessage('Unexpected response from the server.');
        console.error('Empty or invalid response:', response);
        return;
      }
    
      if (response.data.error) {
        console.log(response.data.error);
        setErrorMessage(response.data.error);
      } else if (response.data['Diagnosis Group']) {
        setDiagnosisGroup(response.data['Diagnosis Group']);
        setIsSubmitted(true);
      } else {
        setErrorMessage('Diagnosis group not found in the server response.');
        console.error('Invalid response structure:', response.data);
      }
    } catch (error) {
      setErrorMessage('An error occurred while processing your request. Please try again.');
      console.error('API call error:', error);
    }
  }    

  const handleGoBack = () => {
    setIsSubmitted(false);
  };


  // output
  if (isSubmitted) {
    return (
      <div className="App">
        <header className="App-header">
          <h1>Diagnosis Results</h1>
        </header>
        <main className="main-body">
          {/* Diagnosis Summary Section */}
          <div className="diagnosis-section">
            <h2>Your Diagnosis Summary</h2>
            <p>
              Based on the symptoms you provided, here is the diagnosis group that best matches your input:
            </p>
            <div className="diagnosis-output">
              <strong>Diagnosis Group:</strong> {diagnosisGroup}
            </div>
          </div>
  
          {/* Advice Section */}
          <div className="advice-section">
            <h3>Seek Advice</h3>
            <p>
              If you're facing challenges or need guidance, feel free to share your concerns below. 
            </p>
             
            <p>
            We'll provide helpful tips or advice tailored to your situation.
            </p>
            <div className="form-group">
              <label htmlFor="userConcern">
                <strong>Describe your concern:</strong>
                <br />
                <textarea
      id="userConcern"
      name="userConcern"
      className="form-control"
      placeholder="e.g., I failed an exam and feel overwhelmed. What should I do?"
      rows="8" // Increased number of rows for height
      style={{ width: '100%', resize: 'vertical' }} // Full width and resizable vertically
    ></textarea>
              </label>
            </div>
            <button className="btn btn-primary" onClick={handleGetAdvice}>
              Get Advice
            </button>
          </div>

          {/* Show Results Text Box When Advice is Available */}
          {advice && (
            <div className="form-group">
              <label htmlFor="adviceOutput">
                <strong>Your Advice:</strong>
              </label>
              <textarea
                id="adviceOutput"
                className="form-control"
                value={advice}
                readOnly
                rows="6"
                style={{ width: '100%', marginTop: '15px' }}
              />
            </div>
          )}
  
          <button className="btn btn-secondary" onClick={handleGoBack}>
            Go Back to Diagnosis Form
          </button>
        </main>
      </div>
    );
  }
  

  // maion form
  return (

    <div className="App">
    <header className="App-header">
      <h1>Mental Health Chat Bot</h1>
      <h3>Let's diagnose your mood first</h3>
    </header>
    <main className="main-body">
      <form onSubmit={handleSubmit}>
        {/* Age Field */}
        <div className="form-group">
          <label htmlFor="age">
            Age:
            <br />
            <input type="number" name="age" id="age" required />
          </label>
        </div>
  
        {/* Gender Field */}
        <div className="form-group">
          <label htmlFor="gender">
            Gender:
            <br />
            <select name="gender" id="gender" className="form-control" required>
              <option value="" disabled selected hidden>
                Select Gender
              </option>
              <option value="Male">Male</option>
              <option value="Female">Female</option>
              <option value="Non-binary">Don't want to answer</option>
            </select>
          </label>
        </div>
  
        {/* Duration Field */}
        <div className="form-group">
          <label htmlFor="duration">
            Duration (weeks):
            <br />
            <select name="duration" id="duration" className="form-control" required>
              <option value="" disabled selected hidden>
                Select Duration
              </option>
              {[...Array(50).keys()].map((num) => (
                <option key={num + 1} value={num + 1}>
                  {num + 1}
                </option>
              ))}
            </select>
          </label>
        </div>
  
        {/* Urgency Level Field */}
        <div className="form-group">
          <label htmlFor="urgencyLevel">
            Urgency Level:
            <br />
            <select name="urgencyLevel" id="urgencyLevel" className="form-control" required>
              <option value="" disabled selected hidden>
                Select Urgency Level
              </option>
              <option value="low">Low</option>
              <option value="moderate">Moderate</option>
              <option value="high">High</option>
              <option value="critical">Critical</option>
            </select>
          </label>
        </div>
  
        {/* Previous Diagnosis Field */}
        <div className="form-group">
          <label htmlFor="previousDiagnosis">
            Previous Diagnosis:
            <br />
            <select name="previousDiagnosis" id="previousDiagnosis" className="form-control" required>
              <option value="" disabled selected hidden>
                Select Previous Disorder
              </option>
              <option value="OCD">OCD</option>
              <option value="PTSD">PTSD</option>
              <option value="Bipolar Disorder">Bipolar Disorder</option>
              <option value="Anxiety">Anxiety</option>
              <option value="Depression">Depression</option>
              <option value="NaN">None</option>
            </select>
          </label>
        </div>
  
        {/* Symptoms Field */}
        <div className="form-group">
          <label htmlFor="symptoms">
            Symptoms:
            <br />
            <select name="symptoms" id="symptoms" className="form-control" required>
              <option value="" disabled selected hidden>
                Select a Symptom
              </option>
              <option value="feeling anxious">Feeling Anxious</option>
              <option value="excessive worry">Excessive Worry</option>
              <option value="trouble sleeping">Trouble Sleeping</option>
              <option value="loss of interest in activities">Loss of Interest in Activities</option>
              <option value="panic attacks">Panic Attacks</option>
              <option value="lack of concentration">Lack of Concentration</option>
              <option value="feeling irritable">Feeling Irritable</option>
              <option value="feeling sad">Feeling Sad</option>
              <option value="feeling overwhelmed">Feeling Overwhelmed</option>
            </select>
          </label>
        </div>
  
        {/* Stress Level Field */}
        <div className="form-group">
          <label htmlFor="stressLevel">
            Stress Level:
            <br />
            <select name="stressLevel" id="stressLevel" className="form-control" required>
              <option value="" disabled selected hidden>
                Select Stress Level
              </option>
              {[...Array(10).keys()].map((num) => (
                <option key={num + 1} value={num + 1}>
                  {num + 1}
                </option>
              ))}
            </select>
          </label>
        </div>
  
        {/* Submit Button */}
        <div className="form-group">
          <button type="submit">Submit</button>
        </div>
      </form>
    </main>
  </div>
  
    
  );

}


export default App;