import React from 'react';
// import Comment from '../components/Comment';

const FilmList = ({ films }) => {
    const filmNodes = films.map(film => {
        return (
            <>
            <Film key={film.id} url={film.url}>
            </Film>
            </>
        )
    });
    return (
        <>
            {filmNodes}
        </>

    );
};

export default FilmList;