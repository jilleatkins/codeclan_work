import Filter from "..components/Filter";
import StoryList from "..components/StoryList";


const HackerNews = () => {
    const storyData= [
        {
            title: "How not to code",
            url: "www.google.co.uk",
            by: "Jillybean"
        }
    ]

    useEffect(() => {
        fetch('https://hacker-news.firebaseio.com/v0/topstories.json')
    }, [])

    return (
        <>
            <Filter />
            <h1>Hacker Noobs</h1>
            <StoryList storyData={storyData} />
        </>
    )
}

export default HackerNews;