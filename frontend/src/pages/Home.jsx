import React from "react";
import { Link } from "react-router-dom";
import { ScanLine, ClipboardList, ShieldCheck, Upload } from "lucide-react";

const steps = [
  {
    icon: Upload,
    title: "Upload a photo",
    body: "Snap the affected leaf in natural light — no special equipment needed.",
  },
  {
    icon: ScanLine,
    title: "The model scans it",
    body: "A trained vision model compares the leaf against known disease patterns in seconds.",
  },
  {
    icon: ClipboardList,
    title: "Get a diagnosis",
    body: "See the disease name, confidence score, and the top alternatives it considered.",
  },
  {
    icon: ShieldCheck,
    title: "Act on it",
    body: "Read causes, symptoms, treatment, and prevention tips tailored to the result.",
  },
];

export default function Home() {
  return (
    <div>
      {/* Hero */}
      <section className="relative overflow-hidden px-6 pb-24 pt-20 md:pt-28">
        <div className="mx-auto grid max-w-6xl items-center gap-12 md:grid-cols-2">
          <div>
            <span className="mb-4 inline-block rounded-full bg-surface px-4 py-1 text-xs font-medium uppercase tracking-wide text-forest">
              Leaf-level diagnostics
            </span>
            <h1 className="font-display text-4xl leading-tight text-charcoal md:text-6xl">
              Know what's wrong with your plant{" "}
              <span className="text-forest">before it spreads.</span>
            </h1>
            <p className="mt-6 max-w-md text-lg text-charcoal/70">
              Upload a photo of a leaf and get an instant disease diagnosis,
              confidence score, and treatment plan — powered by a model
              trained on thousands of plant images.
            </p>
            <div className="mt-8 flex flex-wrap gap-4">
              <Link
                to="/signup"
                className="rounded-xl bg-forest px-6 py-3 font-medium text-white shadow-sm transition hover:bg-forest-dark"
              >
                Upload plant image
              </Link>
              <a
                href="#how-it-works"
                className="rounded-xl border border-forest/30 px-6 py-3 font-medium text-forest transition hover:bg-surface"
              >
                See how it works
              </a>
            </div>
          </div>

          {/* Signature element: scanning-line mock preview */}
          <div className="relative mx-auto aspect-square w-full max-w-sm overflow-hidden rounded-2xl bg-surface shadow-xl">
            <div className="absolute inset-0 flex items-center justify-center">
              <svg viewBox="0 0 200 200" className="h-40 w-40 text-forest/30" fill="currentColor">
                <path d="M100 20c-44 0-80 36-80 80 0 33 20 61 49 73-3-14-4-30 1-46 8-27 30-45 55-54 12-4 22-11 30-20-9 45-46 79-92 84 5 1 11 1 17 1 55 0 100-45 100-100 0-6-1-12-2-18-19 0-38-8-52-20-9-8-16 8-16 20z" />
              </svg>
            </div>
            <div className="absolute inset-x-0 top-0 h-1 animate-scan bg-moss/70 shadow-[0_0_20px_4px_rgba(107,155,63,0.5)]" />
            <div className="absolute bottom-4 left-4 right-4 rounded-xl bg-white/90 p-3 backdrop-blur">
              <p className="font-mono text-xs text-charcoal/50">confidence</p>
              <p className="font-mono text-lg font-medium text-forest">94.2%</p>
            </div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="bg-surface px-6 py-20">
        <div className="mx-auto max-w-6xl">
          <h2 className="font-display text-3xl text-charcoal">What you get with every scan</h2>
          <div className="mt-10 grid gap-8 md:grid-cols-3">
            <FeatureCard
              title="Top-3 predictions"
              body="Not just one answer — see the model's next most likely diagnoses and how confident it is in each."
            />
            <FeatureCard
              title="Treatment guidance"
              body="Every result comes with causes, symptoms, treatment steps, and prevention tips."
            />
            <FeatureCard
              title="Full history"
              body="Every scan is saved so you can track how a plant's condition changes over time."
            />
          </div>
        </div>
      </section>

      {/* How it works */}
      <section id="how-it-works" className="px-6 py-20">
        <div className="mx-auto max-w-6xl">
          <h2 className="font-display text-3xl text-charcoal">How it works</h2>
          <div className="mt-10 grid gap-8 md:grid-cols-4">
            {steps.map((s, i) => (
              <div key={s.title} className="relative rounded-2xl border border-forest/10 bg-white p-6">
                <s.icon className="text-forest" size={28} strokeWidth={1.8} />
                <h3 className="mt-4 font-display text-lg text-charcoal">{s.title}</h3>
                <p className="mt-2 text-sm text-charcoal/60">{s.body}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="px-6 pb-24">
        <div className="mx-auto max-w-4xl rounded-2xl bg-forest px-8 py-14 text-center text-white">
          <h2 className="font-display text-3xl">Ready to check your first leaf?</h2>
          <p className="mx-auto mt-3 max-w-md text-white/80">
            Create a free account and get a diagnosis in under a minute.
          </p>
          <Link
            to="/signup"
            className="mt-6 inline-block rounded-xl bg-white px-6 py-3 font-medium text-forest transition hover:bg-white/90"
          >
            Get started free
          </Link>
        </div>
      </section>
    </div>
  );
}

function FeatureCard({ title, body }) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">
      <h3 className="font-display text-lg text-charcoal">{title}</h3>
      <p className="mt-2 text-sm text-charcoal/60">{body}</p>
    </div>
  );
}
