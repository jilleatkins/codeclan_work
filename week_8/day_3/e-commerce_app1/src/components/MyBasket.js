import React from "react";
import ProductList from "./ProductList";
import ProductItem from "./ProductItem";

const MyBasket = ({basket}) => {
    const basketEntries = basket.map((product, index) => {
        return <li key={index}>{product.name}</li> 
    })
    

    return(
        <>
        <h2>My Basket</h2>
        <ul>
            {basketEntries}
        </ul>
        </>
    )
}

export default MyBasket;