import { Entity } from "@/interfaces/entity";

export class Roles implements Entity{
    id: number;
    name: string;

    constructor(id:number = 0, name:string="") {
        this.id = id;
        this.name = name;
    }
}