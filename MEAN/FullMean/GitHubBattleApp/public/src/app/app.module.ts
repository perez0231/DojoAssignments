import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {FormsModule} from '@angular/forms'
import {BattleService} from './battle.service';
import {HttpModule} from '@angular/http'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BattleComponent } from './battle/battle.component';
import { ResultsComponent } from './results/results.component';
import { RankingsComponent } from './rankings/rankings.component';

@NgModule({
  declarations: [
    AppComponent,
    BattleComponent,
    ResultsComponent,
    RankingsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpModule
  ],
  providers: [BattleService],
  bootstrap: [AppComponent]
})
export class AppModule { }
