import { useState } from 'react';

const Filter = () => {
    const [searchTerm, setSearchTerm] = useState('');

    const handleInputChange = (event) => {
        setSearchTerm(event.target.value);
    }

    return (
        <div>
            <input type="text" value={searchTerm} onChange={handleInputChange}/>
        </div>
    )
}

export default Filter;