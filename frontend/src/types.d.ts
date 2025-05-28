export interface Book {
    id: number;
    title: string;
    author: {
        id: number;
        name: string;
    };
    category: {
        id: number;
        name: string;
    };
    price: string;
    description: string;
    cover_image: string;
}
