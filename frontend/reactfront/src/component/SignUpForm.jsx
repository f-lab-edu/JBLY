import React, { useState } from "react";
import axios from "axios";

const SignUpForm = () => {
    const [values, setValues] = useState({
        userId: "",
        password: "",
        name: "",
        phone: "",
        email: "",
        address: "",
    })


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
        axios.post('/api/users', {
            userId: values.userId,
            password: values.password,
            name: values.name,
            phone: values.phone,
            email: values.email,
            address: values.address
        }
        )
    }

    return (
        <div>
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
                name
                <input
                    type="text"
                    name="name"
                    value={values.name}
                    onChange={handleChange}
                />
                phone
                <input
                    type="text"
                    name="phone"
                    value={values.phone}
                    onChange={handleChange}
                />
                email
                <input
                    type="text"
                    name="email"
                    value={values.email}
                    onChange={handleChange}
                />
                address
                <input
                    type="text"
                    name="address"
                    value={values.address}
                    onChange={handleChange}
                />
                <button type="submit">회원가입</button>
            </form>
        </div>
    )


}

export default SignUpForm;
