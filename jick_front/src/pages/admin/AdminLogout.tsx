const AdminLogout = () => {
    localStorage.removeItem('admintoken');
    window.location.href = '/admin/login';

    return (
        <div>
            <h1>Admin Logout</h1>
        </div>
    );
};

export default AdminLogout;
