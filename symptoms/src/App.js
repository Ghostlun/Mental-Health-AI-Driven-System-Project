import './App.css';
import { app, analytics } from './firebase';


function App() {

  return (

      <div className="App">
        <header className="App-header">
          <h1>Symptom Chatbot</h1>
        </header>
        <main className="main-body">
          <form>
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
                <input name="gender" id="gender"/>
              </label>
            </div>
            <div className="form-group">
              <label htmlFor="duration">
                Duration (weeks):
                <br/>
                <input type="number" name="duration" id="duration"/>
              </label>
            </div>
            <div className="form-group">
              <label htmlFor="symptom">
                Enter your symptoms:
                <br/>
                <input name="symptom" id="symptomInput"/>
              </label>
            </div>
            <div className="form-group">
              <label htmlFor="previousDiagnosis">
                Previous Diagnosis:
                <br/>
                <input name="previousDiagnosis" id="previousDiagnosis"/>
              </label>
            </div>
            <div className="form-group">
              <label htmlFor="stressLevel">
                Stress Level:
                <br/>
                <input type="number" name="stressLevel" id="stressLevel"/>
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