import React, { useState } from 'react';
import CommentList from '../components/CommentList';
import CommentForm from '../components/CommentForm';

const CommentBox = () => {
    const [comments, setComments] = useState([
        {
            id: 1,
            author: 'R. Henry',
            text: 'I hate old peoples!'
        },
        {
            id: 2,
            author: 'colleen',
            text: 'my dog farts that stinks like sprouts. wat do I do pleae help me'
        },
        {
            id: 3,
            author: 'keith1947',
            text: 'is it possible for i am to be PREGANANANT?'
        }

    ]);

    const addComment = (submittedComment) => {
        submittedComment.id = Date.now();
        const copyComments = [...comments, submittedComment];
        setComments(copyComments);
    }

        return (
            <>
            <h1>Comments</h1>
            <CommentList comments={comments} />
            <h3>Add a comment</h3>
            <CommentForm onCommentSubmit={addComment}/>
            </>
        );
};

export default CommentBox;