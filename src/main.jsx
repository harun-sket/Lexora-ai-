import React from "react";
import ReactDOM from "react-dom/client";

import App from "./App.jsx";

import "./style.css";
import "./pages/index.css";
import "./pages/auth.css";
import "./pages/dashboard.css";
import "./pages/workspace-access.css";
import "./pages/workspace.css";

ReactDOM.createRoot(
  document.getElementById("root")
).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
