import React, { useEffect } from "react";
import AdminNavBar from "../../components/admin/AdminNavBar";
import { Post } from "../../interfaces/post";
import { useParams } from "react-router-dom";
import { deletePost, getAllPosts } from "../../Api/admin/AdminPost";

const AdminPosts: React.FC = () => {
  if (localStorage.getItem("admintoken") === null) {
    window.location.href = "/admin/login";
  }
  const [posts, setPosts] = React.useState<Post[]>([]);

  const { page } = useParams<{ page: string }>();

  if (page === undefined || isNaN(parseInt(page))) {
    window.location.href = "/admin/posts/0";
  }
  let pageint = parseInt(page);

  useEffect(() => {
    getAllPosts(pageint).then((res) => {
      if (res) {
        setPosts(res);
        console.log(res);
      }
    });
  }, []);
  return (
    <>
      <AdminNavBar />
      <div>Manage Posts:</div>
      <table className="table table-bordered p-3">
        <thead>
          <tr>
            <th className="p-3">sender</th>
            <th className="p-3">text</th>
            <th className="p-3">likes</th>
            <th className="p-3">Date</th>
            <th className="p-3">Actions</th>
          </tr>
        </thead>
        <tbody>
          {posts.map((post) => {
            return (
              <tr>
                <td className="p-3">{post.senderEmail}</td>
                <td className="p-3">{post.text}</td>
                <td className="p-3">{post.likes}</td>
                <td className="p-3">{post.create_date}</td>
                <td className="p-3">
                    <button className="btn btn-outline-danger" onClick={e=>{
                        deletePost(post.id).then(res=>{
                            if(res){
                                window.location.reload();
                            }
                        })
                    }}>delete</button>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
      <button
        className="btn btn-primary"
        onClick={() => {
          if (pageint > 0) {
            window.location.href = "/admin/posts/" + (pageint - 1);
          }
        }}
      >
        Previous page
      </button>
      <button
        className="btn btn-primary"
        onClick={() => {
          window.location.href = "/admin/posts/" + (pageint + 1);
        }}
      >
        next page
      </button>
    </>
  );
};

export default AdminPosts;
