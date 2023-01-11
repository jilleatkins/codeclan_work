import React from "react";
import Story from "./Story";

const StoryList = ({ stories }) => {
    const storyList = stories.map((story, index) => {
        return (<Story key={index} details={story} position={index + 1} />);
    });
    return (
        <>
            <ul>
                {storyList}
            </ul>
        </>
    );
}
export default StoryList;