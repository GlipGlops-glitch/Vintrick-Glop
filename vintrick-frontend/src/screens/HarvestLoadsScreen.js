import "./HarvestLoadsScreen.css";
import React, { useState, useEffect, useCallback } from "react";
import HeaderBar from "../components/HeaderBar";
import AddEditHarvestLoadForm from "../components/AddEditHarvestLoadForm";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import InfiniteScroll from "react-infinite-scroll-component";

const CRUSH_PADS = [
  "All",
  "White Crush Pad",
  "Red Crush Pad",
  "Reserve Crush Pad",
];

// Fetches one page of harvest loads (paginated)
const fetchHarvestLoadsPage = async (authFetch, skip, limit) => {
  const response = await authFetch(`/api/harvestloads?skip=${skip}&limit=${limit}`);
  if (!response.ok) throw new Error("Failed to fetch harvest loads");
  const data = await response.json();
  // Expecting {items: [...], total: N}
  return {
    items: (data.items || []).map((item) => ({
      id: item.uid || "",
      uid: item.uid || "",
      Date_Received: item.Date_Received || "",
      WO: item.WO || "",
      Block: item.Block || "",
      Vintrace_ST: item.Vintrace_ST || "",
      Tons: item.Tons || null,
      Crush_Pad: item.Crush_Pad || "",
      Press: item.Press || "",
      Tank: item.Tank || "",
      AgCode_ST: item.AgCode_ST || "",
      Time_Received: item.Time_Received || "",
      Wine_Type: item.Wine_Type || "",
      Est_Tons_1: item.Est_Tons_1 || null,
      Est_Tons_2: item.Est_Tons_2 || null,
      Est_Tons_3: item.Est_Tons_3 || null,
      Press_Pick_2: item.Press_Pick_2 || "",
      Linked: item.Linked || "",
      Status: item.Status || "",
      last_modified: item.last_modified || "",
      synced: item.synced || false,
      Vintage: item.Vintage || "", // Add this line if your API returns a Vintage/year
    })),
    total: typeof data.total === "number" ? data.total : (data.items?.length || 0),
  };
};

const PAGE_SIZE = 50;

export default function HarvestLoadsScreen() {
  const [data, setData] = useState([]);
  const [skip, setSkip] = useState(0);
  const [total, setTotal] = useState(null);
  const [loading, setLoading] = useState(false);
  const [hasMore, setHasMore] = useState(true);

  const [search, setSearch] = useState("");
  const [crushPad, setCrushPad] = useState("All");
  const [sortCol, setSortCol] = useState("Date_Received");
  const [sortDesc, setSortDesc] = useState(false);
  const [error, setError] = useState(null);

  const [showForm, setShowForm] = useState(false);
  const [formMode, setFormMode] = useState("add");
  const [selectedRecord, setSelectedRecord] = useState(null);

  // NEW FILTERS
  const [vintageFilter, setVintageFilter] = useState("");
  const [dateFilter, setDateFilter] = useState("");

  const navigate = useNavigate();
  const { authFetch } = useAuth();

  // Fetch first page on mount
  useEffect(() => {
    setLoading(true);
    setError(null);
    fetchHarvestLoadsPage(authFetch, 0, PAGE_SIZE)
      .then(({ items, total }) => {
        setData(items);
        setSkip(items.length);
        setTotal(total);
        setHasMore(items.length < total);
      })
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, [authFetch]);

  // Fetch next page for infinite scroll
  const fetchMoreData = useCallback(() => {
    if (loading || !hasMore) return;
    setLoading(true);
    fetchHarvestLoadsPage(authFetch, skip, PAGE_SIZE)
      .then(({ items }) => {
        setData((prev) => [...prev, ...items]);
        setSkip((prev) => prev + items.length);
        setHasMore(data.length + items.length < total);
      })
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
    // eslint-disable-next-line
  }, [authFetch, skip, data.length, total, loading, hasMore]);

  function handleAddNew() {
    setFormMode("add");
    setSelectedRecord(null);
    setShowForm(true);
  }

  function handleOpenEdit(record) {
    setFormMode("edit");
    setSelectedRecord(record);
    setShowForm(true);
  }

  // Reload all pages after adding/editing
  async function handleFormSubmit(formValues) {
    setLoading(true);
    try {
      let res;
      const payload = {
        id: formValues.id || "",
        uid: formValues.uid || "",
        Date_Received: formValues.Date_Received || "",
        WO: formValues.WO || "",
        Block: formValues.Block || "",
        Vintrace_ST: formValues.Vintrace_ST || "",
        Tons: formValues.Tons || null,
        Crush_Pad: formValues.Crush_Pad || "",
        Press: formValues.Press || "",
        Tank: formValues.Tank || "",
        AgCode_ST: formValues.AgCode_ST || "",
        Time_Received: formValues.Time_Received || "",
        Wine_Type: formValues.Wine_Type || "",
        Est_Tons_1: formValues.Est_Tons_1 || null,
        Est_Tons_2: formValues.Est_Tons_2 || null,
        Est_Tons_3: formValues.Est_Tons_3 || null,
        Press_Pick_2: formValues.Press_Pick_2 || "",
        Linked: formValues.Linked || "",
        Status: formValues.Status || "",
        last_modified: formValues.last_modified || "",
        synced: formValues.synced || false,
        Vintage: formValues.Vintage || "", // If using Vintage in your forms too
      };

      if (formMode === "add") {
        res = await authFetch("/api/harvestloads/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload),
        });
      } else {
        const uid = formValues.id || formValues.uid;
        if (!uid) throw new Error("Missing ID for edit operation");

        res = await authFetch(`/api/harvestloads/${uid}`, {
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
      // Reload page 1
      const { items, total } = await fetchHarvestLoadsPage(authFetch, 0, PAGE_SIZE);
      setData(items);
      setSkip(items.length);
      setTotal(total);
      setHasMore(items.length < total);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  }

  // Get unique vintages for the dropdown
  const vintageOptions = Array.from(
    new Set(data.map((rec) => rec.Vintage).filter(Boolean))
  ).sort();

  // Filtering and sorting are applied client-side to loaded data
  const filtered = data.filter((rec) => {
    let match = true;
    if (crushPad !== "All" && rec.Crush_Pad !== crushPad) match = false;
    if (
      search &&
      !`${rec.Date_Received} ${rec.WO} ${rec.Block} ${rec.Vintrace_ST}`
        .toLowerCase()
        .includes(search.toLowerCase())
    )
      match = false;
    if (vintageFilter && rec.Vintage !== vintageFilter) match = false;
    if (
      dateFilter &&
      (!rec.Date_Received ||
        rec.Date_Received.slice(0, 10) !== dateFilter)
    )
      match = false;
    return match;
  });

  const sorted = [...filtered].sort((a, b) => {
    const valA = a[sortCol];
    const valB = b[sortCol];
    if (valA < valB) return sortDesc ? 1 : -1;
    if (valA > valB) return sortDesc ? -1 : 1;
    return 0;
  });

  return (
    <div className="harvestloads-root">
      <HeaderBar
        title="Harvest Loads"
        onBack={() => navigate(-1)}
        onAdd={handleAddNew}
        addLabel="+ Add"
      />
      <div className="card harvestloads-card">
        {/* Controls Row 1: Search and Crush Pad */}
        <div className="harvestloads-controls" style={{ display: "flex", gap: 8, alignItems: "center", flexWrap: "wrap" }}>
          <input
            className="harvestloads-search"
            placeholder="Search"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
          <select
            className="harvestloads-crushpad"
            value={crushPad}
            onChange={(e) => setCrushPad(e.target.value)}
          >
            {CRUSH_PADS.map((cp) => (
              <option value={cp} key={cp}>
                {cp}
              </option>
            ))}
          </select>
        </div>
        {/* Controls Row 2: Vintage and Date */}
        <div className="harvestloads-controls">
          <select
            className="harvestloads-dropdown"
            value={vintageFilter}
            onChange={(e) => setVintageFilter(e.target.value)}
          >
            <option value="">All Vintages</option>
            {vintageOptions.map((vin) => (
              <option value={vin} key={vin}>
                {vin}
              </option>
            ))}
          </select>
          <input
            type="date"
            className="harvestloads-date"
            value={dateFilter}
            onChange={(e) => setDateFilter(e.target.value)}
          />
          {(vintageFilter || dateFilter) && (
            <button
              className="harvestloads-clear-btn"
              onClick={() => {
                setVintageFilter("");
                setDateFilter("");
              }}
            >
              Clear Filters
            </button>
          )}
        </div>
        <div
          className="harvestloads-table-scroll"
          id="harvestloads-scrollable"
          style={{ maxHeight: 600, overflow: "auto" }}
        >
          <InfiniteScroll
            dataLength={data.length}
            next={fetchMoreData}
            hasMore={hasMore}
            loader={
              loading && (
                <tr>
                  <td colSpan={6} style={{ textAlign: "center", padding: 24 }}>
                    Loading...
                  </td>
                </tr>
              )
            }
            scrollableTarget="harvestloads-scrollable"
            endMessage={
              !loading && (
                <tr>
                  <td colSpan={6} style={{ textAlign: "center", padding: 24 }}>
                    All records loaded.
                  </td>
                </tr>
              )
            }
            style={{ overflow: "visible" }}
          >
            <table className="harvestloads-table">
              <thead>
                <tr>
                  {["Date_Received", "WO", "Block", "Vintrace_ST", "Tons"].map(
                    (col) => (
                      <th
                        key={col}
                        onClick={() => {
                          setSortCol(col);
                          setSortDesc((c) => (sortCol === col ? !c : false));
                        }}
                      >
                        {col.replace("_", " ")} {sortCol === col ? (sortDesc ? "▼" : "▲") : ""}
                      </th>
                    )
                  )}
                  <th></th>
                </tr>
              </thead>
              <tbody>
                {sorted.map((rec) => (
                  <tr key={rec.id}>
                    <td>{rec.Date_Received}</td>
                    <td>{rec.WO}</td>
                    <td>{rec.Block}</td>
                    <td>{rec.Vintrace_ST}</td>
                    <td>{rec.Tons}</td>
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
                ))}
                {sorted.length === 0 && (
                  <tr>
                    <td colSpan={6} style={{ textAlign: "center", padding: 24 }}>
                      No records found.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </InfiniteScroll>
        </div>
        {error && (
          <div style={{ color: "red", padding: 10, textAlign: "center" }}>
            {error}
          </div>
        )}
      </div>
      <AddEditHarvestLoadForm
        show={showForm}
        onClose={() => setShowForm(false)}
        onSubmit={handleFormSubmit}
        initialData={formMode === "edit" ? selectedRecord : undefined}
        mode={formMode}
      />
    </div>
  );
}