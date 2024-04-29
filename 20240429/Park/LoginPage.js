import React from 'react';
import NavBar from '../components/NavBar';
import backgroundImage from '../components/image/LoginBackground.png'; // 배경 이미지 import

function LoginPage() {
    return (
        <div style={{
            backgroundImage: `url(${backgroundImage})`,
            backgroundSize: 'cover', // 배경 이미지를 커버 모드로 설정
            backgroundPosition: 'center', // 배경 이미지를 중앙에 위치
            height: '100vh', // 전체 높이
            width: '100vw' // 전체 너비
        }}>
            <NavBar />
            <div style={{ marginTop: '50px', display: 'flex', justifyContent: 'center', alignItems: 'center', height: '90vh' }}>
                <form style={{ width: '300px', border: '1px solid #ccc', padding: '40px', borderRadius: '10px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}>
                    <div style={{ marginBottom: '20px' }}>
                        <label htmlFor="username" style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>사용자 이름</label>
                        <input type="text" id="username" name="username" style={{ width: '100%', padding: '10px', border: '1px solid #ccc', borderRadius: '5px' }} />
                    </div>
                    <div style={{ marginBottom: '20px' }}>
                        <label htmlFor="password" style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>비밀번호</label>
                        <input type="password" id="password" name="password" style={{ width: '100%', padding: '10px', border: '1px solid #ccc', borderRadius: '5px' }} />
                    </div>
                    <button type="submit" style={{ width: '100%', padding: '10px', backgroundColor: 'navy', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }}>로그인</button>
                </form>
            </div>
        </div>
    );
}

export default LoginPage;
