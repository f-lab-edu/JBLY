import {useState, useEffect, useCallback} from 'react';
import axios from 'axios';
import Pagination from "./Pagination";
import {Image} from "@material-ui/icons";

const ProductList = () => {

    // console.log(props)
    const [products, setProducts] = useState([]);
    const [totalPage, setTotalPages] = useState(0);
    const [currentPage, setCurrentPage] = useState(1); // 상태 관리 hook, setter를 사용해 값을 세팅합니다.

    useEffect(() => {
        console.log(currentPage);
        axios.get(`http://localhost:8080/api/v1/product?page=${currentPage ?? 1}&size=10`)
            .then(response => {
                setProducts(response.data.data);
                setTotalPages(response.data.totalPage);
            })
            .catch(error => console.log(error));
    }, [totalPage, currentPage]);

    const handleClickPrevious = () => {
        if (currentPage > 1) {
            setCurrentPage(currentPage - 1);
        }
    };

    const handleClickNext = () => {
        if (currentPage < totalPage) {
            setCurrentPage(currentPage + 1);
        }
    };

    const getPageNumbers = ()=> {
        const pageNumbers = [];
        // 현재 페이지가 3이고 pageSize가 10이면, getPageNumbers 함수는 [21, 22, 23, 24, 25, 26, 27, 28, 29, 30] 배열을 반환합니다.
        for (let i = 1; i <= 10; i++) {
            const pageNumber = (currentPage - 1) * (10) + i;
            pageNumbers.push(pageNumber);
        }
        return pageNumbers;
    };

    return (

        <div>
            <table>
                <thead>
                <tr>
                    <th>상품 번호</th>
                    <th>판매처</th>
                    <th>상품이름</th>
                    <th>가격</th>
                    <th>상품 타입</th>
                    <th>이미지</th>
                    <th>판매처 번호</th>
                </tr>
                </thead>
                <tbody>
                {products.map(product => (
                    <tr key={product.id}>
                        <td >{product.id}</td>
                        <td>{product.shopName}</td>
                        <td>{product.productName}</td>
                        <td>{product.price}</td>
                        <td>{product.productType}</td>
                        <td><img src={product.productImage} style={{ width: '100px', height: '100px' }}/></td>
                        <td>{product.shopId}</td>
                    </tr>
                ))}
                </tbody>
            </table>
            <Pagination
                currentPage={currentPage}
                totalPages={totalPage}
                handleClickPrevious={handleClickPrevious}
                handleClickNext={handleClickNext}
                getPageNumbers={getPageNumbers}
                setCurrentPage={setCurrentPage}
            />
        </div>
    );
}

export default ProductList;
