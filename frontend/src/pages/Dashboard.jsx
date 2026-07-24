import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "sonner";
import { UploadCloud, Loader2 } from "lucide-react";
import api from "../lib/axios";

export default function Dashboard() {
  const navigate = useNavigate();
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [predicting, setPredicting] = useState(false);

  function handleFileChange(e) {
    const selected = e.target.files?.[0];
    if (!selected) return;
    setFile(selected);
    setPreview(URL.createObjectURL(selected));
  }

  async function handlePredict() {
    if (!file) return;
    setPredicting(true);
    try {
      const formData = new FormData();
      formData.append("file", file);

      // NOTE: /predict is implemented in the model-integration step.
      const { data } = await api.post("/predict", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      navigate("/prediction", { state: { result: data, previewUrl: preview } });
    } catch (err) {
      const message = err.response?.data?.detail || "Prediction failed. Please try again.";
      toast.error(message);
    } finally {
      setPredicting(false);
    }
  }

  return (
    <div className="mx-auto max-w-3xl px-6 py-16">
      <h1 className="font-display text-3xl text-charcoal">Diagnose a leaf</h1>
      <p className="mt-2 text-charcoal/60">
        Upload a clear photo of the affected leaf in natural light, with the leaf filling most of the image.
      </p>

      <div className="mt-8 rounded-2xl border-2 border-dashed border-forest/30 bg-surface p-10 text-center">
        {preview ? (
          <div className="relative mx-auto w-64 overflow-hidden rounded-xl shadow-sm">
            <img src={preview} alt="Selected leaf preview" className="w-full object-cover" />
            {predicting && <div className="absolute inset-x-0 top-0 h-1 animate-scan bg-moss/80" />}
          </div>
        ) : (
          <label htmlFor="file-upload" className="flex cursor-pointer flex-col items-center gap-3">
            <UploadCloud className="text-forest" size={36} strokeWidth={1.5} />
            <span className="font-medium text-forest">Click to upload an image</span>
            <span className="text-xs text-charcoal/50">PNG or JPG, up to 10MB</span>
          </label>
        )}
        <input id="file-upload" type="file" accept="image/*" onChange={handleFileChange} className="hidden" />
      </div>

      <div className="mt-6 flex flex-wrap gap-3">
        {preview && (
          <label htmlFor="file-upload" className="cursor-pointer rounded-xl border border-forest/30 px-5 py-2.5 text-sm font-medium text-forest hover:bg-surface">
            Choose a different image
          </label>
        )}
        <button
          onClick={handlePredict}
          disabled={!file || predicting}
          className="flex items-center gap-2 rounded-xl bg-forest px-6 py-2.5 text-sm font-medium text-white transition hover:bg-forest-dark disabled:opacity-50"
        >
          {predicting && <Loader2 className="animate-spin" size={16} />}
          {predicting ? "Analyzing…" : "Predict"}
        </button>
      </div>
    </div>
  );
}
