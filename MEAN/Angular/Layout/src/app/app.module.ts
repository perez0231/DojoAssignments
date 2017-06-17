import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { MainCompComponent } from './main-comp/main-comp.component';
import { MainComponent } from './main-comp/main/main.component';
import { LeftComponent } from './main-comp/left/left.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    MainCompComponent,
    MainComponent,
    LeftComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
