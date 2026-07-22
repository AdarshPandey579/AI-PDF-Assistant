import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

import { useState } from "react";
import UploadSection from "../components/chat/UploadSection";
import ChatWindow from "../components/chat/ChatWindow";
import ChatInput from "../components/chat/ChatInput";

function ChatPage() {
  const [messages, setMessages] = useState([
        {
            role: "assistant",
            content: "Hello! Upload your PDFs and ask me anything."
        }
    ]);

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">

      <Navbar />

      <main className="flex-1 max-w-5xl mx-auto w-full p-6">

        <UploadSection />

        <ChatWindow messages={messages}/>

        <ChatInput setMessages={setMessages} />

      </main>

      <Footer />

    </div>
  );
}

export default ChatPage;

    //         ChatPage
    //     ┌─────────────────┐
    //     │ messages        │
    //     │ setMessages()   │
    //     └─────────────────┘
    //        │           │
    //        │           │
    //        ▼           ▼
    // ChatWindow      ChatInput
    //   (read)         (update)