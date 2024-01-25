import React, { useEffect, useState } from "react";
import AdminNavBar from "../../components/admin/AdminNavBar";
import { user } from "../../interfaces/user";
import {
  ActivateUser,
  DeactivateUser,
  getAllUsers,
} from "../../Api/admin/AdminUser";
import { useParams } from "react-router-dom";

const AdminUsers: React.FC = () => {
  if (localStorage.getItem("admintoken") === null) {
    window.location.href = "/admin/login";
  }

  const { page } = useParams<{ page: string }>();

  if (page === undefined || isNaN(parseInt(page))) {
    window.location.href = "/admin/users/0";
  }
  let pageint = parseInt(page);

  const [users, setUsers] = useState<user[]>([]);

  useEffect(() => {
    getAllUsers(pageint).then((res) => {
      if (res) {
        setUsers(res);
        console.log(res);
      }
    });
  }, []);

  return (
    <>
      <AdminNavBar />
      <div>
        <h1>Manage Users:</h1>

        <table className="table table-bordered p-3">
          <thead>
            <tr>
              <th className="p-3">Username</th>
              <th className="p-3">Email</th>
              <th className="p-3">full Name</th>
              <th className="p-3">join date</th>
              <th className="p-3">Actions</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user) => {
              let btn = (
                <button
                  className="btn btn-danger"
                  onClick={(e) => {
                    DeactivateUser(user.id).then((res) => {
                      if (res) {
                        window.location.reload();
                      }
                    });
                  }}
                >
                  DeActivate
                </button>
              );
              if (!user.is_active) {
                btn = (
                  <button
                    className="btn btn-outline-primary"
                    onClick={(e) => {
                      ActivateUser(user.id).then((res) => {
                        if (res) {
                          window.location.reload();
                        }
                      });
                    }}
                  >
                    Activate
                  </button>
                );
              }
              return (
                <tr key={user.id}>
                  <td>{user.username}</td>
                  <td>{user.email}</td>
                  <td>{user.full_name}</td>
                  <td>{user.create_date}</td>
                  <td>{btn}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
        <button
          className="btn btn-primary"
          onClick={() => {
            if (pageint > 0) {
              window.location.href = "/admin/users/" + (pageint - 1);
            }
          }}
        >
          Previous page
        </button>
        <button
          className="btn btn-primary"
          onClick={() => {
            window.location.href = "/admin/users/" + (pageint + 1);
          }}
        >
          next page
        </button>
      </div>
    </>
  );
};

export default AdminUsers;
