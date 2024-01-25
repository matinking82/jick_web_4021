import { useEffect, useState } from "react";
import { GetHomePosts } from "../Api/Posts";
import { Post } from "../interfaces/post";

const Home = () => {
  const [posts, setPosts]: [Post[], any] = useState();

  useEffect(() => {
    GetHomePosts().then((res) => {
      setPosts(res);
      console.log(res);
    });
  }, []);

  return (
    <div>
      <h1>Welcome to the Home page!</h1>
      {posts?.map((post: Post) => {
        return (
          <div key={post.id}>
            <h3>{post.text}</h3>
            <p>{post.create_date}</p>
          </div>
        );
      })}
    </div>
  );
};

export default Home;
