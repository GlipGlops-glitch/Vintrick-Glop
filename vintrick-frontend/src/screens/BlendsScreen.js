// src/screens/BlendsScreen.js

import "../styles/AppShared.css";
import React, { useState, useEffect } from "react";
import ModernHeaderBar from "../components/ModernHeaderBar"; // <-- Use ModernHeaderBar instead of HeaderBar
import AddEditBlendForm from "../components/AddEditBlendForm";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

// The backend returns a flat array: [ {...}, {...}, ... ]
const fetchBlends = async (authFetch) => {
  const response = await authFetch(`/api/blends`);
  if (!response.ok) throw new Error("Failed to fetch blends");
  const data = await response.json();
  return (data || []).map((item) => ({
    ID: item.ID || "",
    Title: item.Title || "",
    Brand: item.Brand || "",
    Varietal: item.Varietal || "",
    Vintage: item.Vintage || "",
    WineType: item.WineType || "",
  }));
};

export default function BlendsScreen() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const [showForm, setShowForm] = useState(false);
  const [formMode, setFormMode] = useState("add");
  const [selectedBlend, setSelectedBlend] = useState(null);

  const navigate = useNavigate();
  const { authFetch } = useAuth();

  // Fetch blends on mount
  useEffect(() => {
    setLoading(true);
    setError(null);
    fetchBlends(authFetch)
      .then(setData)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, [authFetch]);

  function handleAddNew() {
    setFormMode("add");
    setSelectedBlend(null);
    setShowForm(true);
  }

  function handleOpenEdit(record) {
    setFormMode("edit");
    setSelectedBlend(record);
    setShowForm(true);
  }

  async function handleFormSubmit(formValues) {
    setLoading(true);
    try {
      let res;
      // Build payload
      const payload = {
        // ID is only included for edit
        Title: formValues.Title || "",
        Brand: formValues.Brand || "",
        Varietal: formValues.Varietal || "",
        Vintage: formValues.Vintage || "",
        WineType: formValues.WineType || "",
      };

      if (formMode === "add") {
        res = await authFetch("/api/blends/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload),
        });
      } else {
        const id = formValues.ID;
        if (!id) throw new Error("Missing ID for edit operation");
        res = await authFetch(`/api/blends/${id}`, {
          method: "PATCH",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload),
        });
      }

      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.error || "Save failed");
      }

      setShowForm(false);
      setError(null);
      // Reload blends after add/edit
      const items = await fetchBlends(authFetch);
      setData(items);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app-root">
      <ModernHeaderBar /> {/* Use ModernHeaderBar at the top */}
      <div className="card blends-card">
        <div className="blends-table-scroll" style={{ maxHeight: 600, overflow: "auto" }}>
          <table className="blends-table">
            <thead>
              <tr>
                {["Title", "Brand", "Varietal", "Vintage", "WineType"].map((col) => (
                  <th key={col}>{col}</th>
                ))}
                <th></th>
              </tr>
            </thead>
            <tbody>
              {loading ? (
                <tr>
                  <td colSpan={6} style={{ textAlign: "center", padding: 24 }}>
                    Loading...
                  </td>
                </tr>
              ) : data.length === 0 ? (
                <tr>
                  <td colSpan={6} style={{ textAlign: "center", padding: 24 }}>
                    No records found.
                  </td>
                </tr>
              ) : (
                data.map((rec) => (
                  <tr key={rec.ID || rec.Title}>
                    <td>{rec.Title}</td>
                    <td>{rec.Brand}</td>
                    <td>{rec.Varietal}</td>
                    <td>{rec.Vintage}</td>
                    <td>{rec.WineType}</td>
                    <td>
                      <button
                        className="nav-btn nav-btn-light"
                        style={{ padding: "5px 14px", fontSize: 15 }}
                        onClick={() => handleOpenEdit(rec)}
                      >
                        Edit
                      </button>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
        {error && (
          <div style={{ color: "red", padding: 10, textAlign: "center" }}>
            {error}
          </div>
        )}
      </div>
      <AddEditBlendForm
        show={showForm}
        onClose={() => setShowForm(false)}
        onSubmit={handleFormSubmit}
        initialData={formMode === "edit" ? selectedBlend : undefined}
        mode={formMode}
      />
    </div>
  );
}