import React from 'react';

const Film = ({ name , url }) => {
    return (
        <>
        <p>{name}</p>
        <p>{url}</p>
        </>
    );
};

export default Film;