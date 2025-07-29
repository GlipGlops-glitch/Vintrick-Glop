// src/screens/SettingsScreen.js

import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import HeaderBar from "../components/HeaderBar";
import { useSettings } from "../context/SettingsContext";
import { Modal } from "react-bootstrap";
import HarvestLoadFormBody, {
  ALL_FIELDS,
} from "../components/HarvestLoadFormBody";
import { DragDropContext, Droppable, Draggable } from "@hello-pangea/dnd";

// Helper for DnD reorder
function reorder(array, startIndex, endIndex) {
  const result = Array.from(array);
  const [removed] = result.splice(startIndex, 1);
  result.splice(endIndex, 0, removed);
  return result;
}

export default function SettingsScreen() {
  const navigate = useNavigate();
  const { settings, setSettings } = useSettings();
  const [showHLModal, setShowHLModal] = useState(false);

  // Column setting (persisted)
  const previewColumns = settings.harvestLoadForm.previewColumns || 1;
  function setPreviewColumns(cols) {
    setSettings((prev) => ({
      ...prev,
      harvestLoadForm: {
        ...prev.harvestLoadForm,
        previewColumns: cols,
      },
    }));
  }

  // Order/toggle state
  const fieldOrder =
    settings.harvestLoadForm.order || ALL_FIELDS.map((f) => f.key);
  function setFieldOrder(newOrder) {
    setSettings((prev) => ({
      ...prev,
      harvestLoadForm: {
        ...prev.harvestLoadForm,
        order: newOrder,
      },
    }));
  }
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
  const orderedFields = fieldOrder
    .map((key) => ALL_FIELDS.find((f) => f.key === key))
    .filter(Boolean);

  // Only visible fields participate in drag/reorder preview grid
  const visibleFields = orderedFields.filter(
    (f) => settings.harvestLoadForm.fields[f.key],
  );

  function onDragEnd(result) {
    if (!result.destination) return;
    // Reorder among visible only, but update the master order
    const visibleKeys = visibleFields.map((f) => f.key);
    const reordered = reorder(
      visibleKeys,
      result.source.index,
      result.destination.index,
    );
    // Merge this into the full master order:
    const newOrder = [];
    let reorderedIdx = 0;
    for (let key of fieldOrder) {
      if (visibleKeys.includes(key)) {
        newOrder.push(reordered[reorderedIdx]);
        reorderedIdx++;
      } else {
        newOrder.push(key);
      }
    }
    setFieldOrder(newOrder);
  }

  // For live preview demo values
  const previewForm = {};
  ALL_FIELDS.forEach((f) => {
    if (f.key === "Tons" || f.key.startsWith("Est_Tons"))
      previewForm[f.key] = 0;
    else if (f.key === "synced") previewForm[f.key] = false;
    else if (f.key === "Crush_Pad") previewForm[f.key] = "White Crush Pad";
    else if (f.key === "last_modified")
      previewForm[f.key] = new Date().toISOString();
    else previewForm[f.key] = "";
  });

  return (
    <div className="settings-root">
      <HeaderBar title="Settings" onBack={() => navigate(-1)} />
      <div
        className="card settings-card"
        style={{ maxWidth: 480, margin: "40px auto", padding: 28 }}
      >
        <h3 style={{ marginBottom: 28, fontWeight: 700, fontSize: 22 }}>
          Developer/Feature Settings
        </h3>
        <button
          className="nav-btn nav-btn-light"
          style={{
            width: "100%",
            margin: "12px 0",
            fontWeight: 700,
            fontSize: 16,
            borderRadius: 14,
            padding: "14px 0",
            border: "none",
            background: "var(--primary-bg, #f6f5fa)",
            color: "var(--primary, #636fa4)",
            boxShadow: "0 2px 10px rgba(120,100,190,0.07)",
            cursor: "pointer",
          }}
          onClick={() => setShowHLModal(true)}
        >
          Harvest Loads Form Settings
        </button>
      </div>
      <Modal
        show={showHLModal}
        onHide={() => setShowHLModal(false)}
        size="lg"
        centered
      >
        <Modal.Header closeButton>
          <Modal.Title>Harvest Loads Form Settings</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <div style={{ marginBottom: 18 }}>
            <label style={{ marginRight: 12, fontWeight: 500 }}>
              Preview Columns:
            </label>
            <select
              value={previewColumns}
              onChange={(e) => setPreviewColumns(Number(e.target.value))}
              style={{
                padding: "5px 10px",
                borderRadius: 8,
                border: "1px solid #bbb",
                fontSize: 15,
              }}
            >
              {[1, 2, 3].map((c) => (
                <option key={c} value={c}>
                  {c}
                </option>
              ))}
            </select>
          </div>
          <DragDropContext onDragEnd={onDragEnd}>
            <div
              style={{
                display: "flex",
                gap: 32,
                flexWrap: "wrap",
                justifyContent: "center",
                alignItems: "flex-start",
              }}
            >
              {/* Visible Fields Controls - NOT draggable */}
              <div
                style={{
                  minWidth: 230,
                  maxWidth: 270,
                }}
              >
                <h5 style={{ marginBottom: 2, fontWeight: 700 }}>
                  Visible Fields
                </h5>
                <div
                  style={{ fontWeight: 400, fontSize: 14, marginBottom: 16 }}
                >
                  Toggle visibility
                </div>
                <ul
                  style={{
                    listStyle: "none",
                    padding: 0,
                    margin: 0,
                    maxHeight: 470,
                    overflowY: "auto",
                  }}
                >
                  {orderedFields.map((field) => (
                    <li
                      key={field.key}
                      style={{
                        margin: "12px 0",
                        display: "flex",
                        alignItems: "center",
                        borderRadius: 7,
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
                          marginRight: 10,
                        }}
                      />
                      <label
                        htmlFor={`field-${field.key}`}
                        style={{
                          fontSize: 16,
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

              {/* Live Form Preview - ONLY visible fields, draggable, scrollable grid */}
              <Droppable droppableId="preview" direction="vertical">
                {(provided) => (
                  <div
                    ref={provided.innerRef}
                    {...provided.droppableProps}
                    className="settings-preview-grid"
                    style={{
                      flex: 1,
                      minWidth: 320,
                      maxWidth: 430 * previewColumns,
                      maxHeight: 520,
                      overflowY: "auto",
                      display: "grid",
                      gap: "18px",
                      gridTemplateColumns: `repeat(${previewColumns}, 1fr)`,
                      alignItems: "start",
                    }}
                  >
                    {visibleFields.map((field, idx) => (
                      <Draggable
                        key={field.key}
                        draggableId={field.key}
                        index={idx}
                      >
                        {(provided, snapshot) => (
                          <div
                            ref={provided.innerRef}
                            {...provided.draggableProps}
                            className={
                              "preview-draggable-field" +
                              (snapshot.isDragging ? " is-dragging" : "")
                            }
                            style={{
                              ...provided.draggableProps.style,
                            }}
                          >
                            <div
                              style={{
                                display: "flex",
                                alignItems: "center",
                                gap: "7px",
                              }}
                            >
                              <span
                                {...provided.dragHandleProps}
                                className="preview-drag-handle"
                                title="Drag to reorder"
                                style={{
                                  fontSize: 19,
                                  cursor: "grab",
                                  color: "#a3a2c2",
                                  userSelect: "none",
                                  flexShrink: 0,
                                }}
                              >
                                ☰
                              </span>
                              <div style={{ flex: 1, minWidth: 0 }}>
                                <HarvestLoadFormBody
                                  form={previewForm}
                                  visible={{ [field.key]: true }}
                                  handleChange={() => {}}
                                  mode="add"
                                  error={null}
                                  disableAll={true}
                                />
                              </div>
                            </div>
                          </div>
                        )}
                      </Draggable>
                    ))}
                    {provided.placeholder}
                  </div>
                )}
              </Droppable>
            </div>
          </DragDropContext>
        </Modal.Body>
        <Modal.Footer>
          <button
            className="btn btn-secondary"
            onClick={() => setShowHLModal(false)}
          >
            Done
          </button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}
