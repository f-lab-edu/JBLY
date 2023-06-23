import React from "react";
import {useNavigate} from "react-router";
import LoginFrom from "./LoginForm";
import { Button, Space } from 'antd';
import DropdownComponent from "./footer/DropdownComponent";

const Home = () => {
    return (
        <div>
            <h1>현재 페이지는 Home 입니다.</h1>
            <DropdownComponent/>
        </div>
    );
};
export default Home;
