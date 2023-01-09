const OptionItem = ({index, pokemon}) => {
    return <option value={index}>{pokemon.name}</option>
}

export default OptionItem;