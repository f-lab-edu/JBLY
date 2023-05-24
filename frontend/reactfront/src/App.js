import "./App.css"
import {Route, Routes} from "react-router-dom";
import Home from "./component/Home";
import ProductListPage from "./component/page/ProductListPage";
import SignUpPage from "./component/page/SignUpPage";
import Header from "./component/header/Header";
import Footer from "./component/footer/Footer";
import SearchBox from "./component/searchBox/SearchBox";
import DeployTest from "./component/DeployTest";

const App = () => {
    return (
        <div>
            <Header/>
            <SearchBox/>
            <Routes>
                <Route path="/" element={<Home/>}></Route>
                <Route path="/signUp" element={<SignUpPage/>}></Route>
                <Route path="/productList" element={<ProductListPage/>}></Route>
                <Route path="/deploy-test" element={<DeployTest/>}></Route>
            </Routes>
            <Footer/>
        </div>
    );
};

export default App;
