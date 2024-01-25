export interface Post {
  id: number;
  text: string;
  senderId: number;
  create_date: string;
  senderEmail: string;
  likes: number;
}

export interface orgpost {
  id: number;
  text: string;
  senderId: number;
  create_date: string;
  senderEmail: string;
  likes: number;
  isLiked: boolean;
}
