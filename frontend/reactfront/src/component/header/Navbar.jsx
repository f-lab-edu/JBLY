import React, { useState } from 'react';
import { Avatar, Menu, Dropdown } from 'antd';
import {UserOutlined} from "@ant-design/icons";

const Navbar = () => {
  const [isMenuVisible, setMenuVisible] = useState(false);

  const handleAvatarClick = () => {
    setMenuVisible(!isMenuVisible);
  };

  const handleMenuClick = ({ key }) => {
    // 메뉴 항목 클릭 이벤트 처리
    // 예: 다른 페이지로 이동하거나 기능 수행
    console.log('Clicked menu item:', key);
  };

  const menu = (
    <Menu onClick={handleMenuClick}>
      <Menu.Item key="1">메뉴 항목 1</Menu.Item>
      <Menu.Item key="2">메뉴 항목 2</Menu.Item>
      <Menu.Item key="3">메뉴 항목 3</Menu.Item>
    </Menu>
  );

  return (
    <div>
      <Dropdown overlay={menu} visible={isMenuVisible} onVisibleChange={setMenuVisible}>
        <Avatar icon={<UserOutlined />} onClick={handleAvatarClick} />
      </Dropdown>
    </div>
  );
};

export default Navbar;
