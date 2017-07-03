import { Component, OnInit } from '@angular/core';
import {BattleService} from '../battle.service'
import { NgModule } from '@angular/core';
import { Router } from '@angular/router';


@Component({
  selector: 'app-battle',
  templateUrl: './battle.component.html',
  styleUrls: ['./battle.component.css']
})
export class BattleComponent implements OnInit {
  user1:any = {};
  user2:any = {};
  username= "";
  users:any = [];
  score: number = 0;
//Score = (# of Public Repos + # of Followers) * 12.
  usersarray= [{username:"jimmymixer", publicRepos:5, followers:8},{username:"minh", publicRepos:6, followers:2}]

  constructor(private _battleService: BattleService) {
        this._battleService.new()

  }
  ngOnInit() {
  }

  OnSubmit1(){
    console.log(this.user1)
    console.log("onSubmit fun")
    this._battleService.gitScore(this.user1.login)
    .then( user => {
    this.addUser(user, 0)
    console.log(user)})

    .catch(err => console.log(err))


    // this.users.push(this.usersarray[0])
    // this.users[0] = this.usersarray[0]
  }

    OnSubmit2(){
      console.log(this.user2)
      console.log("onSubmit fun2")
      this._battleService.gitScore(this.user2.login)
      .then( user => {
      this.addUser(user, 1)
      console.log(user)})


      // this.users.push(this.usersarray[1])
      // this.users[1] = this.usersarray[1]


    }

    addUser(user, i){
      console.log(user)
      user.score = user.followers + user.public_repos;
      user.img= user.avatar_url
      console.log(user.score)
      console.log(user)
      this._battleService.create(user)
      .then( user => {this.users[i] = user
        console.log(this.users)})
      .catch(err => console.log(err))
    }






}
