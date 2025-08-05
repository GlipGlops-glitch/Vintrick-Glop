import "./HarvestLoadsScreen.css"; // <-- Use the same CSS!
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import HeaderBar from "../components/HeaderBar";
import { useAuth } from "../context/AuthContext";

export default function BlendsScreen() {
  const [blends, setBlends] = useState([]);
  const [search, setSearch] = useState("");
  const [sortCol, setSortCol] = useState("name");
  const [sortDir, setSortDir] = useState("asc");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const { authFetch } = useAuth();

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

  const safeBlends = Array.isArray(blends) ? blends : [];
  const filtered = safeBlends
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

  return (
    <div className="harvestloads-root">
      <HeaderBar
        title="Blends"
        onBack={() => navigate(-1)}
        onAdd={handleAdd}
        addLabel="+ Add Blend"
      />
      <div className="card harvestloads-card">
        <div className="harvestloads-controls" style={{ display: "flex", gap: 8, alignItems: "center", flexWrap: "wrap" }}>
          <input
            className="harvestloads-search"
            placeholder="Search..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
          <button className="nav-btn nav-btn-light" onClick={() => setSearch("")}>
            Clear
          </button>
        </div>
        <div className="harvestloads-table-scroll">
          <table className="harvestloads-table">
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