import React, {useState} from 'react';
import './PokemonDetail.css';

const PokemonDetail = ({pokemon}) => {

    return (
      <div className="pokemon-detail">
        Name: {pokemon.name.common}
        Abilities: {pokemon.name.abilities}
        Moves: {pokemon.name.moves}
        Habitat: {pokemon.name.habitat}
        Type: {pokemon.name.type}
        {/* <img src={pokemon.sprites.front_shiny}></img>
        <img src={pokemon.sprites.back_shiny}></img> */}
      </div>
    )
}
  
  export default PokemonDetail;