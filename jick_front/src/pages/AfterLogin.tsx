import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Logout from "./Logout";
import Home from "./Home";
import Profile from "./Profile";
import Search from "./Search";
import CreatePost from "./CreatePost";
import MyPosts from "../components/MyPosts";
import UserPosts from "./UserPosts";
import Explore from "./Explore";

const AfterLogin = () => {
  let router = createBrowserRouter([
    {
      path: "/",
      element: <Home />,
      //   loader: HomeLoader,
    },
    {
      path: "/logout",
      element: <Logout />,
    },
    {
      path: "*",
      element: <div>Not Found</div>,
    },
    {
      path: "/profile",
      element: <Profile />,
    },
    {
      path: "/search/:search",
      element: <Search />,
    },
    {
      path: "/post",
      element: <CreatePost />,
    },
    {
      path: "/posts/:email",
      element: <UserPosts />,
    },
    {
      path: "/explore",
      element: <Explore />,
    },
  ]);

  return (
    <React.StrictMode>
      <RouterProvider router={router} />
    </React.StrictMode>
  );
};

export default AfterLogin;
