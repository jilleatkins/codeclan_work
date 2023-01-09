import React, {useState} from 'react';
import PokemonContainer from './containers/PokemonContainer.jsx';

function App() {
  const [pokemonName, setPokemonName] = useState("");

  return (
    <div className="wrapper">
      <h1>Pokemon Stats</h1>
      <PokemonContainer />
      <input type="text"
        onChange={(event) => {
          setPokemonName(event.target.value);
        }}
      />
      <br></br>
      <br></br>
      <button>Search Pokemon</button>
    </div>
  );
}

export default App;