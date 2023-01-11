import React from "react";

const ProductItem = ({product, add}) => {
    return (
        <>
            <h4>{product.name}</h4>
            <p>{product.price}</p>
            <button onClick={() => add(product)}>Add to basket</button>
        </>
    )
};

export default ProductItem;