
const Logout = () => {
    //logout
    localStorage.removeItem("token");
    
    //go to /
    window.location.href = "/";

    return <></>;
};

export default Logout;
