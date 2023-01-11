import React, { useEffect, useState } from "react";
import StoryList from "../components/StoryList";
import Filter from "../components/Filter";

const MainContainer = () => {

    const [stories, setStories] = useState([]);
    const [filteredStories, setFilteredStories] = useState([]);

    useEffect(() => {
        fetch('https://hacker-news.firebaseio.com/v0/topstories.json')
            .then(res => res.json())
            .then((data) => {
                const copyStoryArray = [...data];
                const reducedStoryArray = copyStoryArray.splice(0, 10);
                const storyPromises = reducedStoryArray.map((id) => {
                    return fetch(`https://hacker-news.firebaseio.com/v0/item/${id}.json`).then((res) => res.json());
                });

                Promise.all(storyPromises)
                    .then((data) => {
                        setStories(data);
                    });
            });
    }, []);
   
    const filter = (searchTerm) => {
        const lowerSearch = searchTerm.toLowerCase();
        const filteredStories = stories.filter((story) => {
            return story.title.toLowerCase().includes(lowerSearch);
        });
        setFilteredStories(filteredStories);
    }

    return (
        <div>
            <Filter handleChange={filter} />
            <StoryList stories={filteredStories}  />
            <h1>Test</h1>
        </div>
    );

}

export default MainContainer;