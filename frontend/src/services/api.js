import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/users/',
});

export const registerUser = (userData) => API.post('register/', userData);
export const loginUser = (userData) => API.post('login/', userData);
