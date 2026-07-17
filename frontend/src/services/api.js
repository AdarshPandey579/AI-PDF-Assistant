import axios from "axios";

const api = axios.create({
  baseURL: "https://ai-pdf-assistant-backend-sv9y.onrender.com",
});

export default api;