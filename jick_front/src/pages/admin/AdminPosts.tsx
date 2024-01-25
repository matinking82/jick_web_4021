import React from "react";
import AdminNavBar from "../../components/admin/AdminNavBar";

const AdminPosts: React.FC = () => {
  if (localStorage.getItem("admintoken") === null) {
    window.location.href = "/admin/login";
  }

  return (
    <>
      <AdminNavBar />
      <div>posts</div>;
    </>
  );
};

export default AdminPosts;
