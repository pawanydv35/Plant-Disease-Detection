import React from "react";
import { Link } from "react-router-dom";
import { Sprout } from "lucide-react";

export default function NotFound() {
  return (
    <div className="flex min-h-[70vh] flex-col items-center justify-center px-6 text-center">
      <Sprout className="text-forest/40" size={48} />
      <h1 className="mt-4 font-display text-3xl text-charcoal">This leaf hasn't grown here</h1>
      <p className="mt-2 text-charcoal/60">The page you're looking for doesn't exist.</p>
      <Link to="/" className="mt-6 rounded-xl bg-forest px-6 py-2.5 text-sm font-medium text-white hover:bg-forest-dark">
        Back to home
      </Link>
    </div>
  );
}
