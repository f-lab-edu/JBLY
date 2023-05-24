import axios from "axios";
import React, {useEffect, useState} from "react";

const DeployTest = () => {
    const [data, setData] = useState({
        text:"",
    });

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get(
                    'http://localhost:8080/main/deploy-test');
                console.log(response.data);
                setData(response.data);
            } catch (error) {
                console.log('Error Fetching data : ', error);
            }
        };
        fetchData();
    }, []); // Rendering될 때 한 번만 실행됩니다.

    return (
        <div>
            <h1>Data from API : </h1>
            <ul>
                {data.text}
            </ul>
        </div>
    );
}

export default DeployTest
