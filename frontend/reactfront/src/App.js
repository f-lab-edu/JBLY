import { Route, Routes } from "react-router-dom";
import Home from "./component/Home";
import ProductListPage from "./component/ProductListPage";
import SignUpPage from "./page/SignUpPage";

const App = () => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/signUp" element={<SignUpPage />}></Route>
        <Route path="/productList" element={<ProductListPage />}></Route>
      </Routes>
    </div>
  );
};

export default App;