export interface Author {
    id: number;
    name: string;
}

export interface Category {
    id: number;
    name: string;
}

export interface Book {
    id: number;
    title: string;
    author: Author;
    category: Category;
    price: string;
    description: string;
    cover_image: string; // URL from Cloudinary
    created_at: string;
}
