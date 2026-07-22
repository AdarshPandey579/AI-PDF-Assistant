import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import ChatPage from "./pages/ChatPage";
import SummarizerPage from "./pages/SummarizerPage";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/chat" element={<ChatPage />} />
      <Route path="/summarizer" element={<SummarizerPage />} />
    </Routes>
  );
}

export default App;