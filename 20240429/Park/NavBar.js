import React from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
// 이미지 파일을 import 합니다.
import loginIcon from './image/로그인.png';
import storeIcon from './image/스토어.png';
import brandIcon from './image/브랜드.png';
import chatIcon from './image/채팅.png';
import myIcon from './image/MY.png';
import fuserIcon from './image/Fuser.png';

function NavBar() {
    return (
        <nav>
            <ul style={{ listStyleType: 'none', padding: 0, display: 'flex', justifyContent: 'flex-end' }}>
                <li><Link to ="/login"><img src={loginIcon} alt="Login" /></Link></li>
                <li><Link to="/store"><img src={storeIcon} alt="Store" /></Link></li>
                <li><Link to="/brand"><img src={brandIcon} alt="Brand" /></Link></li>
                <li><Link to="/chat"><img src={chatIcon} alt="Chat" /></Link></li>
                <li><Link to="/my"><img src={myIcon} alt="My Page" /></Link></li>
                <li><Link to="/fuser"><img src={fuserIcon} alt="Fuser" /></Link></li>
            </ul>
        </nav>
    );
}

export default NavBar;
