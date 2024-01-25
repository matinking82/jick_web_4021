import { useEffect, useState } from "react";
import { Post } from "../interfaces/post";
import PostCard from "../components/PostCard";
import { GetExplorePosts } from "../Api/Posts";
import NavBar from "../components/NavBar";

const Explore = () => {
  const [posts, setPosts] = useState<Post[]>([]);
  useEffect(() => {
    GetExplorePosts().then((res) => {
      setPosts(res);
      console.log(res);
    });
  }, []);

  return (
    <>
      <NavBar />
      <div>
        <h1>Explore New Posts</h1>
        <h3>Here are some recently added posts to explore..</h3>
        {posts.map((post: Post) => {
          return <PostCard post={post} />;
        })}
      </div>
    </>
  );
};

export default Explore;
