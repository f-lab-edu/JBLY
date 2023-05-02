import "./App.css"
import {Route, Routes} from "react-router-dom";
import Home from "./component/Home";
import ProductListPage from "./component/page/ProductListPage";
import SignUpPage from "./component/page/SignUpPage";
import Header from "./component/Header";
import Footer from "./component/Footer";

const App = () => {
    return (
        <div>
            <Header/>
            <Routes>
                <Route path="/" element={<Home/>}></Route>
                <Route path="/signUp" element={<SignUpPage/>}></Route>
                <Route path="/productList" element={<ProductListPage/>}></Route>
            </Routes>
            <Footer/>
        </div>
    );
};

export default App;
