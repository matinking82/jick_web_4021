import { useEffect, useState } from "react";
import AdminNavBar from "../../components/admin/AdminNavBar";
import { stats } from "../../interfaces/stats";
import { getStatistics } from "../../Api/admin/stats";

const AdminHome = () => {
  if (localStorage.getItem("admintoken") === null) {
    window.location.href = "/admin/login";
  }

  const [stat, setStat] = useState<stats>({
    new_follows: 0,
    new_posts: 0,
    new_registers: 0,
    total_follows: 0,
    total_likes: 0,
    total_posts: 0,
    total_registers: 0,
  });

  useEffect(() => {
    getStatistics().then((res) => {
        if (res) {
            setStat(res);
        }
    });
  }, []);

  return (
    <>
      <AdminNavBar />
      <div>
        <h1>Welcome to the Admin Home Page</h1>
        <br />
        <br />
        <br />
        <h3>last month Stats:</h3>
        <p>New follows: {stat.new_follows}</p>
        <p>New posts: {stat.new_posts}</p>
        <p>New registers: {stat.new_registers}</p>

        <br />
        <br />
        <hr />
        <br />
        <h1>All time Stats:</h1>
        <p>Total follows: {stat.total_follows}</p>
        <p>Total likes: {stat.total_likes}</p>
        <p>Total posts: {stat.total_posts}</p>
        <p>Total registers: {stat.total_registers}</p>

      </div>
    </>
  );
};

export default AdminHome;
