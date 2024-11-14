// src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Categories from './components/Categories';
import Dashboard from './components/Dashboard';
import Transactions from './components/Transactions';

function App() {
    return (
        <Router>
            <div>
                <h1>Aplikacja Budżet Domowy</h1>
                <Routes>
                    <Route path="/" element={<Login />} />
                    <Route path="/categories" element={<Categories />} />
                    <Route path="/dashboard" element={<Dashboard />} /> {/* Dodajemy Dashboard */}
                    <Route path="/transactions" element={<Transactions />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
