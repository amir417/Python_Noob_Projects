import React from "react";
import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

// Importing individual pages
import { Home, Projects, Apply } from './pages';
import { NavBar } from './components';

function App() {
  return (     
    <Router>
      <NavBar />
      <div className="pages">
        <Routes>
          <Route path="/" element={<Home/>} />
          <Route path="/projects" element={<Projects/>} />
          <Route path="/apply" element={<Apply/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;