import { useEffect, useState } from "react";
import { profile } from "../interfaces/user";
import { getUserProfile, updateUserProfile } from "../Api/User";
import NavBar from "../components/NavBar";
import MyPosts from "../components/MyPosts";

const Profile = () => {
  const [profile, setProfile]: [profile, any] = useState();

  useEffect(() => {
    getUserProfile().then((res) => {
      setProfile(res);
      console.log(res);
    });
  }, []);

  return (
    <>
      <NavBar />

      <div className="container">
        <div className="row">
          <div className="col-md-6 offset-md-3">
            <div className="card mt-5">
              <div className="card-body">
                <h2 className="card-title">Profile</h2>
                {profile && (
                  <>
                    <p>
                      Useruame:
                      <input
                        type="text"
                        className="form-control"
                        placeholder="Username"
                        value={profile.username}
                        onChange={(e) => {
                          profile.username = e.target.value;
                          setProfile(profile);
                        }}
                      ></input>
                    </p>
                    <p>
                      Email:
                      <input
                        type="text"
                        className="form-control"
                        placeholder="Email"
                        value={profile.email}
                      ></input>
                    </p>
                    <p>
                      Full Name:
                      <input
                        type="text"
                        className="form-control"
                        placeholder="Full Name"
                        value={profile.full_name}
                        onChange={(e) => {
                          profile.full_name = e.target.value;
                          setProfile(profile);
                        }}
                      ></input>
                    </p>
                    <p>
                      Age:
                      <input
                        type="number"
                        className="form-control"
                        placeholder="Age"
                        value={profile.age}
                        onChange={(e) => {
                          profile.age = parseInt(e.target.value);
                          setProfile(profile);
                        }}
                      ></input>
                    </p>
                    <p>Registered At: {profile.create_date}</p>

                    <button
                      className="btn btn-primary"
                      onClick={(e) => {
                        updateUserProfile(profile).then((res) => {
                          if (res) {
                            alert("Profile Updated");
                          } else {
                            alert("Profile Update Failed");
                          }
                        });
                      }}
                    >
                      Update
                    </button>
                  </>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>

      <MyPosts />
    </>
  );
};

export default Profile;
