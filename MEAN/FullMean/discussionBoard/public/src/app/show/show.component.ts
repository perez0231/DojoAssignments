import { Component, OnInit } from '@angular/core';
import { Cookie } from 'ng2-cookies'
import { MessageService} from '../message.service'
import { Router } from "@angular/router"
import { ActivatedRoute } from "@angular/router";

@Component({
  selector: 'app-show',
  templateUrl: './show.component.html',
  styleUrls: ['./show.component.css']
})
export class ShowComponent implements OnInit {

  constructor(private _activatedRoute: ActivatedRoute, private _router: Router, private _messageService: MessageService) { }
question ={}
  ngOnInit() {
    this._messageService.show(this._activatedRoute.snapshot.params['id'])
    .then (data =>
    this.question = data)
    .catch(err => console.log(err))
  }

  likeanswer(id){
     this._messageService.likeanswer(id)
     .then(data=>{

     })
     .catch(err => console.log(err))
     this._messageService.show(this._activatedRoute.snapshot.params['id'])
     .then(data =>{
       this.question =data
     })
     .catch(err => console.log(err))
  }

}
