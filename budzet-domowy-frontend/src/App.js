// src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Categories from './components/Categories';

function App() {
    return (
        <Router>
            <div>
                <h1>Aplikacja Budżet Domowy</h1>
                <Routes>
                    <Route path="/" element={<Login />} />
                    <Route path="/categories" element={<Categories />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
