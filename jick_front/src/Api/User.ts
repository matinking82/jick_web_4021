import { UserProfile, profile, searchUserResponse } from "../interfaces/user";
import { API_URL } from "./Vars";

export const getUserProfile = async () => {
  let url = API_URL + "/user/get";
  let token = localStorage.getItem("token");
  let response = await fetch(url, {
    method: "GET",
    headers: {
      Authorization: "Bearer " + token,
    },
  });
  let json = await response.json();
  return json as profile;
};

export const updateUserProfile = async (data: profile) => {
  let url = API_URL + "/user/update";
  let dataJson = {
    username: data.username,
    full_name: data.full_name,
    age: data.age,
  };

  let token = localStorage.getItem("token");
  let response = await fetch(url, {
    method: "POST",
    headers: {
      Authorization: "Bearer " + token,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dataJson),
  });

  if (response.status === 200) {
    return true;
  } else {
    return false;
  }
};

export const searchUsers = async (query: string) => {
  let url = API_URL + "/user/search/" + query;

  let token = localStorage.getItem("token");
  let response = await fetch(url, {
    method: "POST",
    headers: {
      Authorization: "Bearer " + token,
      "Content-Type": "application/json",
    },
  });

  if (response.ok) {
    let res = (await response.json()) as searchUserResponse[];
    console.log(res);

    return res;
  }
};

export const followUser = async (username: string) => {
  let url = API_URL + "/user/Follow/" + username;

  let token = localStorage.getItem("token");

  let response = await fetch(url, {
    method: "POST",
    headers: {
      Authorization: "Bearer " + token,
    },
  });

  if (response.ok) {
    return true;
  } else {
    return false;
  }
};

export const unfollowUser = async (username: string) => {
  let url = API_URL + "/user/unFollow/" + username;

  let token = localStorage.getItem("token");

  let response = await fetch(url, {
    method: "POST",
    headers: {
      Authorization: "Bearer " + token,
    },
  });

  if (response.ok) {
    return true;
  } else {
    return false;
  }
};

export const followUserByEmail = async (email: string) => {
  let url = API_URL + "/user/eFollow/";

  let token = localStorage.getItem("token");

  let data = {
    email: email,
  };
  let jsondata = JSON.stringify(data);
  console.log(jsondata);
  
  let response = await fetch(url, {
    method: "POST",
    headers: {
      Authorization: "Bearer " + token,
      "Content-Type": "application/json",
    },
    body: jsondata,
  });

  if (response.ok) {
    return true;
  } else {
    return false;
  }
};

export const unfollowUserByEmail = async (email: string) => {
  let url = API_URL + "/user/eUnFollow/";

  let data = {
    email: email,
  };

  let token = localStorage.getItem("token");

  let response = await fetch(url, {
    method: "POST",
    headers: {
      Authorization: "Bearer " + token,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (response.ok) {
    return true;
  } else {
    return false;
  }
};

export const getUserProfileByUsername = async (email: string) => {
  let url = API_URL + "/user/get/" + email;
  let token = localStorage.getItem("token");
  let response = await fetch(url, {
    method: "GET",
    headers: {
      Authorization: "Bearer " + token,
    },
  });

  if (response.ok) {
    let res = (await response.json()) as UserProfile;
    console.log(res);

    return res;
  }
};
