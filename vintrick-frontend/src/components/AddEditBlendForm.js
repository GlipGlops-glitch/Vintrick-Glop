// src/components/AddEditBlendForm.js

import React, { useState, useEffect } from "react";
import styles from "../screens/BlendsScreen.module.css";

const FIELDS = [
  "Title", "Brand", "Varietal", "Vintage", "WineType", "Alc", "Active",
  "ExpectedBottleDate", "SpecSheet"
];

export default function AddEditBlendForm({
  show,
  onClose,
  onSubmit,
  initialData = {},
  mode = "add"
}) {
  // FIX: always handle initialData as possibly null/undefined
  const [formData, setFormData] = useState(() => {
    const safeInit = initialData || {};
    return FIELDS.reduce(
      (acc, field) => ({ ...acc, [field]: safeInit[field] || "" }),
      { ID: safeInit.ID || undefined }
    );
  });

  useEffect(() => {
    const safeInit = initialData || {};
    setFormData(
      FIELDS.reduce(
        (acc, field) => ({ ...acc, [field]: safeInit[field] || "" }),
        { ID: safeInit.ID || undefined }
      )
    );
  }, [initialData, show]);

  function handleChange(e) {
    const { name, value, type, checked } = e.target;
    setFormData({ ...formData, [name]: type === "checkbox" ? checked : value });
  }

  function handleSubmit(e) {
    e.preventDefault();
    onSubmit(formData);
  }

  if (!show) return null;

  return (
    <div className={styles["datascreen-modal-backdrop"]}>
      <form className={styles["datascreen-modal-card"]} onSubmit={handleSubmit}>
        <h2>{mode === "edit" ? "Edit Blend" : "Add Blend"}</h2>
        {FIELDS.map((field) =>
          field === "Active" ? (
            <div key={field} style={{ marginBottom: 14 }}>
              <label>{field}:</label>
              <input
                type="checkbox"
                name={field}
                checked={!!formData[field]}
                onChange={handleChange}
              />
            </div>
          ) : (
            <div key={field} style={{ marginBottom: 14 }}>
              <label>{field}:</label>
              <input
                name={field}
                value={formData[field]}
                onChange={handleChange}
              />
            </div>
          )
        )}
        <div style={{ marginTop: 12 }}>
          <button type="submit" className="nav-btn nav-btn-light">Save</button>
          <button type="button" className="nav-btn nav-btn-light" onClick={onClose}>Cancel</button>
        </div>
      </form>
    </div>
  );
}