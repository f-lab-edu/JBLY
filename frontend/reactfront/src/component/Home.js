import React from "react";
import {useNavigate} from "react-router";
import LoginFrom from "./LoginForm";
import { Button, Space } from 'antd';

const Home = () => {
    const navigate = useNavigate();
    const navigateToSignUp = () => {
        navigate("/signUp");
    };

    return (
        <div>
            <LoginFrom/>
            <button id="button1" onClick={navigateToSignUp}>회원가입</button>
            <Button>Default Button</Button>
        </div>
    );
};
export default Home;
