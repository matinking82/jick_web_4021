import React from "react";
import AdminNavBar from "../../components/admin/AdminNavBar";

const AdminUsers: React.FC = () => {
  if (localStorage.getItem("admintoken") === null) {
    window.location.href = "/admin/login";
  }

  return (
    <>
      <AdminNavBar />
      <div>
        <h1>Admin Users</h1>
      </div>
    </>
  );
};

export default AdminUsers;
