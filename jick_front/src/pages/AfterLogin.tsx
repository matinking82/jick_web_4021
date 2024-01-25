import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Logout from "./Logout";
import Home from "./Home";
import Profile from "./Profile";
import Search from "./Search";
import CreatePost from "./CreatePost";
import UserPosts from "./UserPosts";
import Explore from "./Explore";
import AdminHome from "./admin/Adminhome";
import AdminLogin from "./admin/AdminLogin";
import AdminLogout from "./admin/AdminLogout";
import AdminPosts from "./admin/AdminPosts";
import AdminUsers from "./admin/AdminUsers";

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
    {
      path: "/admin",
      element: <AdminHome />,
    },
    {
      path: "/admin/login",
      element: <AdminLogin />,
    },
    {
      path: "/admin/logout",
      element: <AdminLogout />,
    },
    {
      path: "/admin/posts/:page",
      element: <AdminPosts />,
    },
    {
      path: "/admin/users/:page",
      element: <AdminUsers />,
    },
  ]);

  return (
    <React.StrictMode>
      <RouterProvider router={router} />
    </React.StrictMode>
  );
};

export default AfterLogin;
