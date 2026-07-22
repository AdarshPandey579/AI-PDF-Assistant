import Message from "./Message";

function ChatWindow({ messages }) {

    return (
        <div className="bg-white rounded-xl shadow-lg p-6 h-450px overflow-y-auto mb-10">

            {messages.length === 0 ? (
                <p className="text-gray-500 text-center mt-10">
                    Upload PDFs and start chatting.
                </p>
            ) : (
                messages.map((message, index) => (
                    <Message
                        key={index}
                        role={message.role}
                        content={message.content}
                    />
                ))
            )}

        </div>
    );
}

export default ChatWindow;