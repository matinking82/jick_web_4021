import { useEffect, useState } from "react";
import { Post } from "../interfaces/post";
import { GetMyPosts } from "../Api/Posts";
import PostCard from "./PostCard";

const MyPosts = () => {
  const [posts, setPosts]: [Post[], any] = useState([]);

  let postsElement = <p>you dont have any posts yet</p>;

  if (posts.length > 0) {
    postsElement = (
      <div>
        {posts?.map((post: Post) => {
          return <PostCard post={post} />;
        })}
      </div>
    );
  }

  useEffect(() => {
    GetMyPosts().then((res) => {
      setPosts(res);
      console.log(res);
    });
  }, []);

  return (
    <div>
      <h1>My Posts:</h1>
      {postsElement}
    </div>
  );
};

export default MyPosts;
