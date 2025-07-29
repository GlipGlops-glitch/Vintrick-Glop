// src/context/SettingsContext.js
import React, { createContext, useContext, useEffect, useState } from "react";
import { ALL_FIELDS } from "../components/HarvestLoadFormBody"; // Or wherever ALL_FIELDS is defined

const SettingsContext = createContext();

function buildDefaultFields() {
  const defaults = {};
  ALL_FIELDS.forEach((f) => {
    defaults[f.key] = true;
  });
  return defaults;
}

const defaultSettings = {
  harvestLoadForm: {
    fields: buildDefaultFields(),
    order: ALL_FIELDS.map((f) => f.key),
  },
  // ... add other settings groups here if needed
};

function mergeFields(saved, master) {
  // Ensure ALL_FIELDS keys are present in saved, keeping old values if possible
  const merged = {};
  master.forEach((f) => {
    merged[f.key] = saved && f.key in saved ? saved[f.key] : true;
  });
  return merged;
}

function mergeOrder(savedOrder) {
  // Ensure order has all keys, in proper sequence
  const keysInOrder = savedOrder ? [...savedOrder] : [];
  ALL_FIELDS.forEach((f) => {
    if (!keysInOrder.includes(f.key)) keysInOrder.push(f.key);
  });
  // Optionally, remove keys that no longer exist
  return keysInOrder.filter((key) => ALL_FIELDS.some((f) => f.key === key));
}

export function SettingsProvider({ children }) {
  const [settings, setSettingsRaw] = useState(() => {
    const stored = localStorage.getItem("vintrick_settings");
    let parsed = stored ? JSON.parse(stored) : {};
    // Merge defaults/fields/order:
    parsed.harvestLoadForm = parsed.harvestLoadForm || {};
    parsed.harvestLoadForm.fields = mergeFields(
      parsed.harvestLoadForm.fields,
      ALL_FIELDS,
    );
    parsed.harvestLoadForm.order = mergeOrder(parsed.harvestLoadForm.order);
    return { ...defaultSettings, ...parsed };
  });

  // On mount, patch settings if new fields added since last run
  useEffect(() => {
    setSettingsRaw((current) => {
      const patched = { ...current };
      patched.harvestLoadForm = patched.harvestLoadForm || {};
      patched.harvestLoadForm.fields = mergeFields(
        patched.harvestLoadForm.fields,
        ALL_FIELDS,
      );
      patched.harvestLoadForm.order = mergeOrder(patched.harvestLoadForm.order);
      return patched;
    });
    // eslint-disable-next-line
  }, []);

  // Always persist to localStorage on change
  useEffect(() => {
    localStorage.setItem("vintrick_settings", JSON.stringify(settings));
  }, [settings]);

  // Use this to update settings
  const setSettings = (updater) => {
    setSettingsRaw((prev) => {
      const next = typeof updater === "function" ? updater(prev) : updater;
      // Always patch before saving!
      next.harvestLoadForm = next.harvestLoadForm || {};
      next.harvestLoadForm.fields = mergeFields(
        next.harvestLoadForm.fields,
        ALL_FIELDS,
      );
      next.harvestLoadForm.order = mergeOrder(next.harvestLoadForm.order);
      return next;
    });
  };

  // (Optional) Add a reset-to-defaults method
  function resetSettings() {
    setSettingsRaw({ ...defaultSettings });
  }

  return (
    <SettingsContext.Provider value={{ settings, setSettings, resetSettings }}>
      {children}
    </SettingsContext.Provider>
  );
}

export function useSettings() {
  return useContext(SettingsContext);
}
