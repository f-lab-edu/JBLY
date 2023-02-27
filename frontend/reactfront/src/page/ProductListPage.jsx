import React from "react";
import { useNavigate } from "react-router";
import ProductList from "../component/paging/ProductList";

const ProductListPage = () => {
    const navigate = useNavigate();
    return (<>
        <div>
            <button onClick={() => {navigate('/')}}>로그아웃</button>
        </div>
        <div>
            <h1>Product List</h1>
            <ProductList />
        </div></>
    );
}

export default ProductListPage;