// src/components/Categories.js

import React, { useEffect, useState } from 'react';
import { getCategories } from '../api';

function Categories() {
    const [categories, setCategories] = useState([]);

    useEffect(() => {
        const fetchCategories = async () => {
            try {
                const data = await getCategories();
                setCategories(data);
            } catch (error) {
                console.error("Błąd podczas pobierania kategorii:", error);
            }
        };
        fetchCategories();
    }, []);

    return (
        <div>
            <h2>Kategorie</h2>
            <ul>
                {categories.map((category) => (
                    <li key={category.id}>{category.nazwa}</li>
                ))}
            </ul>
        </div>
    );
}

export default Categories;
