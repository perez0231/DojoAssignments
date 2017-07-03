import { Component, OnInit } from '@angular/core';
import {BattleService} from '../battle.service'
import { NgModule } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent implements OnInit {
  users: any = []
  score= 0;
  constructor(private _battleService: BattleService) { }

  ngOnInit() {
    this.users= this._battleService.battle()
  }



}
