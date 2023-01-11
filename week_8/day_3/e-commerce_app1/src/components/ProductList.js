import React from "react";
import NavBar from "./NavBar";
import ProductItem from "./ProductItem";

const ProductList = ({productData, add}) => {

    const productEntries = productData.map((product, index) => {
        return <li key={index} ><ProductItem product={product} add={add}/></li> 
});

    return (
                <>
                    <h3>Products</h3>
                    <ul>
                        {productEntries}
                    </ul>
                </>
    )
};

export default ProductList;