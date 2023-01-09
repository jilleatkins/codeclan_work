import React from 'react';
import ListItem from './ListItem';

const PokemonList = ({pokemon, onPokemonClicked}) => {

    const pokemonItems = pokemon.map((pokemon, index) => {
      return <ListItem pokemon={pokemon} key={index} onPokemonClicked={onPokemonClicked}/>
    })

  return (
    <div>
    <ul>
      {pokemonItems}
    </ul>
  </div>
  )
}

export default PokemonList;