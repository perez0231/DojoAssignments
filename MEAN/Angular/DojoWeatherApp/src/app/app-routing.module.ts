import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SeattleComponent } from './seattle/seattle.component';
import { SanJoseComponent } from './san-jose/san-jose.component';
import { BurbankComponent } from './burbank/burbank.component';
import { DallasComponent } from './dallas/dallas.component';
import { ChicagoComponent } from './chicago/chicago.component';
import { DCComponent } from './dc/dc.component';


const routes: Routes = [
  { path: '', pathMatch: 'full', component: DCComponent},
  {path: 'burbank', component: BurbankComponent },
  {path: 'seattle', component: SeattleComponent },
  {path: 'sanjose', component: SanJoseComponent },
  {path: 'dallas', component: DallasComponent },
  {path: 'chicago', component: ChicagoComponent}

]
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
