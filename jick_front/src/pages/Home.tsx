import { useEffect, useState } from "react";
import { GetHomePosts } from "../Api/Posts";
import { Post } from "../interfaces/post";
import PostCard from "../components/PostCard";
import NavBar from "../components/NavBar";

const Home = () => {
  const [posts, setPosts]: [Post[], any] = useState();

  useEffect(() => {
    GetHomePosts().then((res) => {
      setPosts(res);
      console.log(res);
    });
  }, []);

  return (
    <>
      <NavBar/>
      <div>
        <h1>Welcome to Jick web!!</h1>
        {posts?.map((post: Post) => {
          return <PostCard post={post} />;
        })}
      </div>
    </>
  );
};

export default Home;
