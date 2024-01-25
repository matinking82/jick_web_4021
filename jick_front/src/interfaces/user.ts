export interface profile {
  id: number;
  username: string;
  email: string;
  full_name: string;
  age: number;
  create_date: string;
}

export interface searchUserResponse {
  username: string;
  full_name: string | null;
  email: string;
  create_date: string;
  isFollowing: boolean;
}

export interface UserProfile{
  username: string;
  email: string;
  full_name: string;
  create_date: string;
  isFollowing: boolean;
}

export interface user{
  id: number;
  username: string;
  email: string;
  full_name: string;
  age: number;
  create_date: string;
  is_active: boolean;
}