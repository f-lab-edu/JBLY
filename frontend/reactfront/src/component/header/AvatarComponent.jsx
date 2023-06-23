import React, { useState } from 'react';
import {Avatar, Space} from "antd";
import {UserOutlined} from "@ant-design/icons";
import DropdownComponent from "./DropdownComponent";

const AvatarComponent = () => {
    const [dropdownVisible, setDropdownVisible] = useState(false);

    const handleAvatarClick = () => {
        setDropdownVisible(!dropdownVisible);
    };

    return (
        <Space>
            <Avatar icon={<UserOutlined />} />
        </Space>
    );
};

export default AvatarComponent;
