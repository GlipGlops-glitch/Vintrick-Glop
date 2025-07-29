import React from "react";
import { Form } from "react-bootstrap";

export const ALL_FIELDS = [
  { key: "uid", label: "UID" },
  { key: "Vintrace_ST", label: "Vintrace ST" },
  { key: "Block", label: "Block" },
  { key: "Tons", label: "Tons" },
  { key: "Press", label: "Press" },
  { key: "Tank", label: "Tank" },
  { key: "WO", label: "Work Order (WO)" },
  { key: "Date_Received", label: "Date Received" },
  { key: "AgCode_ST", label: "AgCode ST" },
  { key: "Time_Received", label: "Time Received" },
  { key: "Wine_Type", label: "Wine Type" },
  { key: "Est_Tons_1", label: "Est Tons 1" },
  { key: "Est_Tons_2", label: "Est Tons 2" },
  { key: "Est_Tons_3", label: "Est Tons 3" },
  { key: "Press_Pick_2", label: "Press Pick 2" },
  { key: "Linked", label: "Linked" },
  { key: "Crush_Pad", label: "Crush Pad" },
  { key: "Status", label: "Status" },
  { key: "last_modified", label: "Last Modified" },
  { key: "synced", label: "Synced" },
];

const isNumField = (key) =>
  key === "Tons" ||
  key === "Est_Tons_1" ||
  key === "Est_Tons_2" ||
  key === "Est_Tons_3";

const CRUSH_PADS = ["White Crush Pad", "Red Crush Pad", "Reserve Crush Pad"];

export default function HarvestLoadFormBody({
  form,
  visible,
  handleChange,
  mode = "add",
  error,
  disableAll = false,
}) {
  return (
    <>
      {ALL_FIELDS.map((field) => {
        if (!visible[field.key]) return null;

        if (field.key === "Crush_Pad") {
          return (
            <Form.Group className="mb-3" key={field.key}>
              <Form.Label>{field.label}</Form.Label>
              <Form.Select
                name={field.key}
                value={form[field.key] ?? CRUSH_PADS[0]}
                onChange={handleChange}
                required
                disabled={disableAll}
              >
                {CRUSH_PADS.map((cp) => (
                  <option key={cp} value={cp}>
                    {cp}
                  </option>
                ))}
              </Form.Select>
            </Form.Group>
          );
        }

        if (field.key === "synced") {
          return (
            <Form.Group className="mb-3" key={field.key}>
              <Form.Check
                type="checkbox"
                label={field.label}
                name="synced"
                checked={!!form.synced}
                onChange={(e) =>
                  handleChange({
                    target: { name: "synced", value: e.target.checked },
                  })
                }
                disabled={disableAll}
              />
            </Form.Group>
          );
        }

        if (field.key === "last_modified") {
          return (
            <Form.Group className="mb-3" key={field.key}>
              <Form.Label>{field.label}</Form.Label>
              <Form.Control
                name="last_modified"
                value={form.last_modified ?? ""}
                disabled
                readOnly
              />
            </Form.Group>
          );
        }

        return (
          <Form.Group className="mb-3" key={field.key}>
            <Form.Label>{field.label}</Form.Label>
            <Form.Control
              name={field.key}
              type={isNumField(field.key) ? "number" : "text"}
              value={form[field.key] ?? ""}
              onChange={handleChange}
              min={isNumField(field.key) ? "0" : undefined}
              step={isNumField(field.key) ? "any" : undefined}
              required={
                mode === "add" && (field.key === "uid" || field.key === "WO")
              }
              disabled={disableAll}
            />
          </Form.Group>
        );
      })}
    </>
  );
}
