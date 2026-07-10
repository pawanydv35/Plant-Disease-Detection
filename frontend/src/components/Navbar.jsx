import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { Leaf, Menu, X } from "lucide-react";
import { useAuth } from "../context/AuthContext.jsx";

export default function Navbar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [open, setOpen] = React.useState(false);

  function handleLogout() {
    logout();
    navigate("/");
  }

  const links = user
    ? [
        { to: "/dashboard", label: "Dashboard" },
        { to: "/history", label: "History" },
        { to: "/profile", label: "Profile" },
      ]
    : [];

  return (
    <header className="sticky top-0 z-50 border-b border-forest/10 bg-background/90 backdrop-blur">
      <nav className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
        <Link to="/" className="flex items-center gap-2 font-display text-xl font-medium text-forest">
          <Leaf size={22} strokeWidth={2.5} />
          Leaflet
        </Link>

        <div className="hidden items-center gap-8 md:flex">
          {links.map((l) => (
            <Link
              key={l.to}
              to={l.to}
              className="text-sm font-medium text-charcoal/80 transition hover:text-forest"
            >
              {l.label}
            </Link>
          ))}

          {user ? (
            <button
              onClick={handleLogout}
              className="rounded-xl border border-forest px-4 py-2 text-sm font-medium text-forest transition hover:bg-forest hover:text-white"
            >
              Log out
            </button>
          ) : (
            <div className="flex items-center gap-3">
              <Link to="/login" className="text-sm font-medium text-charcoal/80 hover:text-forest">
                Log in
              </Link>
              <Link
                to="/signup"
                className="rounded-xl bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
              >
                Get started
              </Link>
            </div>
          )}
        </div>

        <button className="md:hidden" onClick={() => setOpen(!open)} aria-label="Toggle menu">
          {open ? <X size={24} /> : <Menu size={24} />}
        </button>
      </nav>

      {open && (
        <div className="flex flex-col gap-1 border-t border-forest/10 px-6 py-4 md:hidden">
          {links.map((l) => (
            <Link key={l.to} to={l.to} className="py-2 text-sm font-medium" onClick={() => setOpen(false)}>
              {l.label}
            </Link>
          ))}
          {user ? (
            <button onClick={handleLogout} className="py-2 text-left text-sm font-medium text-rust">
              Log out
            </button>
          ) : (
            <>
              <Link to="/login" className="py-2 text-sm font-medium" onClick={() => setOpen(false)}>
                Log in
              </Link>
              <Link to="/signup" className="py-2 text-sm font-medium text-forest" onClick={() => setOpen(false)}>
                Get started
              </Link>
            </>
          )}
        </div>
      )}
    </header>
  );
}
