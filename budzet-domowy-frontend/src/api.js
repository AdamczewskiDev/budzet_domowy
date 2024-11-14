// src/api.js

import axios from 'axios';

// URL API Django
const API_URL = "http://127.0.0.1:8000/api"; // Upewnij się, że backend Django działa pod tym adresem

// Tworzymy instancję axios z domyślnym adresem API
export const api = axios.create({
    baseURL: API_URL,
});

// Funkcja do logowania użytkownika
export const loginUser = async (username, password) => {
    const response = await api.post("/token/", { username, password });
    localStorage.setItem("access", response.data.access); // Zapisujemy token dostępu
    localStorage.setItem("refresh", response.data.refresh); // Zapisujemy token odświeżania
    return response.data;
};

// Funkcja do pobierania kategorii
export const getCategories = async () => {
    const accessToken = localStorage.getItem("access");
    const response = await api.get("/kategorie/", {
        headers: { Authorization: `Bearer ${accessToken}` }
    });
    return response.data;
};
