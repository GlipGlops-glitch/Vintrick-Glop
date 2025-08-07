// vintrick-frontend/src/screens/DataScreen.js

import "../styles/AppShared.css";
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import ModernHeaderBar from "../components/ModernHeaderBar";
import axios from "axios";

// Column definitions (used for mapping and table headers)
const ALL_COLUMNS = [
  "Task", "Scheduled", "Crush Pad", "Time", "Comment", "Ranch", "Block", "Allocation", "Tons",
  "Brand", "Ferm Site", "Variety", "Pick", "Analysis", "Date", "Brix", "pH", "TA",
];

const BOOKINGS_COLUMNS = ["bookingNumber", "block", "dateOccurred", "Status"];
const FRUIT_COLUMNS = [
  "externalWeighTag", "bookingNumber", "block", "gross_value",
  "tare_value", "net_value", "dateOccurred"
];

// --- Improved VintraceTransactionSearchForm ---
// Now directly triggers the legacy fetcher endpoint, shows stdout/stderr
function VintraceTransactionSearchForm() {
  const [params, setParams] = useState([]);
  const [form, setForm] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [result, setResult] = useState(null);
  const [fetching, setFetching] = useState(false);

  useEffect(() => {
    async function fetchParams() {
      try {
        const res = await axios.get("/api/meta/transaction-search-params");
        setParams(res.data.params || []);
        setLoading(false);
      } catch (err) {
        setError("Failed to load param metadata");
        setLoading(false);
      }
    }
    fetchParams();
  }, []);

  function isDateParam(param) {
    return (
      param.type === "string" &&
      param.description &&
      param.description.toLowerCase().includes("yyyy-mm-dd")
    );
  }

  const handleChange = (name, value) => {
    setForm(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setFetching(true);
    setResult(null);
    setError("");
    // Format all date param fields to YYYY-MM-DD
    const formattedForm = { ...form };
    params.forEach(param => {
      if (isDateParam(param) && form[param.name]) {
        formattedForm[param.name] = form[param.name].slice(0, 10);
      }
    });

    try {
      // POST to the legacy fetcher endpoint
      const res = await axios.post("/api/vintrace/run-trans-fetch/", null, {
        params: formattedForm
      });
      setResult(res.data); // { status, stdout, stderr }
    } catch (err) {
      setError(
        err.response?.data?.detail ||
        err.response?.data?.error ||
        err.message ||
        "Unknown error"
      );
    } finally {
      setFetching(false);
    }
  };

  if (loading) return <div>Loading search parameters...</div>;
  if (error) return <div style={{ color: "red" }}>{error}</div>;

  return (
    <form style={{ display: "flex", flexDirection: "column", gap: 12 }} onSubmit={handleSubmit}>
      {params.map((param) => (
        <label key={param.name}>
          {param.name}
          {isDateParam(param) ? (
            <input
              type="date"
              name={param.name}
              value={form[param.name] || ""}
              onChange={e => handleChange(param.name, e.target.value)}
              className="input"
              style={{ minWidth: 140 }}
            />
          ) : (
            <input
              type={param.type === "string" ? "text" : param.type}
              name={param.name}
              value={form[param.name] || ""}
              placeholder={param.example}
              onChange={e => handleChange(param.name, e.target.value)}
              className="input"
              style={{ minWidth: 140 }}
            />
          )}
          <small style={{ display: "block", color: "#555" }}>{param.description}</small>
        </label>
      ))}
      <button
        className="nav-btn nav-btn-purple"
        type="submit"
        style={{ marginTop: 12 }}
        disabled={fetching}
      >
        {fetching ? "Running Fetch..." : "Run Legacy Vintrace Fetch"}
      </button>
      {/* Show result or error */}
      {result && (
        <div style={{ marginTop: 16 }}>
          <b>Status:</b> {result.status}<br />
          <b>Stdout:</b>
          <pre style={{ background: "#f7f6fa", padding: 10, borderRadius: 6 }}>{result.stdout}</pre>
          {result.stderr && (
            <>
              <b>Stderr:</b>
              <pre style={{ background: "#fbeaea", padding: 10, borderRadius: 6 }}>{result.stderr}</pre>
            </>
          )}
        </div>
      )}
      {error && (
        <div style={{ marginTop: 16, color: "red" }}>{error}</div>
      )}
    </form>
  );
}

export default function DataScreen() {
  const [testMode, setTestMode] = useState(true);
  const [preview, setPreview] = useState({ open: false, title: "", content: "" });
  const [fieldMappingOpen, setFieldMappingOpen] = useState(false);
  const [uploadStatus, setUploadStatus] = useState("");
  const [vintraceSyncOpen, setVintraceSyncOpen] = useState(false);
  const [vintraceSyncStatus, setVintraceSyncStatus] = useState("");
  const [vintraceSyncLoading, setVintraceSyncLoading] = useState(false);
  const [vintraceSyncResult, setVintraceSyncResult] = useState(null);
  const [vintraceSyncError, setVintraceSyncError] = useState(null);

  const [vintraceStartDate, setVintraceStartDate] = useState("");
  const [vintraceEndDate, setVintraceEndDate] = useState("");

  const [bookings, setBookings] = useState([]);
  const [fruitIntake, setFruitIntake] = useState([]);
  const [tableModal, setTableModal] = useState({ open: false, title: "", records: [], columns: [], editType: "" });

  const navigate = useNavigate();

  // Simulate DB (use backend API in real code)
  const loadBookings = () => setBookings([
    { bookingNumber: "25001-01", block: "A1", dateOccurred: "2025-08-01", Status: "imported" },
    { bookingNumber: "25001-02", block: "B2", dateOccurred: "2025-08-02", Status: "imported" }
  ]);
  const loadFruitIntake = () => setFruitIntake([
    { externalWeighTag: "FT-001", bookingNumber: "25001-01", block: "A1", gross_value: 1000, tare_value: 200, net_value: 800, dateOccurred: "2025-08-01" }
  ]);

  const handlePreviewBookings = () =>
    setPreview({
      open: true,
      title: "Bookings Preview",
      content: "File preview not implemented yet.",
    });
  const handleImportBookings = () =>
    alert("Import/Post Bookings not implemented yet.");
  const handlePreviewFruit = () =>
    setPreview({
      open: true,
      title: "Fruit Intake Preview",
      content: "Fruit intake preview not implemented yet.",
    });
  const handleImportFruit = () =>
    alert("Import/Post Fruit Intake not implemented yet.");
  const handleViewAllBookings = () => {
    loadBookings();
    setTableModal({ open: true, title: "All Bookings", records: bookings, columns: BOOKINGS_COLUMNS, editType: "booking" });
  };
  const handleViewAllFruit = () => {
    loadFruitIntake();
    setTableModal({ open: true, title: "All Fruit Intake", records: fruitIntake, columns: FRUIT_COLUMNS, editType: "fruit" });
  };
  const handleFieldMapping = () => setFieldMappingOpen(true);

  const handleSqlUpload = async () => {
    setUploadStatus("Uploading...");
    try {
      const res = await axios.post("/api/data/sql-upload");
      if (res.data && res.data.success) {
        setUploadStatus("✅ SQL upload complete!");
      } else {
        setUploadStatus("❌ SQL upload failed.");
      }
    } catch (err) {
      setUploadStatus("❌ Error during SQL upload.");
    }
  };

  // ---- Vintrace Sync Controls ----
  const openVintraceSyncModal = () => {
    setVintraceSyncOpen(true);
    setVintraceSyncStatus("");
    setVintraceSyncResult(null);
    setVintraceSyncError(null);
    setVintraceStartDate("");
    setVintraceEndDate("");
  };
  const handleVintraceSync = async (e) => {
    e.preventDefault();
    setVintraceSyncLoading(true);
    setVintraceSyncStatus("Starting sync...");
    setVintraceSyncResult(null);
    setVintraceSyncError(null);

    try {
      const res = await axios.post(
        `/api/vintrace_api/fetch_and_update?start_date=${encodeURIComponent(vintraceStartDate)}&end_date=${encodeURIComponent(vintraceEndDate)}`
      );
      setVintraceSyncStatus("");
      setVintraceSyncResult(res.data);
    } catch (err) {
      setVintraceSyncStatus("");
      setVintraceSyncError(
        err.response?.data?.detail || err.message || "Unknown error"
      );
    } finally {
      setVintraceSyncLoading(false);
    }
  };

  // ---- TransSum Sync Controls ----
  const [transSumSyncOpen, setTransSumSyncOpen] = useState(false);
  const [transSumSyncStatus, setTransSumSyncStatus] = useState("");
  const [transSumSyncLoading, setTransSumSyncLoading] = useState(false);
  const [transSumSyncResult, setTransSumSyncResult] = useState(null);
  const [transSumSyncError, setTransSumSyncError] = useState(null);
  const [transSumStartDate, setTransSumStartDate] = useState("");
  const [transSumEndDate, setTransSumEndDate] = useState("");

  const openTransSumSyncModal = () => {
    setTransSumSyncOpen(true);
    setTransSumSyncStatus("");
    setTransSumSyncResult(null);
    setTransSumSyncError(null);
    setTransSumStartDate("");
    setTransSumEndDate("");
  };

  const handleTransSumSync = async (e) => {
    e.preventDefault();
    setTransSumSyncLoading(true);
    setTransSumSyncStatus("Starting trans_sum sync...");
    setTransSumSyncResult(null);
    setTransSumSyncError(null);

    try {
      // Call the backend endpoint for trans_sum sync
      const res = await axios.post(
        `/api/vintrace/pull-transactions/`,
        {
          start_date: transSumStartDate,
          end_date: transSumEndDate,
        }
      );
      setTransSumSyncStatus("");
      setTransSumSyncResult(res.data);
    } catch (err) {
      setTransSumSyncStatus("");
      setTransSumSyncError(
        err.response?.data?.detail || err.message || "Unknown error"
      );
    } finally {
      setTransSumSyncLoading(false);
    }
  };

  // --- Vintrace Transaction Search Modal (Legacy Fetch) ---
  const [vintraceSearchOpen, setVintraceSearchOpen] = useState(false);

  const openVintraceSearchModal = () => {
    setVintraceSearchOpen(true);
  };

  // --- Transaction Search Modal (API, not legacy fetch) ---
  const [apiSearchOpen, setApiSearchOpen] = useState(false);
  const [apiSearchResult, setApiSearchResult] = useState(null);
  const [apiSearchLoading, setApiSearchLoading] = useState(false);
  const [apiSearchError, setApiSearchError] = useState("");

  const openApiSearchModal = () => {
    setApiSearchOpen(true);
    setApiSearchResult(null);
    setApiSearchError("");
  };

  const handleTransactionSearch = async (searchParams) => {
    setApiSearchLoading(true);
    setApiSearchResult(null);
    setApiSearchError("");
    try {
      // Build query string from params
      const query = Object.entries(searchParams)
        .filter(([_, v]) => v !== "")
        .map(([k, v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`)
        .join("&");
      // Adjust endpoint to match your backend!
      const res = await axios.get(`/api/vintrace/transaction/search/?${query}`);
      setApiSearchResult(res.data);
    } catch (err) {
      setApiSearchError(
        err.response?.data?.detail || err.message || "Unknown error"
      );
    } finally {
      setApiSearchLoading(false);
    }
  };

  return (
    <div className="app-root">
      <ModernHeaderBar />
      <div className="card harvestloads-card">
        <div className="harvestloads-controls" style={{ flexWrap: "wrap" }}>
          <button className="nav-btn nav-btn-light" onClick={handlePreviewBookings}>
            Preview Bookings Upload
          </button>
          <button className="nav-btn nav-btn-blue" onClick={handleImportBookings}>
            Import/Post Bookings
          </button>
          <button className="nav-btn nav-btn-light" onClick={handlePreviewFruit}>
            Preview Fruit Intake Upload
          </button>
          <button className="nav-btn nav-btn-green" onClick={handleImportFruit}>
            Import/Post Fruit Intake
          </button>
          <button className="nav-btn nav-btn-light" onClick={handleViewAllBookings}>
            View All Bookings
          </button>
          <button className="nav-btn nav-btn-light" onClick={handleViewAllFruit}>
            View All Fruit Intake
          </button>
          <button className="nav-btn nav-btn-light" onClick={handleFieldMapping}>
            Field Mapping
          </button>
          <button className="nav-btn nav-btn-orange" onClick={handleSqlUpload}>
            SQL Server Upload
          </button>
          <button className="nav-btn nav-btn-purple" onClick={openVintraceSyncModal}>
            Vintrace Sync
          </button>
          {/* API Transaction Search */}
          <button className="nav-btn nav-btn-teal" onClick={openApiSearchModal}>
            Search Vintrace Transactions (API)
          </button>
          {/* Legacy Fetcher Button */}
          <button className="nav-btn nav-btn-pink" onClick={openVintraceSearchModal}>
            Run Legacy Vintrace Fetch
          </button>
          <button className="nav-btn nav-btn-pink" onClick={openTransSumSyncModal}>
            Sync TransSum from Vintrace
          </button>
        </div>
        <div className="harvestloads-controls" style={{ marginBottom: 0 }}>
          <label htmlFor="testModeToggle" style={{ marginRight: 8 }}>
            Test
          </label>
          <input
            id="testModeToggle"
            type="checkbox"
            checked={testMode}
            onChange={() => setTestMode(!testMode)}
          />
        </div>

        {uploadStatus && (
          <div className="datascreen-status">{uploadStatus}</div>
        )}

        {/* Preview Modal */}
        {preview.open && (
          <Modal
            title={preview.title}
            onClose={() => setPreview({ ...preview, open: false })}
          >
            <pre className="datascreen-modal-pre">{preview.content}</pre>
          </Modal>
        )}

        {/* Field Mapping Modal (Stub) */}
        {fieldMappingOpen && (
          <Modal
            title="Field Mapping"
            onClose={() => setFieldMappingOpen(false)}
          >
            <div>
              <p>This would show a field mapping UI.</p>
              <button
                className="nav-btn nav-btn-light"
                onClick={() => setFieldMappingOpen(false)}
              >
                Close
              </button>
            </div>
          </Modal>
        )}

        {/* Table Modal for Bookings and Fruit Intake */}
        {tableModal.open && (
          <Modal
            title={tableModal.title}
            onClose={() => setTableModal({ ...tableModal, open: false })}
          >
            <TableView
              records={tableModal.records}
              columns={tableModal.columns}
              editType={tableModal.editType}
              onClose={() => setTableModal({ ...tableModal, open: false })}
            />
          </Modal>
        )}

        {/* Vintrace Sync Modal */}
        {vintraceSyncOpen && (
          <Modal
            title="Sync Vintrace Harvest Loads"
            onClose={() => setVintraceSyncOpen(false)}
          >
            <form
              style={{ display: "flex", flexDirection: "column", gap: 12, marginBottom: 12 }}
              onSubmit={handleVintraceSync}
            >
              <label>
                Start Date:{" "}
                <input
                  type="date"
                  value={vintraceStartDate}
                  onChange={e => setVintraceStartDate(e.target.value)}
                  required
                  className="input"
                  style={{ minWidth: 140 }}
                />
              </label>
              <label>
                End Date:{" "}
                <input
                  type="date"
                  value={vintraceEndDate}
                  onChange={e => setVintraceEndDate(e.target.value)}
                  required
                  className="input"
                  style={{ minWidth: 140 }}
                />
              </label>
              <button
                className="nav-btn nav-btn-purple"
                type="submit"
                style={{ marginTop: 12, fontSize: 16 }}
                disabled={vintraceSyncLoading || !vintraceStartDate || !vintraceEndDate}
              >
                {vintraceSyncLoading ? "Syncing..." : "Start Sync"}
              </button>
            </form>
            {vintraceSyncStatus && (
              <div style={{ textAlign: "center", color: "#8d41e9", margin: 6 }}>
                {vintraceSyncStatus}
              </div>
            )}
            {vintraceSyncResult && (
              <div style={{ textAlign: "center", color: "green", margin: 6 }}>
                <b>Sync started:</b>
                <pre
                  style={{
                    background: "#f7f6fa",
                    padding: "10px",
                    borderRadius: "6px",
                    marginTop: 8,
                    fontSize: 15,
                    color: "#222"
                  }}
                >
                  {JSON.stringify(vintraceSyncResult, null, 2)}
                </pre>
              </div>
            )}
            {vintraceSyncError && (
              <div style={{ color: "red", textAlign: "center", margin: 6 }}>
                {vintraceSyncError}
              </div>
            )}
          </Modal>
        )}

        {/* TransSum Sync Modal */}
        {transSumSyncOpen && (
          <Modal
            title="Sync TransSum from Vintrace"
            onClose={() => setTransSumSyncOpen(false)}
          >
            <form
              style={{ display: "flex", flexDirection: "column", gap: 12, marginBottom: 12 }}
              onSubmit={handleTransSumSync}
            >
              <label>
                Start Date:{" "}
                <input
                  type="date"
                  value={transSumStartDate}
                  onChange={e => setTransSumStartDate(e.target.value)}
                  required
                  className="input"
                  style={{ minWidth: 140 }}
                />
              </label>
              <label>
                End Date:{" "}
                <input
                  type="date"
                  value={transSumEndDate}
                  onChange={e => setTransSumEndDate(e.target.value)}
                  required
                  className="input"
                  style={{ minWidth: 140 }}
                />
              </label>
              <button
                className="nav-btn nav-btn-pink"
                type="submit"
                style={{ marginTop: 12, fontSize: 16 }}
                disabled={transSumSyncLoading || !transSumStartDate || !transSumEndDate}
              >
                {transSumSyncLoading ? "Syncing..." : "Start Sync"}
              </button>
            </form>
            {transSumSyncStatus && (
              <div style={{ textAlign: "center", color: "#d41e8d", margin: 6 }}>
                {transSumSyncStatus}
              </div>
            )}
            {transSumSyncResult && (
              <div style={{ textAlign: "center", color: "green", margin: 6 }}>
                <b>Sync started:</b>
                <pre
                  style={{
                    background: "#f7f6fa",
                    padding: "10px",
                    borderRadius: "6px",
                    marginTop: 8,
                    fontSize: 15,
                    color: "#222"
                  }}
                >
                  {JSON.stringify(transSumSyncResult, null, 2)}
                </pre>
              </div>
            )}
            {transSumSyncError && (
              <div style={{ color: "red", textAlign: "center", margin: 6 }}>
                {transSumSyncError}
              </div>
            )}
          </Modal>
        )}

        {/* --- API Transaction Search Modal --- */}
        {apiSearchOpen && (
          <Modal
            title="Search Vintrace Transactions (API)"
            onClose={() => setApiSearchOpen(false)}
          >
            {/* Reuse the original form, pass onSearch as prop */}
            <VintraceTransactionSearchForm onSearch={handleTransactionSearch} />
            {apiSearchLoading && (
              <div style={{ textAlign: "center", color: "#2cb0a0", margin: 6 }}>
                Searching...
              </div>
            )}
            {apiSearchResult && (
              <div style={{ textAlign: "center", color: "green", margin: 6 }}>
                <b>Results:</b>
                <pre
                  style={{
                    background: "#f7f6fa",
                    padding: "10px",
                    borderRadius: "6px",
                    marginTop: 8,
                    fontSize: 15,
                    color: "#222"
                  }}
                >
                  {JSON.stringify(apiSearchResult, null, 2)}
                </pre>
              </div>
            )}
            {apiSearchError && (
              <div style={{ color: "red", textAlign: "center", margin: 6 }}>
                {apiSearchError}
              </div>
            )}
          </Modal>
        )}

        {/* --- Legacy Fetcher Transaction Search Modal --- */}
        {vintraceSearchOpen && (
          <Modal
            title="Run Legacy Vintrace Transaction Fetch"
            onClose={() => setVintraceSearchOpen(false)}
          >
            {/* Improved form, triggers legacy fetcher */}
            <VintraceTransactionSearchForm />
          </Modal>
        )}
      </div>
    </div>
  );
}

// --- Table View Modal for "View All ..." ---
function TableView({ records, columns, editType }) {
  return (
    <div style={{ maxHeight: 400, overflow: "auto" }}>
      <table className="datascreen-table">
        <thead>
          <tr>
            {columns.map((col) => (
              <th key={col}>{col}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {records.length === 0 ? (
            <tr>
              <td colSpan={columns.length} style={{ textAlign: "center" }}>
                No records found.
              </td>
            </tr>
          ) : (
            records.map((rec, idx) => (
              <tr key={idx}>
                {columns.map((col) => (
                  <td key={col}>{rec[col]}</td>
                ))}
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}

// --- Modal component with themed style ---
function Modal({ title, onClose, children }) {
  return (
    <div className="datascreen-modal-backdrop">
      <div className="datascreen-modal-card">
        <h3>{title}</h3>
        <div>{children}</div>
        <button
          className="nav-btn nav-btn-light"
          style={{ marginTop: 16, float: "right" }}
          onClick={onClose}
        >
          Close
        </button>
      </div>
    </div>
  );
}