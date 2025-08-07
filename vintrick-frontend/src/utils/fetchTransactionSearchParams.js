


export async function fetchTransactionSearchParams() {
  const res = await fetch("/api/meta/transaction-search-params");
  if (!res.ok) throw new Error("Failed to fetch params");
  const data = await res.json();
  return data.params; // Array of param metadata
}