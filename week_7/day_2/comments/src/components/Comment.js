import React from 'react';

const Comment = ({ author , children }) => {
    return (
        <>
        <p>Posted by <b>{author}:</b></p>
        <p><i>{children}</i></p>
        <br></br>
        </>
    );
};

export default Comment;