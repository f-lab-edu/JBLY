import React, { useState } from 'react';
import { DownOutlined } from '@ant-design/icons';
import { Space, Dropdown, Menu } from 'antd';

const DropdownComponent = () => {
    const handleMenuItemClick = (e) => {
        console.log('Clicked menu item:', e.key);
    };

    const items = [
        {
            label: '1st menu item',
            key: '0',
        },
        {
            label: '두 번째',
            key: '1',
        },
        {
            type: 'divider',
        },
        {
            label: '3rd menu item',
            key: '3',
        },
    ];

    const menu = (
        <Menu onClick={handleMenuItemClick}>
            {items.map((item) => (
                <Menu.Item key={item.key}>{item.label}</Menu.Item>
            ))}
        </Menu>
    );

    return (
        <Dropdown overlay={menu} visible={true}>
            <a onClick={(e) => e.preventDefault()}>
                <Space>
                    <DownOutlined />
                </Space>
            </a>
        </Dropdown>
    );
};


export default DropdownComponent;
