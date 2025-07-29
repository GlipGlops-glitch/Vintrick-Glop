// DetailsScreen.js

import "./DetailsScreen.css";
import React, { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { useAuth } from "../context/AuthContext"; // Import useAuth

const FIELDS_TO_SHOW = [
  "Vintrace_ST",
  "Block",
  "Tons",
  "Press",
  "Tank",
  "WO",
  "Date_Received",
  "Crush_Pad",
  "Status",
];

const PRESS_OPTIONS = [
  "CC WP1 (25t)",
  "CC WP2 (25t)",
  "CC WP3 (25t)",
  "CC WP4 (25t)",
  "CC WP5 (10t)",
  "CC WP6 (50t)",
];
const CRUSH_OPTIONS = ["White Crush Pad", "Red Crush Pad", "Reserve Crush Pad"];

export default function DetailsScreen() {
  const navigate = useNavigate();
  const { id } = useParams();
  const { authFetch } = useAuth(); // Get authFetch
  const [record, setRecord] = useState({});
  const [loading, setLoading] = useState(false);
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    if (id) {
      setLoading(true);
      authFetch(`/api/harvestloads/${id}`)
        .then((res) => res.json())
        .then((data) => {
          setRecord(data);
          setLoading(false);
        })
        .catch(() => setLoading(false));
    }
  }, [id, authFetch]);

  const handleChange = (field, value) => {
    setRecord((rec) => ({ ...rec, [field]: value }));
  };

  const handleSave = async () => {
    setSaving(true);
    let tons = parseFloat(record.Tons);
    if (isNaN(tons)) {
      alert("Tons must be numeric.");
      setSaving(false);
      return;
    }
    let body = { ...record, Tons: tons };

    let resp = await authFetch(
      id ? `/api/harvestloads/${id}` : `/api/harvestloads`,
      {
        method: id ? "PUT" : "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      },
    );
    setSaving(false);
    if (resp.ok) {
      navigate("/harvest-loads");
    } else {
      alert("Failed to save. Please try again.");
    }
  };

  const handleCancel = () => navigate("/harvest-loads");

  return (
    <div className="details-root">
      <div className="card details-card">
        <h2 className="details-title">Load Details</h2>
        {loading ? (
          <div className="details-loading">Loading...</div>
        ) : (
          <form className="details-form" onSubmit={(e) => e.preventDefault()}>
            {FIELDS_TO_SHOW.map((field) => (
              <div className="details-field-row" key={field}>
                <label className="details-label">{field}</label>
                {field === "Press" ? (
                  <select
                    className="details-input"
                    value={record.Press || ""}
                    onChange={(e) => handleChange(field, e.target.value)}
                  >
                    <option value="">-- Select Press --</option>
                    {PRESS_OPTIONS.map((opt) => (
                      <option key={opt} value={opt}>
                        {opt}
                      </option>
                    ))}
                  </select>
                ) : field === "Crush_Pad" ? (
                  <select
                    className="details-input"
                    value={record.Crush_Pad || ""}
                    onChange={(e) => handleChange(field, e.target.value)}
                  >
                    <option value="">-- Select Crush Pad --</option>
                    {CRUSH_OPTIONS.map((opt) => (
                      <option key={opt} value={opt}>
                        {opt}
                      </option>
                    ))}
                  </select>
                ) : (
                  <input
                    className="details-input"
                    value={record[field] || ""}
                    onChange={(e) => handleChange(field, e.target.value)}
                    type={field === "Tons" ? "number" : "text"}
                  />
                )}
              </div>
            ))}
            <div className="button-bar-bg details-action-bar">
              <button
                type="button"
                className="nav-btn"
                onClick={handleSave}
                disabled={saving}
              >
                {saving ? "Saving..." : "Save"}
              </button>
              <button
                type="button"
                className="nav-btn nav-btn-light"
                onClick={handleCancel}
                disabled={saving}
              >
                Cancel
              </button>
            </div>
          </form>
        )}
      </div>
    </div>
  );
}
