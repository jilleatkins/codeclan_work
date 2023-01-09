import React, { useEffect, useState } from 'react';
import PokemonSelector from '../components/PokemonSelector';
import PokemonDetail from '../components/PokemonDetail';

const PokemonContainer = () => {
    const [pokemon, setPokemon] = useState([]);
    const [selectedPokemon, setSelectedPokemon] = useState(null);

    useEffect(() => {
      getPokemon();
    }, [])

    const getPokemon = function(){
        fetch('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
        .then(res => res.json())
        .then(pokemon => setPokemon(pokemon.results))
    }

    const getSpecificPokemon = function(pokemon){
        fetch('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0' + pokemon.name)
        .then(res => res.json())
        .then(pokemon => setSelectedPokemon(pokemon))
    }

    const onPokemonSelected = function(pokemon){
        getSpecificPokemon(pokemon)
    }



    // return (
    //     <div className="main-container">
    //         <PokemonSelector pokemon={pokemon} onPokemonSelected={onPokemonSelected} />
    //         {selectedPokemon ? <PokemonDetail pokemon={selectedPokemon}/> : null}
    //     </div>
    // )
}

export default PokemonContainer;