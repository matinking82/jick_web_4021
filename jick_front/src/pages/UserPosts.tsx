import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Post } from "../interfaces/post";
import PostCard from "../components/PostCard";
import { GetPostsForUser } from "../Api/Posts";
import NavBar from "../components/NavBar";
import { UserProfile } from "../interfaces/user";
import {
  followUser,
  followUserByEmail,
  getUserProfileByUsername,
  unfollowUser,
  unfollowUserByEmail,
} from "../Api/User";

const UserPosts = () => {
  const { email } = useParams<{ email: string }>();
  const [posts, setPosts]: [Post[], any] = useState(null);
  const [profile, setProfile]: [UserProfile, any] = useState(null);

  let element = <h1> User not found </h1>;

  let profileElement = <></>;

  if (posts) {
    if (posts.length > 0) {
      element = (
        <div>
          {posts?.map((post: Post) => {
            return <PostCard post={post} />;
          })}
        </div>
      );
    } else {
      element = <h1> User has no posts </h1>;
    }
  }

  if (profile) {
    let follow = (
      <button
        className="btn btn-outline-primary"
        onClick={() => {
          followUserByEmail(profile.email).then((res) => {
            if (res) {
              window.location.reload();
            }
          });
        }}
      >
        Follow
      </button>
    );
    if (profile.isFollowing) {
      follow = (
        <button
          className="btn btn-primary"
          onClick={() => {
            unfollowUserByEmail(profile.email).then((res) => {
              if (res) {
                window.location.reload();
              }
            });
          }}
        >
          Unfollow
        </button>
      );
    }

    profileElement = (
      <div className="user-profile-card">
        <h4>username: {profile.username}</h4>
        <p>email: {profile.email}</p>
        <p>full name: {profile.full_name}</p>
        <span>joined at: {profile.create_date}</span>
        <br />
        {follow}
      </div>
    );
  }

  useEffect(() => {
    GetPostsForUser(email).then((res) => {
      setPosts(res);
      console.log(res);
    });

    getUserProfileByUsername(email).then((res) => {
      setProfile(res);
      console.log(res);
    });
  }, []);

  return (
    <>
      <NavBar />
      <div>
        {profileElement}
        <br />
        <h1>Posts for {email}</h1>
        {element}
      </div>
    </>
  );
};

export default UserPosts;
