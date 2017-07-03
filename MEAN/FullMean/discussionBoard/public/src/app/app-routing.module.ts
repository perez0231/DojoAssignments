import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { QuestionsComponent } from './questions/questions.component';
import { AllpostsComponent } from './allposts/allposts.component'
import { ShowComponent } from './show/show.component'
import { AnswerComponent } from './answer/answer.component'



const routes: Routes = [
  { path: '', pathMatch: "full", component: LoginComponent},
  { path: 'questions', component: QuestionsComponent},
  { path: 'allquestions', component: AllpostsComponent},
  {path: 'questions/:id', component: ShowComponent},
  {path: 'answers/:id', component: AnswerComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
