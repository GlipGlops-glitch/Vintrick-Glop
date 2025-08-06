// src/components/BlendFormBody.js

import React from "react";
import { Form } from "react-bootstrap";

export const BLEND_FIELDS = [
  { key: "Title", label: "Title" },
  { key: "Brand", label: "Brand" },
  { key: "Varietal", label: "Varietal" },
  { key: "Vintage", label: "Vintage" },
  { key: "WineType", label: "Wine Type" },
];

export default function BlendFormBody({ formData, handleChange, disableAll = false }) {
  return (
    <>
      {BLEND_FIELDS.map(field => (
        <Form.Group className="mb-3" key={field.key}>
          <Form.Label htmlFor={`blend-${field.key}`}>{field.label}</Form.Label>
          <Form.Control
            id={`blend-${field.key}`}
            name={field.key}
            value={formData[field.key] ?? ""}
            onChange={handleChange}
            autoComplete="off"
            disabled={disableAll}
          />
        </Form.Group>
      ))}
    </>
  );
}