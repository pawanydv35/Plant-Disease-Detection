import React, { useEffect, useState } from "react";
import { Search, Trash2 } from "lucide-react";
import { toast } from "sonner";
import api from "../lib/axios";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export default function History() {
  const [predictions, setPredictions] = useState([]);
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api
      .get("/history")
      .then(({ data }) => setPredictions(data))
      .catch(() => setPredictions([]))
      .finally(() => setLoading(false));
  }, []);

  async function handleDelete(id) {
    try {
      await api.delete(`/history/${id}`);
      setPredictions((prev) => prev.filter((p) => p.id !== id));
    } catch {
      toast.error("Couldn't delete that prediction.");
    }
  }

  const filtered = predictions.filter((p) =>
    p.disease_name?.toLowerCase().includes(query.toLowerCase())
  );

  return (
    <div className="mx-auto max-w-4xl px-6 py-16">
      <h1 className="font-display text-3xl text-charcoal">Prediction history</h1>

      <div className="mt-6 flex items-center gap-2 rounded-xl border border-forest/20 bg-white px-4 py-2.5">
        <Search size={16} className="text-charcoal/40" />
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search by disease name…"
          className="w-full text-sm outline-none"
        />
      </div>

      <div className="mt-6 space-y-3">
        {loading && <p className="text-sm text-charcoal/50">Loading history…</p>}

        {!loading && filtered.length === 0 && (
          <div className="rounded-2xl border border-dashed border-forest/20 bg-surface p-10 text-center text-sm text-charcoal/50">
            No predictions yet — upload a leaf image from your dashboard to get started.
          </div>
        )}

        {filtered.map((p) => (
          <div key={p.id} className="flex items-center justify-between rounded-2xl border border-forest/10 bg-white p-4 shadow-sm">
            <div className="flex items-center gap-4">
              <img src={`${API_BASE_URL}${p.image_url}`} alt={p.disease_name} className="h-14 w-14 rounded-lg object-cover" />
              <div>
                <p className="font-medium text-charcoal">{p.disease_name}</p>
                <p className="text-xs text-charcoal/50">
                  {new Date(p.created_at).toLocaleDateString()}
                </p>
              </div>
            </div>
            <div className="flex items-center gap-3">
              <span className="rounded-full bg-surface px-3 py-1 font-mono text-xs text-forest">
                {Math.round(p.confidence * 100)}%
              </span>
              <button
                onClick={() => handleDelete(p.id)}
                aria-label="Delete prediction"
                className="text-charcoal/30 transition hover:text-rust"
              >
                <Trash2 size={16} />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
