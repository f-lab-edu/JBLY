import React from "react";
import {useNavigate} from "react-router";
import LoginFrom from "./LoginForm";

const Home = () => {
    const navigate = useNavigate();
    const navigateToSignUp = () => {
        navigate("/signUp");
    };

    return (
        <div>
            <h1>JBLY</h1>
            <p>BY. SJ, YS</p>
            <LoginFrom/>
            <button id="button1" onClick={navigateToSignUp}>회원가입</button>

        </div>
    );
};
export default Home;
