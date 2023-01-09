import React from 'react';
import './ListItem.css';

const ListItem = ({pokemon, onPokemonClicked}) => {

  const handleClick = function() {
    console.log(`Clicked on ${pokemon.name}`);
    onPokemonClicked(pokemon);
  }

  return (
    <li onClick={handleClick} className="clickable-li">{pokemon.name}</li>
  )
}

export default ListItem;