import React, { useState } from 'react';

const CommentForm = ({ onCommentSubmit }) => {
    const [author, setAuthor] = useState('');
    const [text, setText] = useState('');

    const handleAuthorChange = (event) => {
        setAuthor(event.target.value);
    };

    const handleTextChange = (event) => {
        setText(event.target.value);
    };

    const handleFormSubmit = (event) => {
        event.preventDefault();
        const authorToSubmit = author.trim();
        const textToSubmit = text.trim();

        if (!authorToSubmit || !textToSubmit) {
            return;
        }

    onCommentSubmit({
            author: authorToSubmit,
            text: textToSubmit
        });

    setAuthor('');
    setText('');
    }

    return (
        <form onSubmit={handleFormSubmit}>
            <label>Your name: </label>
            <input
                id="author-field"
                value={author}
                type="text"
                onChange={handleAuthorChange}
            />
            <br></br>
            <label>Your comment: </label>
            <input
                id="text-field"
                text={text}
                type="text"
                onChange={handleTextChange}
            />
            <br></br>
            <div className="post-comment">
                <input type="submit" value="Post comment" />
            </div>
        </form>
    )
}

export default CommentForm;