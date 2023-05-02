import axios from "axios";
import React from "react";
import {useNavigate} from "react-router";
import ProductList from "./ProductList";

const ProductListPage = () => {
    const navigate = useNavigate();
    return (<>
            <div>
                <button onClick={() => {
                    axios.post('/api/logout')
                    navigate('/')
                }
                }>로그아웃
                </button>
            </div>
            <div>
                <h1>Product List</h1>
                <ProductList/>
            </div>
        </>
    );
}

export default ProductListPage;
