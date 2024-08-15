import { useState } from 'react'
import './App.css'
import { Routes, Route } from 'react-router-dom'
import Chatbot from './pages/chatbot/chat-bot'
import Sidebar from './components/sidebar'

function App() {


  return (
    <div>
      <Sidebar />
      <main>
        <Routes>
          <Route path='/' element={<Chatbot />} />
          {/* //adding data route */}
        </Routes>
      </main>
    </div>
  )
}

export default App
