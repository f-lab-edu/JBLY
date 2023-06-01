import axios from "axios";
import React, {useEffect, useState} from "react";

const DeployTest = () => {
    const [data, setData] = useState({
        text:"",
    });

    useEffect(() => {
        const fetchData = async () => {
            try {
                console.log('DeployTest는 호출되었습니다.');
                const response = await axios.get(
                    process.env.REACT_APP_API_URL + '/main/deploy-test');
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
