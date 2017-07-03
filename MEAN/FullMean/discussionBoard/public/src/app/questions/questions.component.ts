import { Component, OnInit } from '@angular/core';
import { Cookie } from 'ng2-cookies'
import { MessageService} from '../message.service'
import { Router } from "@angular/router"

@Component({
  selector: 'app-questions',
  templateUrl: './questions.component.html',
  styleUrls: ['./questions.component.css']
})
export class QuestionsComponent implements OnInit {
  name= Cookie.get("name")
  question: any ={};
  allposts: any  = []

  constructor(private _router: Router, private _messageService: MessageService ) {
    console.log("in my constructor")




  }

  ngOnInit() {


  }

  mkQuestion(){
    this._messageService.mkQuestion(this.question)
    .then(data =>{
      console.log(this.question)
      this._router.navigateByUrl("allquestions")
    })
    .catch(err => console.log(err))
  }






}
