import React, { useState } from 'react';
import './App.css';
import { app, analytics } from './firebase';


function App() {

  const [isSubmitted, setIsSubmitted] = useState(false); // Track form submission
  const [diagnosisGroup, setDiagnosisGroup] = useState(''); // Store diagnosis group

  // added logic
  const groupDiagnosis = (diagnosis) => {
    if (['Panic Disorder', 'Anxiety'].includes(diagnosis)) {
      return 'Anxiety Disorders';
    } else if (['Depression', 'Burnout'].includes(diagnosis)) {
      return 'Mood Disorders';
    } else if (diagnosis === 'Stress') {
      return 'Stress-Related Disorders';
    }
    return 'Unknown';
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const previousDiagnosis = document.getElementById('previousDiagnosis').value;

    const group = groupDiagnosis(previousDiagnosis);

    setDiagnosisGroup(group);
    setIsSubmitted(true);
  };

  const handleGoBack = () => {
    setIsSubmitted(false);
  };

  // output
  if (isSubmitted) {
    return (
        <div className="App">
          <header className="App-header">
            <h1>Diagnosis Output</h1>
          </header>
          <main className="main-body">
            <div className="form-group">
              <label htmlFor="symptom">
                Enter your symptoms:
                <br/>
                <input name="symptom" id="symptomInput"/>
              </label>
            </div>
            <h2>Diagnosis Group</h2>
            <p>{diagnosisGroup}</p>
            <button onClick={handleGoBack}>Go Back</button>
          </main>
        </div>
    );
  }

  // maion form
  return (

      <div className="App">
        <header className="App-header">
          <h1>Symptom Chatbot</h1>
        </header>
        <main className="main-body">
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="age">
                Age:
                <br/>
                <input type="number" name="age" id="age"/>
              </label>
            </div>
            <div className="form-group">
              <label htmlFor="gender">
                Gender (M/F):
                <br/>
                <select name="gender" id="gender" className="form-control">
                  <option value="">Select Gender</option>
                  <option value="Male">Male</option>
                  <option value="Female">Female</option>
                  <option value="Non-binary">Non-binary</option>
                  <option value="Other">Other</option>
                </select>
              </label>
            </div>
            <div className="form-group">
              <label htmlFor="duration">
                Duration (weeks):
                <br/>
                {/*<input type="number" name="duration" id="duration"/>*/}
                <select name="duration" id="duration" className="form-control">
                  <option value="">Select Duration</option>
                  {[...Array(115).keys()].map((num) => (
                      <option key={num + 1} value={num + 1}>
                        {num + 1}
                      </option>
                  ))}
                </select>
              </label>
              <div className="form-group">
                <label htmlFor="urgencyLedvel">
                  Urgency Level:
                  <br/>
                  {/*<input name="urgencyLedvel" id="urgencyLedvel"/>*/}
                  <select name="urgencyLedvel" id="urgencyLedvel" className="form-control">
                    <option value="">Urgency Level</option>
                    <option value="low">Low</option>
                    <option value="moderrate">Moderate</option>
                    <option value="high">High</option>
                    <option value="critical">Critical</option>
                  </select>
                </label>
              </div>
            </div>
            <div className="form-group">
              <label htmlFor="previousDiagnosis">
                Previous Diagnosis:
                <br/>
                {/*<input name="previousDiagnosis" id="previousDiagnosis"/>*/}
                <select name="previousDiagnosis" id="previousDiagnosis" className="form-control">
                  <option value="">Select Previous Disorder</option>
                  <option value="OCD">OCD</option>
                  <option value="PTSD">PTSD</option>
                  <option value="Bipolar Disorder">Bipolar Disorder</option>
                  <option value="Anxiety">Anxiety</option>
                  <option value="Depression">Depression</option>
                  <option value="NaN">NaN</option>
                </select>
              </label>
            </div>
            <div className="form-group">
              <label htmlFor="stressLevel">
                Stress Level:
                <br/>
                {/*<input type="number" name="stressLevel" id="stressLevel"/>*/}
                <select name="stressLevel" id="stressLevel" className="form-control">
                  <option value="">Select Stress Level</option>
                  {[...Array(10).keys()].map((num) => (
                      <option key={num + 1} value={num + 1}>
                        {num + 1}
                      </option>
                  ))}
                </select>
              </label>
            </div>
            <div className="form-group">
              <label htmlFor="mood">
                Mood:
                <br/>
                <input name="moom" id="mood"/>
              </label>
            </div>
            <div className="form-group">
              <button type="submit">Submit</button>
            </div>
          </form>
        </main>
      </div>
  );

}


export default App;