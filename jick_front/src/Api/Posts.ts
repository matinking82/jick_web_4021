import { API_URL } from "./Vars";
import {Post} from "../interfaces/post";

export const GetHomePosts = async () => {
    let url = API_URL + "/post/all";
    let token = localStorage.getItem('token');
    let response = await fetch(url, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
    });

    if (response.ok) {
        return await response.json() as Post[];
    }
}