import { API_URL } from "../Vars";


export const AdminLoginService = async (username: string, password: string) => {
    let url = API_URL + "/admin/login";
    let data = {
        username: username,
        password: password,
    };
    let response = await fetch(url, {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });
    
    if (response.ok) {
        return await response.json();
    }
};