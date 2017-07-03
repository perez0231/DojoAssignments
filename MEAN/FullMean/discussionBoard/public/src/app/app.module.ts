import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {FormsModule} from '@angular/forms'
import { HttpModule } from '@angular/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { QuestionsComponent } from './questions/questions.component';
import { MessageService } from './message.service';
import { AllpostsComponent } from './allposts/allposts.component';
import { ShowComponent } from './show/show.component';
import { AnswerComponent } from './answer/answer.component'

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    QuestionsComponent,
    AllpostsComponent,
    ShowComponent,
    AnswerComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpModule,
    FormsModule,

  ],
  providers: [MessageService],
  bootstrap: [AppComponent]
})
export class AppModule { }
