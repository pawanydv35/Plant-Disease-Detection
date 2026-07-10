import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || "http://localhost:8000",
});

// Attach the JWT (if present) to every outgoing request, so individual
// components never have to remember to set the Authorization header.
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access_token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// If the backend ever returns 401, the token is invalid/expired —
// clear it so the UI doesn't keep pretending the user is logged in.
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem("access_token");
      localStorage.removeItem("user");
    }
    return Promise.reject(error);
  }
);

export default api;
