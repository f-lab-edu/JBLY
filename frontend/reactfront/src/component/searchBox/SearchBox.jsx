import React from "react";
import "./SearchBox.css";

const SearchBox = () => {
    return (
        <div className={"search-box-container"}>
            <input
                type={"text"}
                className={"search-box"}
                placeholder={"검색어를 입력해 주세요."}/>
            <button>검색</button>
        </div>
    );
}

export default SearchBox;
