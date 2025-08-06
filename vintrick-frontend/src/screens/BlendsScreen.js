// src/screens/BlendsScreen.js

import styles from "./BlendsScreen.module.css";
import React, { useState, useEffect } from "react";
import HeaderBar from "../components/HeaderBar";
import AddEditBlendForm from "../components/AddEditBlendForm";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

export default function BlendsScreen() {
  const [blends, setBlends] = useState([]);
  const [search, setSearch] = useState("");
  const [sortCol, setSortCol] = useState("Title");
  const [sortDir, setSortDir] = useState("asc");
  const [loading, setLoading] = useState(false);
  const [showForm, setShowForm] = useState(false);
  const [formMode, setFormMode] = useState("add");
  const [selectedBlend, setSelectedBlend] = useState(null);

  const { authFetch } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    setLoading(true);
    authFetch("/api/blends/")
      .then((res) => res.json())
      .then((data) => {
        setBlends(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, [authFetch]);

  function handleSort(col) {
    if (sortCol === col) setSortDir(sortDir === "asc" ? "desc" : "asc");
    else {
      setSortCol(col);
      setSortDir("asc");
    }
  }

  function handleEdit(blend) {
    setFormMode("edit");
    setSelectedBlend(blend);
    setShowForm(true);
  }

  function handleFormSubmit(formValues) {
    setLoading(true);
    let method = formMode === "edit" ? "PATCH" : "POST";
    // Always use ID for PATCH!
    let url = formMode === "edit"
      ? `/api/blends/${formValues.ID}`
      : "/api/blends/";
    authFetch(url, {
      method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formValues),
    })
      .then((res) => {
        if (!res.ok) throw new Error("Failed to save blend");
        return res.json();
      })
      .then(() => {
        setShowForm(false);
        setSelectedBlend(null);
        return authFetch("/api/blends/").then((res) => res.json());
      })
      .then((data) => setBlends(data))
      .finally(() => setLoading(false));
  }

  function handleAdd() {
    setFormMode("add");
    setSelectedBlend(null);
    setShowForm(true);
  }

  const safeBlends = Array.isArray(blends) ? blends : [];
  const filtered = safeBlends
    .filter((b) => {
      const t = `${b.Title} ${b.Brand} ${b.Varietal} ${b.Vintage} ${b.WineType}`.toLowerCase();
      return t.includes(search.toLowerCase());
    })
    .sort((a, b) => {
      let v1 = a[sortCol] || "";
      let v2 = b[sortCol] || "";
      if (v1 < v2) return sortDir === "asc" ? -1 : 1;
      if (v1 > v2) return sortDir === "asc" ? 1 : -1;
      return 0;
    });

  return (
    <div className={styles["datascreen-root"]}>
      <HeaderBar
        title="Blends"
        onBack={() => navigate(-1)}
        onAdd={handleAdd}
        addLabel="+ Add Blend"
      />
      <div className={`card ${styles["datascreen-card"]}`}>
        <div className={styles["datascreen-btn-group"]}>
          <input
            className={styles["datascreen-search"]}
            placeholder="Search..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
          <button className="nav-btn nav-btn-light" onClick={() => setSearch("")}>
            Clear
          </button>
        </div>
        <div className={styles["datascreen-table-scroll"]}>
          <table className="harvestloads-table">
            <thead>
              <tr>
                <th onClick={() => handleSort("Title")}>
                  Name {sortCol === "Title" && (sortDir === "asc" ? "▲" : "▼")}
                </th>
                <th onClick={() => handleSort("Brand")}>
                  Brand {sortCol === "Brand" && (sortDir === "asc" ? "▲" : "▼")}
                </th>
                <th onClick={() => handleSort("Varietal")}>
                  Varietal {sortCol === "Varietal" && (sortDir === "asc" ? "▲" : "▼")}
                </th>
                <th onClick={() => handleSort("Vintage")}>
                  Vintage {sortCol === "Vintage" && (sortDir === "asc" ? "▲" : "▼")}
                </th>
                <th onClick={() => handleSort("WineType")}>
                  Wine Type {sortCol === "WineType" && (sortDir === "asc" ? "▲" : "▼")}
                </th>
                {/* <th onClick={() => handleSort("Alc")}>
                  Alc {sortCol === "Alc" && (sortDir === "asc" ? "▲" : "▼")}
                </th>
                <th onClick={() => handleSort("Active")}>
                  Active {sortCol === "Active" && (sortDir === "asc" ? "▲" : "▼")}
                </th>
                <th onClick={() => handleSort("ExpectedBottleDate")}>
                  Expected Bottle Date {sortCol === "ExpectedBottleDate" && (sortDir === "asc" ? "▲" : "▼")}
                </th>
                <th onClick={() => handleSort("SpecSheet")}>
                  Spec Sheet {sortCol === "SpecSheet" && (sortDir === "asc" ? "▲" : "▼")}
                </th> */}
                <th></th>
              </tr>
            </thead>
            <tbody>
              {filtered.map((blend) => (
                <tr key={blend.ID}>
                  <td>{blend.Title}</td>
                  <td>{blend.Brand}</td>
                  <td>{blend.Varietal}</td>
                  <td>{blend.Vintage}</td>
                  <td>{blend.WineType}</td>
                  <td>{blend.Alc}</td>
                  <td>{blend.Active ? "Yes" : "No"}</td>
                  <td>{blend.ExpectedBottleDate}</td>
                  <td>{blend.SpecSheet}</td>
                  <td>
                    <button
                      className="nav-btn nav-btn-light"
                      onClick={() => handleEdit(blend)}
                      style={{ padding: "5px 14px", fontSize: 15 }}
                    >
                      Edit
                    </button>
                  </td>
                </tr>
              ))}
              {filtered.length === 0 && (
                <tr>
                  <td colSpan={10} style={{ textAlign: "center" }}>
                    No blends found.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
        {loading && <div className="blendsscreen-loading">Loading...</div>}
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