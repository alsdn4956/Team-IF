import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import NavBar from './components/NavBar';
import LoginPage from './pages/LoginPage';
import StorePage from './pages/StorePage';
import BrandPage from './pages/BrandPage';
import ChatPage from './pages/ChatPage';
import MyPage from './pages/MyPage';
import FuserPage from './pages/FuserPage';
import SignUpPage from './pages/SignUpPage';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<LoginPage />} />
                <Route path="/signup" element={<SignUpPage />} />
                <Route path="/*" element={<DefaultLayout />} />
            </Routes>
        </Router>
    );
}

function DefaultLayout() {
    // 그라데이션 스타일을 정의합니다.
    const gradientStyle = {
        background: 'linear-gradient(to bottom, #6b6b6b, #ffffff)',
        minHeight: '100vh',
        padding: '20px'
    };

    return (
        <div style={gradientStyle}>
            <NavBar />
            <Routes>
                <Route path="/store" element={<StorePage />} />
                <Route path="/brand" element={<BrandPage />} />
                <Route path="/chat" element={<ChatPage />} />
                <Route path="/my" element={<MyPage />} />
                <Route path="/fuser" element={<FuserPage />} />
            </Routes>
        </div>
    );
}

export default App;
