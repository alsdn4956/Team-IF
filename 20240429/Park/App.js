import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import NavBar from './components/NavBar';
import LoginPage from './pages/LoginPage';
import StorePage from './pages/StorePage';
import BrandPage from './pages/BrandPage';
import ChatPage from './pages/ChatPage';
import MyPage from './pages/MyPage';
import FuserPage from './pages/FuserPage';

function App() {
    return (
        <Router>
            <div>
                <Routes>
                    <Route path="/" element={<LoginPage />} />
                    <Route path="/store" element={<PageWithNavBar pageComponent={<StorePage />} />} />
                    <Route path="/brand" element={<PageWithNavBar pageComponent={<BrandPage />} />} />
                    <Route path="/chat" element={<PageWithNavBar pageComponent={<ChatPage />} />} />
                    <Route path="/my" element={<PageWithNavBar pageComponent={<MyPage />} />} />
                    <Route path="/fuser" element={<PageWithNavBar pageComponent={<FuserPage />} />} />
                </Routes>
            </div>
        </Router>
    );
}

function PageWithNavBar({ pageComponent }) {
    return (
        <>
            <NavBar />
            {pageComponent}
        </>
    );
}

export default App;
