import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AnimalsListComponent } from './animals-list/animals-list.component';

const routes: Routes = [
  {path: '', pathMatch: 'full', component: AnimalsListComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
