import React, { createContext, useContext, useState, useEffect } from "react";
import api from "../lib/axios";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(() => {
    const stored = localStorage.getItem("user");
    return stored ? JSON.parse(stored) : null;
  });
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (user) {
      localStorage.setItem("user", JSON.stringify(user));
    } else {
      localStorage.removeItem("user");
    }
  }, [user]);

  async function signup(name, email, password) {
    setLoading(true);
    try {
      const { data } = await api.post("/signup", { name, email, password });
      localStorage.setItem("access_token", data.access_token);
      setUser(data.user);
      return data.user;
    } finally {
      setLoading(false);
    }
  }

  async function login(email, password) {
    setLoading(true);
    try {
      const { data } = await api.post("/login", { email, password });
      localStorage.setItem("access_token", data.access_token);
      setUser(data.user);
      return data.user;
    } finally {
      setLoading(false);
    }
  }

  function logout() {
    localStorage.removeItem("access_token");
    setUser(null);
  }

  return (
    <AuthContext.Provider value={{ user, loading, signup, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within an AuthProvider");
  return ctx;
}
