import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {NgForm} from '@angular/forms'
import {FormsModule} from '@angular/forms'

import { AppComponent } from './app.component';
import { MyComponentComponent } from './my-component/my-component.component';
import { MainComponent } from './main/main.component';
import { HeaderComponent } from './header/header.component';
import { TopComponent } from './main/top/top.component';
import { BottomComponent } from './main/bottom/bottom.component';

@NgModule({
  declarations: [
    AppComponent,
    MyComponentComponent,
    MainComponent,
    HeaderComponent,
    TopComponent,
    BottomComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
