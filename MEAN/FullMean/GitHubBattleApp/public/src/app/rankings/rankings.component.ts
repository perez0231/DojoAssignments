import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router"
import {BattleService}  from "../battle.service";
@Component({
  selector: 'app-rankings',
  templateUrl: './rankings.component.html',
  styleUrls: ['./rankings.component.css']
})
export class RankingsComponent implements OnInit {
  users: any = []
  score= 0;
  constructor(private _battleService: BattleService,
    private _router: Router) { }

  ngOnInit() {
  this._battleService.rankings()
    .then(users =>{
      console.log(users)
      this.users= users.sort((x,y) => y.score- x.score)
    })

    .catch(err => console.log(err))





  }

}
