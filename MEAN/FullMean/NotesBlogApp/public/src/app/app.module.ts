import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {FormsModule} from '@angular/forms';
import {HttpModule} from "@angular/http";
import {NotesService} from "./notes.service"

import { AppRoutingModule } from "./app-routing.module";


import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';

@NgModule({
  declarations: [
    AppComponent,
    MainComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpModule,
    FormsModule

  ],
  providers: [NotesService],
  bootstrap: [AppComponent]
})
export class AppModule { }
