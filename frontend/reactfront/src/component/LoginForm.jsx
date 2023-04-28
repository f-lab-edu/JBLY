import React, {useState} from "react";
import axios from "axios";
import {useNavigate} from "react-router";

const SignUpForm = () => {
    const [values, setValues] = useState({
        userId: "",
        password: ""
    })

    const [login, setLogin] = useState(false);

    const navigate = useNavigate();
    const navigateToProductList = () => {
        navigate("/productList");
    };

    const handleChange = e => {
        setValues({
            ...values,
            [e.target.name]: e.target.value,
        })
    }

    const handleSubmit = e => { // submit 버튼이 눌러졌을 때 호출되는 함수
        e.preventDefault()
        console.log(values)
        console.log(e)
        axios.post('/api/login', {
            userId: values.userId,
            password: values.password
        }).then(() => {
            navigateToProductList()
        }).catch(() => {
            setLogin(true)
            console.log("error @@@")
        })

    }

    return (
        <div id="loginform">
            <form onSubmit={handleSubmit}>
                id
                <input
                    type="text"
                    name="userId"
                    value={values.userId}
                    onChange={handleChange}
                />
                pw
                <input
                    type="password"
                    name="password"
                    value={values.password}
                    onChange={handleChange}
                />
                <button type="submit">로그인</button>
            </form>
            {login && <div> 로그인 실패 </div>}
        </div>
    )

}

export default SignUpForm;
