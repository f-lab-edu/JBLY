import React from 'react';
import { UserOutlined } from '@ant-design/icons';
import { Avatar, Space } from 'antd';

const AvatarComponent = () => {

    return (
        <Space>
            <Avatar icon={<UserOutlined />} />
        </Space>
    )
}

export default AvatarComponent;
