// src/components/Transactions.js

import React, { useEffect, useState } from 'react';
import { api } from '../api';

function Transactions() {
    const [transactions, setTransactions] = useState([]);
    const [categories, setCategories] = useState([]);
    const [newTransaction, setNewTransaction] = useState({
        kwota: "",
        data: "",
        opis: "",
        kategoria: ""
    });

    useEffect(() => {
        const fetchTransactions = async () => {
            try {
                const accessToken = localStorage.getItem("access");
                const response = await api.get("/transakcje/", {
                    headers: { Authorization: `Bearer ${accessToken}` }
                });
                setTransactions(response.data);
            } catch (error) {
                console.error("Błąd podczas pobierania transakcji:", error);
            }
        };

        const fetchCategories = async () => {
            try {
                const accessToken = localStorage.getItem("access");
                const response = await api.get("/kategorie/", {
                    headers: { Authorization: `Bearer ${accessToken}` }
                });
                setCategories(response.data);
            } catch (error) {
                console.error("Błąd podczas pobierania kategorii:", error);
            }
        };

        fetchTransactions();
        fetchCategories();
    }, []);

    const handleAddTransaction = async (e) => {
        e.preventDefault();
        try {
            const accessToken = localStorage.getItem("access");
            const response = await api.post("/transakcje/", newTransaction, {
                headers: { Authorization: `Bearer ${accessToken}` }
            });
            setTransactions([...transactions, response.data]);
            setNewTransaction({ kwota: "", data: "", opis: "", kategoria: "" });
        } catch (error) {
            console.error("Błąd podczas dodawania transakcji:", error);
        }
    };

    return (
        <div>
            <h2>Transakcje</h2>
            <ul>
                {transactions.map((transaction) => (
                    <li key={transaction.id}>
                        {transaction.kwota} PLN - {transaction.opis} - {transaction.data}
                    </li>
                ))}
            </ul>
            <form onSubmit={handleAddTransaction}>
                <input
                    type="number"
                    placeholder="Kwota"
                    value={newTransaction.kwota}
                    onChange={(e) => setNewTransaction({ ...newTransaction, kwota: e.target.value })}
                />
                <input
                    type="date"
                    value={newTransaction.data}
                    onChange={(e) => setNewTransaction({ ...newTransaction, data: e.target.value })}
                />
                <input
                    type="text"
                    placeholder="Opis"
                    value={newTransaction.opis}
                    onChange={(e) => setNewTransaction({ ...newTransaction, opis: e.target.value })}
                />
                <select
                    value={newTransaction.kategoria}
                    onChange={(e) => setNewTransaction({ ...newTransaction, kategoria: e.target.value })}
                >
                    <option value="">Wybierz kategorię</option>
                    {categories.map((category) => (
                        <option key={category.id} value={category.id}>
                            {category.nazwa}
                        </option>
                    ))}
                </select>
                <button type="submit">Dodaj transakcję</button>
            </form>
        </div>
    );
}

export default Transactions;
