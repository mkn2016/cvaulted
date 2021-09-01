import {Roles} from "../classes/roles";
import {Entity} from "@/interfaces/entity"

export class User implements Entity{
    id: number
    username: string;
    email: string;
    roles: Roles[]

    constructor(id:number=0, username:string="", email:string="", roles:Roles[]) {
        this.id = id;
        this.username = username;
        this.email = email;
        this.roles = roles;

    }
}