import React, { useEffect, useState } from "react";
import { useAuth } from "../context/AuthContext.jsx";
import api from "../lib/axios";

export default function Profile() {
  const { user, logout } = useAuth();
  const [profile, setProfile] = useState(user);

  useEffect(() => {
    api
      .get("/profile")
      .then(({ data }) => setProfile(data))
      .catch(() => {});
  }, []);

  if (!profile) return null;

  return (
    <div className="mx-auto max-w-2xl px-6 py-16">
      <h1 className="font-display text-3xl text-charcoal">Your profile</h1>

      <div className="mt-8 rounded-2xl border border-forest/10 bg-white p-6 shadow-sm">
        <dl className="divide-y divide-forest/10">
          <Row label="Name" value={profile.name} />
          <Row label="Email" value={profile.email} />
          <Row
            label="Member since"
            value={new Date(profile.created_at).toLocaleDateString()}
          />
        </dl>
      </div>

      <div className="mt-6 flex gap-3">
        <button className="rounded-xl border border-forest/30 px-5 py-2.5 text-sm font-medium text-forest hover:bg-surface">
          Edit profile
        </button>
        <button className="rounded-xl border border-forest/30 px-5 py-2.5 text-sm font-medium text-forest hover:bg-surface">
          Change password
        </button>
        <button
          onClick={logout}
          className="rounded-xl border border-rust/30 px-5 py-2.5 text-sm font-medium text-rust hover:bg-rust/5"
        >
          Log out
        </button>
      </div>
      <p className="mt-3 text-xs text-charcoal/40">
        Edit profile and change password are wired up in a later step.
      </p>
    </div>
  );
}

function Row({ label, value }) {
  return (
    <div className="flex items-center justify-between py-3">
      <dt className="text-sm text-charcoal/50">{label}</dt>
      <dd className="text-sm font-medium text-charcoal">{value}</dd>
    </div>
  );
}
