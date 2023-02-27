import {useEffect, useState} from "react";

function Pagination({currentPage, totalPages, handleClickPrevious, handleClickNext, getPageNumbers, setCurrentPage}) {

    // const [currentPgae, setCurrentPage] = useState(1);
    console.log(getPageNumbers())

    return (
        <div>
            <button onClick={handleClickPrevious}>이전</button>
            {getPageNumbers().map(pageNumber => (
                <button key={pageNumber} onClick={() => setCurrentPage(pageNumber)}>
                    {pageNumber}
                </button>
            ))}
            <button onClick={handleClickNext}>다음</button>
        </div>
    );
}

export default Pagination;
