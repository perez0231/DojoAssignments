export class User {

    constructor(
      public id: number = null,
      public fname: string = "",
      public lname: string = "",
      public email: string = "",
      public password: string = "",
      public address: string = "",
      public unit: string = "",
      public state: string = "",
      public lucky: boolean = true,
      public created_at: Date = new Date(),
      public updated_at: Date = new Date()
    ){}
  }
