import {React, useState, useEffect} from "react";
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import ProductList from "../components/ProductList";
import NavBar from "../components/NavBar";
import MyBasket from "../components/MyBasket";
import Home from "../components/Home";


const Bakery = () => {

    const productData = [
        {id: 0, name: "Chocolate Muffin", price: "£2"},
        {id: 1, name: "Vanilla Cupcake", price: "£2.50"},
        {id:2, name: "Chocolate Chip Cookie", price: "£1"}
    ];

    const userData = [{id:0, name: "Jim"}]


    const [user, setUser] = useState(userData);
    const [basket, setBasket] = useState([]);

    const add = (product) => {
        const copyBasket = [...basket, product]
        setBasket(copyBasket)
    }

    return (
        <Router>
            <NavBar/>
            <Routes>
                <Route path="/" element={ <Home /> } />
                <Route path="/products" element={ <ProductList productData={productData} add={add}/> } />
                <Route path="/mybasket" element={ <MyBasket basket={basket} /> } />
            </Routes>
        </Router>
    )
};

export default Bakery;
