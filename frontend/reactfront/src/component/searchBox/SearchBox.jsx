import React from "react";
import "./SearchBox.css";
import { Input } from "antd";

const SearchBox = () => {
    const { Search } = Input;
    const onSearch = (value) => console.log(value);
    return (
        <div className={"search-box-styler"}>
            <Search style={{ width: 200 }} placeholder="검색어를 입력해 주세요" onSearch={onSearch} enterButton />
        </div>
    );
}

export default SearchBox;
