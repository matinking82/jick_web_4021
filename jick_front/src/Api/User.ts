import { profile } from "../interfaces/user";
import { API_URL } from "./Vars";

export const getUserProfile = async () => {
    let url = API_URL + "/user/get";
    let token = localStorage.getItem("token");
    let response = await fetch(url, {
        method: "GET",
        headers: {
            "Authorization": "Bearer " + token
        }
    });
    let json = await response.json();
    return json as profile;
};

export const updateUserProfile = async (data: profile) => {
    let url = API_URL + "/user/update";
    let dataJson = {
        username: data.username,
        full_name: data.full_name,
        age: data.age
    };

    let token = localStorage.getItem("token");
    let response = await fetch(url, {
        method: "POST",
        headers: {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dataJson)
    });

    if (response.status === 200) {
        return true;
    } else {
        return false;
    }
};