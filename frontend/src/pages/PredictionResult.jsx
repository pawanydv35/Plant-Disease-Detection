import React from "react";
import { useLocation, Link } from "react-router-dom";

export default function PredictionResult() {
  const { state } = useLocation();
  const result = state?.result;
  const previewUrl = state?.previewUrl;

  if (!result) {
    return (
      <div className="mx-auto max-w-2xl px-6 py-24 text-center">
        <p className="text-charcoal/60">
          No prediction to show. Upload an image from your dashboard first.
        </p>
        <Link to="/dashboard" className="mt-4 inline-block font-medium text-forest">
          Go to dashboard
        </Link>
      </div>
    );
  }

  const confidencePct = Math.round(result.confidence * 100);

  return (
    <div className="mx-auto max-w-3xl px-6 py-16">
      <div className="grid gap-8 md:grid-cols-[240px_1fr]">
        <div>
          {previewUrl && (
            <img src={previewUrl} alt="Uploaded leaf" className="w-full rounded-2xl object-cover shadow-sm" />
          )}
          <p className="mt-3 text-center text-xs text-charcoal/40">
            {new Date().toLocaleString()}
          </p>
        </div>

        <div>
          <span className="text-xs font-medium uppercase tracking-wide text-charcoal/40">Diagnosis</span>
          <h1 className="font-display text-3xl text-charcoal">{result.disease_name}</h1>

          <div className="mt-3 flex items-center gap-2">
            <div className="h-2 w-40 overflow-hidden rounded-full bg-surface">
              <div className="h-full bg-forest" style={{ width: `${confidencePct}%` }} />
            </div>
            <span className="font-mono text-sm text-forest">{confidencePct}%</span>
          </div>

          {result.top_predictions?.length > 0 && (
            <div className="mt-6">
              <h2 className="text-sm font-medium text-charcoal/70">Other possibilities</h2>
              <ul className="mt-2 space-y-1">
                {result.top_predictions.map((p) => (
                  <li key={p.label} className="flex justify-between text-sm text-charcoal/60">
                    <span>{p.label}</span>
                    <span className="font-mono">{Math.round(p.confidence * 100)}%</span>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      </div>

      {/* Disease info sections are populated once the disease knowledge
          base is wired up in the model-integration step. */}
      <div className="mt-10 grid gap-6 md:grid-cols-2">
        <InfoCard title="Causes" body={result.causes} />
        <InfoCard title="Symptoms" body={result.symptoms} />
        <InfoCard title="Treatment" body={result.treatment} />
        <InfoCard title="Prevention" body={result.prevention} />
      </div>
    </div>
  );
}

function InfoCard({ title, body }) {
  return (
    <div className="rounded-2xl border border-forest/10 bg-white p-5 shadow-sm">
      <h3 className="font-display text-lg text-charcoal">{title}</h3>
      <p className="mt-2 text-sm text-charcoal/60">
        {body || "Not available yet."}
      </p>
    </div>
  );
}
