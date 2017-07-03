import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AnimalsService } from './animals.service';
import {HttpModule} from "@angular/http"

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AnimalsListComponent } from './animals-list/animals-list.component';

@NgModule({
  declarations: [
    AppComponent,
    AnimalsListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpModule
  ],
  providers: [AnimalsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
