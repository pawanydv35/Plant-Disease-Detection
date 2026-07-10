import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { toast } from "sonner";
import { Leaf } from "lucide-react";
import { useAuth } from "../context/AuthContext.jsx";

export default function Login() {
  const { login, loading } = useAuth();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    setError("");
    try {
      await login(email, password);
      toast.success("Welcome back!");
      navigate("/dashboard");
    } catch (err) {
      const message = err.response?.data?.detail || "Something went wrong. Please try again.";
      setError(message);
    }
  }

  return (
    <div className="flex min-h-[80vh] items-center justify-center px-6 py-16">
      <div className="w-full max-w-sm">
        <div className="mb-8 flex flex-col items-center text-center">
          <Leaf className="text-forest" size={32} />
          <h1 className="mt-3 font-display text-2xl text-charcoal">Welcome back</h1>
          <p className="mt-1 text-sm text-charcoal/60">Log in to check on your plants.</p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4 rounded-2xl border border-forest/10 bg-white p-6 shadow-sm">
          {error && (
            <div className="rounded-xl bg-rust/10 px-4 py-3 text-sm text-rust">{error}</div>
          )}

          <div>
            <label htmlFor="email" className="mb-1 block text-sm font-medium text-charcoal/80">
              Email
            </label>
            <input
              id="email"
              type="email"
              required
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full rounded-xl border border-forest/20 px-4 py-2.5 text-sm outline-none focus:border-forest"
              placeholder="you@example.com"
            />
          </div>

          <div>
            <label htmlFor="password" className="mb-1 block text-sm font-medium text-charcoal/80">
              Password
            </label>
            <input
              id="password"
              type="password"
              required
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full rounded-xl border border-forest/20 px-4 py-2.5 text-sm outline-none focus:border-forest"
              placeholder="••••••••"
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full rounded-xl bg-forest px-4 py-2.5 text-sm font-medium text-white transition hover:bg-forest-dark disabled:opacity-60"
          >
            {loading ? "Logging in…" : "Log in"}
          </button>
        </form>

        <p className="mt-6 text-center text-sm text-charcoal/60">
          Don't have an account?{" "}
          <Link to="/signup" className="font-medium text-forest">
            Sign up
          </Link>
        </p>
      </div>
    </div>
  );
}
