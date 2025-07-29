// BlendsScreen.js

import "./BlendsScreen.css";
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext"; // Import useAuth

export default function BlendsScreen() {
  const [blends, setBlends] = useState([]);
  const [search, setSearch] = useState("");
  const [sortCol, setSortCol] = useState("name");
  const [sortDir, setSortDir] = useState("asc");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const { authFetch } = useAuth(); // Get authFetch

  useEffect(() => {
    setLoading(true);
    authFetch("/api/blends")
      .then((res) => res.json())
      .then((data) => {
        setBlends(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, [authFetch]);

  const filtered = blends
    .filter((b) => {
      const t = `${b.name} ${b.bulk} ${b.fg} ${b.date_created}`.toLowerCase();
      return t.includes(search.toLowerCase());
    })
    .sort((a, b) => {
      let v1 = a[sortCol],
        v2 = b[sortCol];
      if (sortCol === "fg") {
        v1 = parseFloat(v1);
        v2 = parseFloat(v2);
      }
      if (v1 < v2) return sortDir === "asc" ? -1 : 1;
      if (v1 > v2) return sortDir === "asc" ? 1 : -1;
      return 0;
    });

  function handleSort(col) {
    if (sortCol === col) setSortDir(sortDir === "asc" ? "desc" : "asc");
    else {
      setSortCol(col);
      setSortDir("asc");
    }
  }

  function handleRowDoubleClick(blend) {
    navigate(`/blends/${blend.id}`);
  }

  function handleAdd() {
    navigate("/blends/new");
  }

  function handleBack() {
    navigate("/");
  }

  return (
    <div className="blendsscreen-root">
      <div className="header-bar">
        <button className="header-back-btn" onClick={handleBack}>
          ← Back
        </button>
        <h2 className="header-title">Blends</h2>
        <button className="nav-btn" onClick={handleAdd}>
          + Add Blend
        </button>
      </div>

      <div className="card blends-card">
        <div className="blendsscreen-searchbar">
          <input
            className="blendsscreen-search"
            placeholder="Search..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
          <button className="nav-btn" onClick={() => setSearch("")}>
            Clear
          </button>
        </div>

        <div className="blends-table-scroll">
          <table className="blendsscreen-table">
            <thead>
              <tr>
                <th onClick={() => handleSort("name")}>
                  Name {sortCol === "name" && (sortDir === "asc" ? "▲" : "▼")}
                </th>
                <th onClick={() => handleSort("bulk")}>
                  Bulk {sortCol === "bulk" && (sortDir === "asc" ? "▲" : "▼")}
                </th>
                <th onClick={() => handleSort("fg")}>
                  FG {sortCol === "fg" && (sortDir === "asc" ? "▲" : "▼")}
                </th>
                <th onClick={() => handleSort("date_created")}>
                  Date Created{" "}
                  {sortCol === "date_created" &&
                    (sortDir === "asc" ? "▲" : "▼")}
                </th>
              </tr>
            </thead>
            <tbody>
              {filtered.map((blend) => (
                <tr
                  key={blend.id}
                  onDoubleClick={() => handleRowDoubleClick(blend)}
                  className="blendsscreen-row"
                >
                  <td>{blend.name}</td>
                  <td>{blend.bulk}</td>
                  <td>{blend.fg}</td>
                  <td>
                    {blend.date_created &&
                      new Date(blend.date_created).toLocaleDateString()}
                  </td>
                </tr>
              ))}
              {filtered.length === 0 && (
                <tr>
                  <td colSpan={4} style={{ textAlign: "center" }}>
                    No blends found.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
        {loading && <div className="blendsscreen-loading">Loading...</div>}
      </div>
    </div>
  );
}
