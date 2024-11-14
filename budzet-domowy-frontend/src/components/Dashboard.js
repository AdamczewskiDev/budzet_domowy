// src/components/Dashboard.js

import React, { useEffect, useState } from 'react';
import { api } from '../api';

function Dashboard() {
    const [stats, setStats] = useState({ wydatki: 0, przychody: 0 });

    useEffect(() => {
        const fetchStats = async () => {
            try {
                const accessToken = localStorage.getItem("access");
                const response = await api.get('/statystyki/', {
                    headers: { Authorization: `Bearer ${accessToken}` }
                });
                setStats(response.data);
            } catch (error) {
                console.error("Błąd podczas pobierania statystyk:", error);
            }
        };

        fetchStats();
    }, []);

    return (
        <div>
            <h2>Podsumowanie finansowe</h2>
            <p>Łączne wydatki: {stats.wydatki} PLN</p>
            <p>Łączne przychody: {stats.przychody} PLN</p>
        </div>
    );
}

export default Dashboard;
