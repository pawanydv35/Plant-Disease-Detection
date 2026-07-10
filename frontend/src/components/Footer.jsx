import React from "react";
import { Leaf } from "lucide-react";

export default function Footer() {
  return (
    <footer className="border-t border-forest/10 bg-surface">
      <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-4 px-6 py-10 md:flex-row">
        <div className="flex items-center gap-2 font-display text-lg text-forest">
          <Leaf size={18} />
          Leaflet
        </div>
        <p className="text-sm text-charcoal/60">
          Built for growers who'd rather catch disease on day one than day thirty.
        </p>
        <p className="text-xs text-charcoal/40">© {new Date().getFullYear()} Leaflet. All rights reserved.</p>
      </div>
    </footer>
  );
}
