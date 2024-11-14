// src/components/Categories.js

import React, { useEffect, useState } from 'react';
import { api } from '../api';

function Categories() {
    const [categories, setCategories] = useState([]);
    const [newCategory, setNewCategory] = useState("");

    useEffect(() => {
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

        fetchCategories();
    }, []);

    const handleAddCategory = async (e) => {
        e.preventDefault();
        try {
            const accessToken = localStorage.getItem("access");
            const response = await api.post(
                "/kategorie/",
                { nazwa: newCategory },
                { headers: { Authorization: `Bearer ${accessToken}` } }
            );
            setCategories([...categories, response.data]);
            setNewCategory("");
        } catch (error) {
            console.error("Błąd podczas dodawania kategorii:", error);
        }
    };

    return (
        <div>
            <h2>Kategorie</h2>
            <ul>
                {categories.map((category) => (
                    <li key={category.id}>{category.nazwa}</li>
                ))}
            </ul>
            <form onSubmit={handleAddCategory}>
                <input
                    type="text"
                    value={newCategory}
                    onChange={(e) => setNewCategory(e.target.value)}
                    placeholder="Nowa kategoria"
                />
                <button type="submit">Dodaj kategorię</button>
            </form>
        </div>
    );
}

export default Categories;
