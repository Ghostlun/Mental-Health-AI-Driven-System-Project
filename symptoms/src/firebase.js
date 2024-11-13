// src/firebase.js

import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {
  apiKey: "AIzaSyBQ8WQP-9unJxhxWMLWPRjT6t2d-_8aAW4",
  authDomain: "cs6440-d4689.firebaseapp.com",
  projectId: "cs6440-d4689",
  storageBucket: "cs6440-d4689.firebasestorage.app",
  messagingSenderId: "625367661238",
  appId: "1:625367661238:web:13ec2ecb0291408de94417",
  measurementId: "G-E20D8Q9RCR"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export { app, analytics };
