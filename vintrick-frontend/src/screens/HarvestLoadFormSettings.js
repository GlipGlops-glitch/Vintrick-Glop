import React from "react";
import HeaderBar from "../components/HeaderBar";
import { useNavigate } from "react-router-dom";
import { useSettings } from "../context/SettingsContext";

const ALL_FIELDS = [
  { key: "uid", label: "UID" },
  { key: "Date_Received", label: "Date Received" },
  { key: "WO", label: "Work Order (WO)" },
  { key: "Block", label: "Block" },
  { key: "Vintrace_ST", label: "Vintrace ST" },
  { key: "Tons", label: "Tons" },
  { key: "Crush_Pad", label: "Crush Pad" },
  // Add more as needed
];

export default function HarvestLoadFormSettings() {
  const { settings, setSettings } = useSettings();
  const navigate = useNavigate();

  function toggleField(key) {
    setSettings((prev) => ({
      ...prev,
      harvestLoadForm: {
        ...prev.harvestLoadForm,
        fields: {
          ...prev.harvestLoadForm.fields,
          [key]: !prev.harvestLoadForm.fields[key],
        },
      },
    }));
  }

  return (
    <div className="settings-root">
      <HeaderBar
        title="Harvest Loads Form Fields"
        onBack={() => navigate("/settings")}
      />
      <div
        className="card settings-card"
        style={{ maxWidth: 480, margin: "40px auto", padding: 28 }}
      >
        <h4 style={{ marginBottom: 24, fontWeight: 600, fontSize: 20 }}>
          Visible Fields
        </h4>
        <ul style={{ listStyle: "none", padding: 0 }}>
          {ALL_FIELDS.map((field) => (
            <li
              key={field.key}
              style={{
                margin: "18px 0",
                display: "flex",
                alignItems: "center",
              }}
            >
              <input
                type="checkbox"
                checked={settings.harvestLoadForm.fields[field.key]}
                onChange={() => toggleField(field.key)}
                id={`field-${field.key}`}
                style={{
                  width: 20,
                  height: 20,
                  accentColor: "var(--primary, #636fa4)",
                  marginRight: 12,
                }}
              />
              <label
                htmlFor={`field-${field.key}`}
                style={{
                  fontSize: 17,
                  fontWeight: 500,
                  letterSpacing: 0.2,
                }}
              >
                {field.label}
              </label>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
