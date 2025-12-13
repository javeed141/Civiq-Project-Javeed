// import React, { useState, useContext, useEffect, useRef } from "react";
// import { ThemeContext } from "../Context/ThemeContext";

// export default function Chatbot() {
//   const { isDark } = useContext(ThemeContext);
//   const [open, setOpen] = useState(false);
//   const [messages, setMessages] = useState([
//     { from: "bot", text: "Hi! Need help reporting or tracking an issue?" },
//   ]);
//   const [input, setInput] = useState("");
//   const listRef = useRef(null);

//   useEffect(() => {
//     if (listRef.current) listRef.current.scrollTop = listRef.current.scrollHeight;
//   }, [messages, open]);

// // const sendMessage = async () => {
// //   if (!input.trim()) return;

// //   const userMsg = { from: "user", text: input.trim() };

// //   // update UI immediately
// //   setMessages((prev) => [...prev, userMsg]);
// //   setInput("");

// //   // convert chat history to API format
// //   const payloadMessages = [...messages, userMsg].map((m) => ({
// //     role: m.from === "user" ? "user" : "assistant",
// //     content: m.text,
// //   }));

// //   try {
// //     const res = await fetch("http://localhost:5000/ask", {
// //       method: "POST",
// //       headers: {
// //         "Content-Type": "application/json",
// //       },
// //       body: JSON.stringify({
// //         messages: payloadMessages,
// //       }),
// //     });

// //     const data = await res.json();

// //     setMessages((prev) => [
// //       ...prev,
// //       { from: "bot", text: data.answer || "Sorry, I couldn't answer that." },
// //     ]);
// //   }  catch (err) {
// //   console.error("Chat error:", err);
// //   setMessages((prev) => [
// //     ...prev,
// //     { from: "bot", text: "Server error. Check backend logs." },
// //   ]);
// // }

// // };
// const sendMessage = async () => {
//   if (!input.trim()) return;

//   const userMsg = { from: "user", text: input.trim() };

//   // take a snapshot of current messages
//   const updatedMessages = [...messages, userMsg];

//   // update UI
//   setMessages(updatedMessages);
//   setInput("");

//   // convert FULL history to API format
//   const payloadMessages = updatedMessages.map((m) => ({
//     role: m.from === "user" ? "user" : "assistant",
//     content: m.text,
//   }));

//   try {
//     const res = await fetch("http://localhost:5000/ask", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify({
//         messages: payloadMessages,
//       }),
//     });

//     const data = await res.json();

//     setMessages((prev) => [
//       ...prev,
//       { from: "bot", text: data.answer || "Sorry, I couldn't answer that." },
//     ]);
//   } catch (err) {
//     console.error("Chat error:", err);
//     setMessages((prev) => [
//       ...prev,
//       { from: "bot", text: "Server error. Check backend logs." },
//     ]);
//   }
// };


//   return (
//     <div>
//       <div className={`fixed right-5 bottom-5 z-50`}> 
//         <div className={`flex flex-col items-end`}>
//           {open && (
//             <div className={`w-80 h-96 rounded-xl shadow-xl overflow-hidden mb-3 ${isDark ? "bg-[#1E1E1E] text-white" : "bg-white text-black"}`}>
//               <div className={`px-4 py-3 border-b ${isDark ? "border-[#333]" : "border-[#E6E6E6]"}`}>
//                 <div className="font-semibold">Support Chat</div>
//                 <div className="text-xs text-gray-400">Ask about reporting or tracking issues</div>
//               </div>
//               <div ref={listRef} className="p-3 flex-1 overflow-y-auto h-64 space-y-2">
//                 {messages.map((m, i) => (
//                   <div key={i} className={m.from === "user" ? "text-right" : "text-left"}>
//                     <div className={`inline-block px-3 py-1 rounded-lg text-sm ${m.from === "user" ? "bg-blue-600 text-white" : "bg-gray-200 text-black"}`}>
//                       {m.text}
//                     </div>
//                   </div>
//                 ))}
//               </div>
//               <div className="p-3 border-t" style={{ borderTopColor: isDark ? "#333" : "#eee" }}>
//                 <div className="flex gap-2">
//                   <input
//                     value={input}
//                     onChange={(e) => setInput(e.target.value)}
//                     onKeyDown={(e) => e.key === "Enter" && sendMessage()}
//                     placeholder="Type a message..."
//                     className={`flex-1 px-3 py-2 rounded-lg border focus:outline-none ${isDark ? "bg-[#262626] border-[#404040] text-white" : "bg-white border-[#E6E6E6] text-black"}`}
//                   />
//                   <button onClick={sendMessage} className="px-3 py-2 rounded-lg bg-blue-600 text-white">Send</button>
//                 </div>
//               </div>
//             </div>
//           )}

//           <button
//             onClick={() => setOpen((o) => !o)}
//             className={`w-14 h-14 rounded-full flex items-center justify-center shadow-lg ${isDark ? "bg-blue-600 text-white" : "bg-blue-600 text-white"}`}
//             aria-label="Open chat"
//           >
//             💬
//           </button>
//         </div>
//       </div>
//     </div>
//   );
// }
import React, { useState, useContext, useEffect, useRef } from "react";
import { ThemeContext } from "../Context/ThemeContext";

export default function Chatbot() {
  const { isDark } = useContext(ThemeContext);
  const [open, setOpen] = useState(false);
const [loading, setLoading] = useState(false);
  const [messages, setMessages] = useState([
    { from: "bot", text: "Hi! Need help reporting or tracking an issue?" },
  ]);
  const [input, setInput] = useState("");
  const listRef = useRef(null);

  // ---------------- SCROLL ----------------
  useEffect(() => {
    if (listRef.current) {
      listRef.current.scrollTop = listRef.current.scrollHeight;
    }
  }, [messages, open]);

  // ---------------- DUMMY USER DATA ----------------
  // 🔴 Replace this later with DB data
  const dummyUserIssues = [
    {
      title: "Pothole near school",
      location: "MG Road",
      status: "inprogress",
      createdAt: "2025-02-10",
      department: "Roads Department",
    },
    {
      title: "Streetlight not working",
      location: "Sector 5",
      status: "resolved",
      createdAt: "2025-01-28",
      department: "Street Lighting Department",
    },
  ];

  // ---------------- SEND MESSAGE ----------------
const sendMessage = async () => {
  if (!input.trim()) return;

  const userMsg = { from: "user", text: input.trim() };
  const updatedMessages = [...messages, userMsg];

  setMessages(updatedMessages);
  setInput("");
  setLoading(true); // 🔵 START LOADER

  const payloadMessages = updatedMessages.map((m) => ({
    role: m.from === "user" ? "user" : "assistant",
    content: m.text,
  }));

  const userData = {
    userName: "Ravi Kumar",
    issues: dummyUserIssues,
  };

  try {
    const res = await fetch("http://localhost:5000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages: payloadMessages, userData }),
    });

    const data = await res.json();

    setMessages((prev) => [
      ...prev,
      { from: "bot", text: data.answer || "I couldn't find an answer." },
    ]);
  } catch (err) {
    setMessages((prev) => [
      ...prev,
      { from: "bot", text: "Server error. Please try again." },
    ]);
  } finally {
    setLoading(false); // 🔵 STOP LOADER
  }
};

const TypingLoader = ({ isDark }) => (
  <div className="flex items-center gap-1 px-3 py-2">
    <span
      className={`w-2 h-2 rounded-full animate-bounce ${
        isDark ? "bg-gray-400" : "bg-gray-500"
      }`}
      style={{ animationDelay: "0ms" }}
    />
    <span
      className={`w-2 h-2 rounded-full animate-bounce ${
        isDark ? "bg-gray-400" : "bg-gray-500"
      }`}
      style={{ animationDelay: "150ms" }}
    />
    <span
      className={`w-2 h-2 rounded-full animate-bounce ${
        isDark ? "bg-gray-400" : "bg-gray-500"
      }`}
      style={{ animationDelay: "300ms" }}
    />
  </div>
);

  // ---------------- UI ----------------
  return (
    <div className="fixed right-5 bottom-5 z-50">
      <div className="flex flex-col items-end">
        {open && (
          <div
            className={`w-80 h-96 rounded-xl shadow-xl overflow-hidden mb-3 ${
              isDark ? "bg-[#1E1E1E] text-white" : "bg-white text-black"
            }`}
          >
            <div
              className={`px-4 py-3 border-b ${
                isDark ? "border-[#333]" : "border-[#E6E6E6]"
              }`}
            >
              <div className="font-semibold">Civiq Chat</div>
              <div className="text-xs text-gray-400">
                Ask about reporting or tracking issues
              </div>
            </div>

         <div
  ref={listRef}
  className="p-3 flex-1 overflow-y-auto h-64 space-y-2"
>
  {messages.map((m, i) => (
    <div
      key={i}
      className={m.from === "user" ? "text-right" : "text-left"}
    >
      <div
        className={`inline-block px-3 py-2 rounded-lg text-sm max-w-[85%] ${
          m.from === "user"
            ? "bg-blue-600 text-white"
            : isDark
            ? "bg-[#2A2A2A] text-white"
            : "bg-gray-200 text-black"
        }`}
      >
        {m.text}
      </div>
    </div>
  ))}

  {/* ✅ BOT TYPING LOADER */}
  {loading && (
    <div className="text-left">
      <div
        className={`inline-block rounded-lg ${
          isDark ? "bg-[#2A2A2A]" : "bg-gray-200"
        }`}
      >
        <TypingLoader isDark={isDark} />
      </div>
    </div>
  )}
</div>


            <div
              className="p-3 border-t"
              style={{ borderTopColor: isDark ? "#333" : "#eee" }}
            >
              <div className="flex gap-2">
                <input
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  onKeyDown={(e) => e.key === "Enter" && sendMessage()}
                  placeholder="Type a message..."
                  className={`flex-1 px-3 py-2 rounded-lg border focus:outline-none ${
                    isDark
                      ? "bg-[#262626] border-[#404040] text-white"
                      : "bg-white border-[#E6E6E6] text-black"
                  }`}
                />
               <button
  onClick={sendMessage}
  disabled={loading}
  className={`px-3 py-2 rounded-lg text-white ${
    loading ? "bg-blue-400 cursor-not-allowed" : "bg-blue-600"
  }`}
>
  {loading ? "..." : "Send"}
</button>

              </div>
            </div>
          </div>
        )}

        <button
          onClick={() => setOpen((o) => !o)}
          className="w-14 h-14 rounded-full flex items-center justify-center shadow-lg bg-blue-600 text-white"
          aria-label="Open chat"
        >
          💬
        </button>
      </div>
    </div>
  );
}
