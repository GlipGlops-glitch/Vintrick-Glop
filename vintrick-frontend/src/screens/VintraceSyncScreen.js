// src/screens/VintraceSyncScreen.js

import "../styles/AppShared.css";
import React, { useState } from "react";
import ModernHeaderBar from "../components/ModernHeaderBar";
import { useAuth } from "../context/AuthContext";

export default function VintraceSyncScreen() {
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const { authFetch } = useAuth();

  async function handleSyncSubmit(e) {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      // POST to the backend endpoint for vintrace sync
      const res = await authFetch(
        `/api/vintrace_api/fetch_and_update?start_date=${encodeURIComponent(startDate)}&end_date=${encodeURIComponent(endDate)}`,
        { method: "POST" }
      );
      if (!res.ok) {
        let msg = "Sync failed";
        try {
          const data = await res.json();
          msg = data.detail || data.error || msg;
        } catch {
          // ignore
        }
        throw new Error(msg);
      }
      const data = await res.json();
      setResult(data);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app-root">
      <ModernHeaderBar />
      <div className="card blends-card">
        <h2 style={{ textAlign: "center", marginTop: 0 }}>Sync Vintrace Harvest Loads</h2>
        <form className="vintrace-sync-form" onSubmit={handleSyncSubmit} style={{ display: "flex", justifyContent: "center", gap: 16, marginBottom: 20 }}>
          <label>
            Start Date:{" "}
            <input
              type="date"
              value={startDate}
              onChange={e => setStartDate(e.target.value)}
              required
              className="input"
              style={{ minWidth: 140 }}
            />
          </label>
          <label>
            End Date:{" "}
            <input
              type="date"
              value={endDate}
              onChange={e => setEndDate(e.target.value)}
              required
              className="input"
              style={{ minWidth: 140 }}
            />
          </label>
          <button
            className="nav-btn"
            type="submit"
            style={{ padding: "5px 24px", fontSize: 16 }}
            disabled={loading || !startDate || !endDate}
          >
            {loading ? "Syncing..." : "Sync"}
          </button>
        </form>
        {result && (
          <div style={{ color: "green", textAlign: "center", margin: 10 }}>
            <b>Sync started:</b>
            <pre style={{ background: "#e9ffe9", padding: "10px", borderRadius: "6px", marginTop: 8, fontSize: 15 }}>
              {JSON.stringify(result, null, 2)}
            </pre>
          </div>
        )}
        {error && (
          <div style={{ color: "red", textAlign: "center", margin: 10 }}>
            {error}
          </div>
        )}
      </div>
    </div>
  );
}